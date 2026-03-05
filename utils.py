import numpy as np

def print_board(state):
    board = state[-1]
    symbols = {0: '.', 1: 'X', -1: 'O'}
    for row in board:
        print(' '.join(symbols[val] for val in row))
    print()
