# python-tic-tac-toe-ai
Three levels of Tic-Tac-Toe AI in Python, ranging from random moves to an unbeatable Minimax algorithm.
# Python Tic Tac Toe - From Simple Logic to Minimax AI

Welcome to my project! I built a Tic Tac Toe game in Python with three different levels of computer intelligence. This project shows how I started with basic random moves, moved up to writing custom rules to block the player, and finally implemented the Minimax algorithm to make the computer unbeatable

## Game Levels

### 1. Easy Mode (ox_random.py)
In this version, the computer just makes completely random moves using the random library. It does not try to win just tries to block you. I wrote this first to get the basic game board grid and player input loop working correctly.

### 2. Medium Mode (ox_heuristic.py)
In this version, I cleaned up the code layout, fixed logic issues, and made the computer's decision-making more structured. It handles the board checks more efficiently before making its move to block the player.

### 3. Hard Mode (ox_minimax.py)
This is the final version where I implemented the Minimax algorithm. The computer checks every single possible future move on the board before making its decision. It plays perfectly, so it is impossible to beat it. The best result you can get against this version is a draw game.



## My Coding Journey and Using AI

While making this project, I took help from AI tools to learn new things and fix errors:

# Learning concepts: 
  I used AI to understand the logic behind game trees and how the Minimax algorithm actually works, which helped me convert the theory into Python code.

# Finding bugs: 
  I used AI like a senior programmer to review my code. It helped me find and fix a major bug where the game got stuck in an infinite loop during draw matches, and     helped me make the user input validation safer so the game does not crash if a user types wrong inputs.
