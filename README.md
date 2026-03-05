# MCTS - Monte Carlo Tree Search Implementation

This repository contains a Python implementation of the Monte Carlo Tree Search (MCTS) algorithm, applied to classic board games like Tic-Tac-Toe and Gomoku.

## Features

- **MCTS Core Algorithm**: Pure Python implementation of MCTS including Selection, Expansion, Simulation, and Backpropagation.
- **Game Environments**:
  - **Tic-Tac-Toe**: Standard 3x3 game.
  - **Gomoku**: Support for various board sizes (default 15x15) and Renju rules (forbidden moves for black).
- **Interactive Play**: Play against the MCTS AI directly from your terminal.
- **Extensible**: Easily add new games by implementing the game logic interface.

## Project Structure

```text
.
├── envs/
│   ├── gomoku.py      # Gomoku game logic and Renju rules
│   └── tictactoe.py   # Tic-Tac-Toe game logic
├── mcts.py            # Core MCTS algorithm implementation
├── main.py            # Entry point to play Tic-Tac-Toe vs MCTS
├── test_gomoku.py     # Script to test MCTS on Gomoku
├── utils.py           # Utility functions (e.g., board printing)
└── LICENSE            # MIT License
```

## Getting Started

### Prerequisites

- Python 3.x
- NumPy
- SciPy (for Gomoku's advanced rule checks)

Install dependencies:

```bash
pip install numpy scipy
```

### Running the Project

To play a game of Tic-Tac-Toe against the MCTS AI:

```bash
python main.py
```

To run a Gomoku simulation (AI vs AI on a 9x9 board):

```bash
python test_gomoku.py
```

## How it Works

MCTS builds a search tree by repeatedly performing four steps:
1. **Selection**: Start from root and select child nodes using UCB (Upper Confidence Bound) until a leaf node is reached.
2. **Expansion**: If the leaf node is not terminal, create child nodes for untried actions.
3. **Simulation**: Perform a random rollout from the new node until a terminal state is reached.
4. **Backpropagation**: Update the statistics (visit count and value) of the nodes along the path from the expanded node back to the root.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
