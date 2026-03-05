from envs.tictactoe import TicTacToe
from mcts import MCTS
import numpy as np

def get_human_action(game, state, to_play):
    board_size = game.board_size
    legal_actions = game.get_is_legal_actions(state, to_play)
    while True:
        try:
            user_input = input(f"Player {to_play}, enter your move (row col, e.g., '1 1'): ")
            parts = user_input.split()
            if len(parts) == 2:
                r, c = map(int, parts)
                action = r * board_size + c
            else:
                action = int(parts[0])
            
            if 0 <= action < board_size * board_size and legal_actions[action]:
                return action
            else:
                print(f"Invalid or illegal move. Legal actions are: {np.where(legal_actions)[0]}")
        except (ValueError, IndexError):
            print("Invalid input. Enter 'row col' (e.g., '1 1') or a single action index.")

def main():
    game = TicTacToe()
    args = {
        'num_simulations': 1000,
        'exploration_constant': 1.41
    }
    mcts = MCTS(game, args)
    
    state = game.get_initial_state()
    to_play = 1 # X starts first
    
    print("Welcome to TicTacToe! You are playing against MCTS.")
    human_side = input("Choose your side (1 for X, -1 for O). X starts first [default: 1]: ")
    if human_side == "-1":
        human_player = -1
    else:
        human_player = 1
        
    print("\nInitial Board:")
    from utils import print_board
    print_board(state)
    
    while not game.is_terminal(state):
        if to_play == human_player:
            print(f"Your turn (Player {to_play})...")
            action = get_human_action(game, state, to_play)
        else:
            print(f"MCTS's turn (Player {to_play})...")
            action = mcts.search(state, to_play)
            print(f"MCTS chooses action {action} (row {action // game.board_size}, col {action % game.board_size})")
        
        state = game.get_next_state(state, action, to_play)
        print_board(state)
        to_play = -to_play
        
    winner = game.get_winner(state)
    if winner == 0:
        print("It's a draw!")
    else:
        print(f"Player {winner} wins!")

if __name__ == "__main__":
    main()
