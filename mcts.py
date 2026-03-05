import math
import numpy as np

class Node:
    def __init__(self, state, to_play, action_taken=None, parent=None):
        self.state = state
        self.to_play = to_play
        self.parent = parent
        self.action_taken = action_taken
        self.children = []
        
        self.v = 0
        self.n = 0
        self._untried_actions = None

    def is_fully_expanded(self, game):
        if self._untried_actions is None:
            legal_actions = game.get_is_legal_actions(self.state, self.to_play)
            self._untried_actions = np.where(legal_actions)[0].tolist()
        return len(self._untried_actions) == 0

    def get_ucb(self, exploration_constant):
        # 该函数将在选择的时候被调用，
        # 而且是父节点去调用子节点的get_ucb，所以
        # 对于父节点来说，子节点的q需要取反（父节点选子节点需要选对父节点最不利的子节点）
        if self.n == 0:
            return np.inf
        q = -self.v / self.n
        u = exploration_constant * math.sqrt(math.log(self.parent.n) / self.n)
        return q + u
    
    def update(self, value):
        self.v += value
        self.n += 1


class MCTS:
    def __init__(self, game, args):
        self.game = game
        self.args = args

    def search(self, state, to_play):
        root = Node(state, to_play)
        
        for _ in range(self.args['num_simulations']):
            node = root
            
            # 1. Selection
            while not self.game.is_terminal(node.state) and node.is_fully_expanded(self.game):
                node = self._select(node)
            
            # 2. Expansion
            if not self.game.is_terminal(node.state):
                node = self._expand(node)
            
            # 3. Simulation
            winner = self._simulate(node.state, node.to_play)  # 绝对视角下的winner
            value = winner * node.to_play  # 转换成对于当前节点的相对胜负
            
            # 4. Backpropagation
            self._backpropagate(node, value)
            
        best_child = max(root.children, key=lambda c: c.n)
        return best_child.action_taken

    def _select(self, node):
        # 根据UCB公式，选择UCB值最大的子节点
        max_ucb = -np.inf
        best_child = None
        for child in node.children:
            if child.get_ucb(self.args['exploration_constant']) > max_ucb:
                max_ucb = child.get_ucb(self.args['exploration_constant'])
                best_child = child
        return best_child

    def _expand(self, node):
        # 随机选择一个动作
        action_idx = np.random.randint(len(node._untried_actions))  # 先随机一个动作索引（在node的棋局的untried_actions中）
        action = node._untried_actions[action_idx]
        node._untried_actions.pop(action_idx)  # 该动作接下来将进行扩展，所以不再是未尝试动作，故移除

        next_state = self.game.get_next_state(node.state, action, node.to_play)
        child_node = Node(
            state=next_state,
            to_play=-node.to_play,
            action_taken=action,
            parent=node
        )
        node.children.append(child_node)

        return child_node

    def _simulate(self, state, to_play):
        # 随机行动，将游戏玩至终局并且返回winner
        current_state = state.copy()
        current_to_play = to_play
        while not self.game.is_terminal(current_state):
            legal_actions = self.game.get_is_legal_actions(current_state, current_to_play)
            actions_idxs = np.where(legal_actions)[0]  # 获取合法动作索引列表
            action = np.random.choice(actions_idxs)  # 随机选择一个合法动作
            current_state = self.game.get_next_state(current_state, action, current_to_play)
            current_to_play = -current_to_play
            
        winner = self.game.get_winner(current_state)
        return winner

    def _backpropagate(self, node, value):
        while node is not None:
            node.update(value)
            value = -value  # 每次传播都翻转value（不同视角）
            node = node.parent
