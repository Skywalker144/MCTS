from envs.gomoku import Gomoku
from mcts import MCTS
import numpy as np
import time

def main():
    # Use a smaller board for testing if needed, but Gomoku defaults to 15x15
    game = Gomoku(board_size=9) 
    args = {
        'num_simulations': 100,
        'exploration_constant': 1.41
    }
    mcts = MCTS(game, args)
    
    state = game.get_initial_state()
    to_play = 1 # Black
    
    from utils import print_board
    
    while not game.is_terminal(state):
        start_time = time.time()
        action = mcts.search(state, to_play)
        elapsed = time.time() - start_time
        
        row, col = action // game.board_size, action % game.board_size
        print(f"Player {to_play} chooses ({row}, {col}) - search took {elapsed:.2f}s")
        
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
