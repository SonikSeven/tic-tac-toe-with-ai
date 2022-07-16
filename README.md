# Tic-Tac-Toe with AI

This project implements a Tic-Tac-Toe game that can be played in the console against an AI opponent or another player. The AI comes with different difficulty levels ranging from easy to hard, including a perfect-play AI developed using the Minimax algorithm.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/tic-tac-toe-with-ai.git
```

## How to Run

To run the program, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using Python:

```
python main.py
```

## How to Play

- The game is played on a 3x3 grid.
- Players take turns to mark a position on the grid with their symbol (X or O).
- The first player to align three of their symbols vertically, horizontally, or diagonally wins the game.
- To start a game, enter the command `start` followed by the desired player types for X and O. For example, `start user hard` to play against the hard difficulty AI.
- To input your move as a player, enter the coordinates as two numbers (row and column), each between 1 and 3, separated by space.

## AI Difficulty Levels

- `easy`: The AI performs random moves.
- `medium`: The AI blocks the opponent's winning move or wins if possible.
- `hard`: The AI uses the Minimax algorithm for a flawless game where winning is impossible, aiming for a draw as the worse outcome.

## License

This project is licensed under the [MIT License](LICENSE.txt).
