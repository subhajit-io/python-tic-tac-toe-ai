# python-tic-tac-toe-ai
Three levels of Tic-Tac-Toe AI in Python, ranging from random moves to an unbeatable Minimax algorithm.
# Python Tic Tac Toe - Unified Terminal Game

Welcome to my project! I built a complete Tic Tac Toe game in Python. Instead of just a simple script, I turned this into a full terminal application where you can play multiple matches, track your score, and choose how smart you want the computer to be.

---

## Features

* **Interactive Menu:** The game greets you, asks for your name, and lets you pick your marker (X or O).
* **Live Scorecard:** You can play up to 10 matches in a row. The game keeps track of your wins, the computer's wins, and draws, showing a scorecard after every round.
* **Final Results:** When you are done playing, it calculates the overall winner of the session.

---

## The Three Difficulty Levels

When you start the game, you can choose from three different AI modes:

### 1. Easy Mode
In this version, the computer just makes completely random moves by picking any empty spot on the board. It is very easy to beat and mainly serves as a warm-up.

### 2. Medium Mode
In this version, the computer plays much smarter. It actively checks the rows, columns, and diagonals. If it sees that you have already placed two marks in a line, it will immediately block your win. If there is nothing to block, it picks a random open spot.

### 3. Hard Mode
This is the final level where I implemented the Minimax algorithm. The computer checks every single possible future move on the board before making its decision. It plays perfectly, so it is completely unbeatable. The best result you can get against this mode is a draw.

---

## How to Play

To play the game on your computer, just open your terminal or command prompt, go to the folder where you downloaded the file, and type:

`python ox_main.py`

The game will handle all the wrong inputs (like typing letters instead of numbers or picking a spot that is already taken) without crashing.

---

## My Coding Journey and Using AI

While making this project, I took help from AI tools to learn new things and fix errors:
* **Learning concepts:** I used AI to understand the logic behind game trees and how the Minimax algorithm actually works, which helped me convert the theory into Python code for the Hard mode.
* **Finding bugs:** I used AI like a senior programmer to review my code. It helped me find and fix a bug where the game got stuck in an infinite loop during draw matches, and helped me make the user input validation safer so the game does not crash if a user types wrong inputs.
