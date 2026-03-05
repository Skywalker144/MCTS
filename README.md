# MCTS: Monte Carlo Tree Search Foundations

This repository contains a robust Python implementation of the Monte Carlo Tree Search (MCTS) algorithm. It serves as the algorithmic foundation for the **SkyZero** series, demonstrating the core principles of search-based decision-making in board games.

## Project Context
This MCTS implementation is the baseline for more advanced reinforcement learning projects:
- **MCTS Foundations (Current)**: Pure search-based AI using random rollouts.
- [SkyZero_V0](../SkyZero_V0/README.md): AlphaZero (MCTS + Neural Networks).
- [SkyZero_V2](../SkyZero_V2/README.md): AlphaZero with KataGo optimizations.
- [SkyZero_V3](../SkyZero_V3/README.md): Gumbel AlphaZero implementation.

## Core Features
- **MCTS Lifecycle**: Full implementation of the four stages:
    1. **Selection**: Using UCB1 (Upper Confidence Bound) to balance exploration and exploitation.
    2. **Expansion**: Growing the search tree at leaf nodes.
    3. **Simulation**: Random rollouts (playouts) to estimate state value.
    4. **Backpropagation**: Updating node statistics from outcome results.
- **Environment Support**:
    - **Tic-Tac-Toe**: Standard 3x3 implementation.
    - **Gomoku**: Support for various board sizes and Renju rules.
- **Interactive Mode**: Play directly against the MCTS AI in the terminal.

## Project Structure
- `mcts.py`: Core logic of the MCTS algorithm.
- `envs/`: Game environment definitions (Tic-Tac-Toe, Gomoku).
- `main.py`: Entry point for terminal-based play.
- `test_gomoku.py`: Benchmarking and simulation scripts.

## Quick Start
### Installation
```bash
pip install numpy scipy
```

### Run Tic-Tac-Toe vs MCTS
```bash
python main.py
```

### Run Gomoku Simulation
```bash
python test_gomoku.py
```

## License
Licensed under the [MIT License](LICENSE).
