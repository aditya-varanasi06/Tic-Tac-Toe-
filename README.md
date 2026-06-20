# 🎮 Tic Tac Toe Game

A modern **Tic Tac Toe** desktop game built with **Python** and **Tkinter**, featuring both **Player vs Player** and **Player vs AI** game modes. The application includes a clean dark-themed UI, score tracking, sound effects, and two AI difficulty levels, making it suitable for beginners learning GUI development and game logic in Python. 

---

## ✨ Features

* 🎲 Player vs Player mode
* 🤖 Player vs AI mode

  * Easy (Random AI)
  * Hard (Minimax Algorithm)
* 🎨 Modern dark-themed interface
* 🔊 Click and win sound effects (Windows)
* 🏆 Score tracking
* 🔄 Restart game option
* 📋 Main menu navigation
* ✅ Automatic win and draw detection
* 🟩 Winning combination highlighting

---

## 🛠️ Technologies Used

* Python 3.x
* Tkinter
* Random module
* Winsound (Windows only)

---

## 📂 Project Structure

```
tic-tac-toe/
│
├── index.py          # Main application
└── README.md         # Project documentation
```

---

## 🚀 Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/tic-tac-toe.git
```

2. Navigate to the project folder

```bash
cd tic-tac-toe
```

3. Run the application

```bash
python index.py
```

---

## 🎮 Game Modes

### Player vs Player

Two players take turns placing **X** and **O** on the board.

### Player vs AI

#### Easy Mode

The AI selects random available cells.

#### Hard Mode

The AI uses the **Minimax Algorithm**, making it nearly impossible to beat.

---

## 🧠 AI Algorithm

The Hard AI uses the **Minimax Algorithm**, which:

* Evaluates every possible move
* Chooses the optimal move
* Prevents losing whenever possible
* Plays perfectly

---

## 🎨 UI Highlights

* Dark mode interface
* Hover button effects
* Colored X and O symbols
* Winning cells highlighted in green
* Simple and responsive layout

---

## 🔊 Sound Effects

The game includes:

* Button click sound
* Winning sound

> **Note:** Sound effects use the `winsound` module and work only on Windows.

---

## 📋 Requirements

* Python 3.8 or higher
* Windows OS (for sound support)

No external libraries are required.

---

## 📸 Gameplay

* Select a game mode from the main menu.
* Players alternate turns.
* The game automatically detects wins and draws.
* Scores are updated after each completed game.
* Restart or return to the main menu at any time.

---

## 🔮 Possible Future Enhancements

* Adjustable board sizes (4×4, 5×5)
* Online multiplayer
* Custom player names
* Difficulty levels (Medium)
* Animations and transitions
* Cross-platform sound support
* Game history and statistics
* Theme customization

---

## 👨‍💻 Author

Developed as a Python GUI project to demonstrate:

* Tkinter GUI development
* Event-driven programming
* Game state management
* Artificial Intelligence using Minimax
* Python fundamentals

---

## 📄 License

This project is intended for educational and personal learning purposes. Feel free to modify, improve, and build upon it.
