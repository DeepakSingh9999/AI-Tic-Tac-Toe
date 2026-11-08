# Unbeatable Tic-Tac-Toe AI 🤖❌⭕

A command-line implementation of the classic Tic-Tac-Toe game featuring an intelligent AI opponent powered by the **Minimax algorithm**. The AI calculates optimal moves recursively, making it completely unbeatable—you can either tie or lose!

---

## 🚀 Features

- **Interactive Terminal Gameplay:** Clean, text-based grid rendering that updates in real-time.
- **Unbeatable AI (`O`):** Uses the Minimax decision-making algorithm to evaluate every future board state.
- **Robust Error Handling:** Validates user inputs to prevent crashes from out-of-range choices, non-integers, or occupied cells.

---

## 📋 Requirements

- Python 3.x installed on your system. (No external libraries or dependencies are required as it uses Python's built-in `math` module).

---

## 🕹️ How to Run

1. Save the Python script to your machine, for example as `tictactoe.py`.
2. Open your terminal or command prompt, navigate to the folder containing the file, and run:
   ```bash
   python tictactoe.py

---

## 🎮 Game Rules & Controls

1. You play as X and always go first.
2. The AI plays as O.
3. The board positions correspond to numbers 1 through 9:

Plaintext

 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
7 | 8 | 9
-----------

    When prompted, type a number from 1 to 9 to place your 'X' in that cell.

---

## 🧠 How the AI Works (Minimax)

The AI evaluates all possible moves using a recursive backtracking strategy:

    AI Wins (O): Evaluated with a score of +1

    Human Wins (X): Evaluated with a score of -1

    Tie Game: Evaluated with a score of 0

The AI acts as the maximizer trying to get the highest possible score, while predicting you (the minimizer) to make the best possible counter-moves.
