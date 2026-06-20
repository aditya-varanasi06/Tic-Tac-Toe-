import tkinter as tk
import random
import winsound  # Windows only

# ---------- APP ----------
root = tk.Tk()
root.title("Tic Tac Toe ")
root.geometry("420x560")
root.config(bg="#12121a")
root.resizable(False, False)

# ---------- STATE ----------
board = [" "]*9
buttons = []
current_player = "X"
mode = "AI"
difficulty = "Easy"
scores = {"X": 0, "O": 0}
game_over = False

# ---------- COLORS ----------
BG = "#12121a"
BTN = "#1f1f2e"
HOVER = "#2d2d44"
TEXT = "#ffffff"
ACCENT = "#831873"
X_COLOR = "#ff4d6d"
O_COLOR = "#00bbf9"
WIN = "#6aef6e"

# ---------- SOUND ----------
def click_sound():
    try:
        winsound.Beep(700, 80)
    except:
        pass

def win_sound():
    try:
        winsound.Beep(1200, 200)
    except:
        pass

# ---------- UTIL ----------
def clear():
    for w in root.winfo_children():
        w.destroy()

# ---------- LOGIC ----------
def check_winner(p, b):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for w in wins:
        if all(b[i] == p for i in w):
            return w
    return None

def is_draw():
    return " " not in board

# ---------- MINIMAX ----------
def minimax(new_board, is_max):
    if check_winner("O", new_board): return 1
    if check_winner("X", new_board): return -1
    if " " not in new_board: return 0

    if is_max:
        best = -999
        for i in range(9):
            if new_board[i] == " ":
                new_board[i] = "O"
                score = minimax(new_board, False)
                new_board[i] = " "
                best = max(best, score)
        return best
    else:
        best = 999
        for i in range(9):
            if new_board[i] == " ":
                new_board[i] = "X"
                score = minimax(new_board, True)
                new_board[i] = " "
                best = min(best, score)
        return best

def best_move():
    best_score = -999
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# ---------- AI ----------
def ai_move():
    if difficulty == "Easy":
        return random.choice([i for i in range(9) if board[i]==" "])
    else:
        return best_move()

# ---------- GAME FLOW ----------
def on_click(i):
    global current_player, game_over
    if board[i] != " " or game_over:
        return

    click_sound()
    make_move(i, current_player)

    win = check_winner(current_player, board)
    if win:
        end_game(current_player, win)
        return

    if is_draw():
        end_game(None, None)
        return

    switch()
    update_status()

    if mode == "AI" and current_player == "O":
        root.after(random.randint(300, 600), ai_turn)

def ai_turn():
    move = ai_move()
    make_move(move, "O")

    win = check_winner("O", board)
    if win:
        end_game("O", win)
        return

    if is_draw():
        end_game(None, None)
        return

    switch()
    update_status()

def make_move(i, p):
    board[i] = p
    buttons[i].config(text=p,
                      fg=X_COLOR if p=="X" else O_COLOR)

def switch():
    global current_player
    current_player = "O" if current_player=="X" else "X"

# ---------- END ----------
def end_game(player, win_combo):
    global game_over
    game_over = True

    if win_combo:
        win_sound()
        for i in win_combo:
            buttons[i].config(bg=WIN)
        scores[player] += 1



# ---------- RESET ----------
def reset():
    global board, current_player, game_over
    board = [" "]*9
    current_player = "X"
    game_over = False
    game()

# ---------- UI ----------
def update_status():
    status.config(text=f"{current_player}'s Turn")

# ---------- MENU ----------
def menu():
    clear()

    tk.Label(root, text="TIC TAC TOE",
             font=("Arial",24,"bold"),
             fg=ACCENT, bg=BG).pack(pady=40)

    def btn(text, cmd):
        b = tk.Button(root, text=text,
                      font=("Arial",14,"bold"),
                      bg=BTN, fg=TEXT,
                      width=18, height=2,
                      bd=0, command=cmd)
        b.pack(pady=10)

        b.bind("<Enter>", lambda e: b.config(bg=HOVER))
        b.bind("<Leave>", lambda e: b.config(bg=BTN))

    btn("2 Player", lambda:start("2P"))
    btn("PLAYER Vs AI - Easy", lambda:start("AI","Easy"))
    btn("PLAYER Vs AI - Hard", lambda:start("AI","Hard"))

# ---------- START ----------
def start(m, diff="Easy"):
    global mode, difficulty
    mode = m
    difficulty = diff
    reset()

# ---------- GAME SCREEN ----------
def game():
    clear()
    global buttons, status
    buttons = []

    tk.Label(root, text=f"Score  X:{scores['X']}  O:{scores['O']}",
             fg=TEXT, bg=BG).pack(pady=10)

    status = tk.Label(root, text=f"{current_player}'s Turn",
                      font=("Arial",14,"bold"),
                      fg=TEXT, bg=BG)
    status.pack()

    frame = tk.Frame(root, bg=BG)
    frame.pack(pady=20)

    for i in range(9):
        b = tk.Button(frame, text="",
                      font=("Arial",26,"bold"),
                      width=4, height=2,
                      bg=BTN, fg=TEXT,
                      bd=0,
                      command=lambda i=i:on_click(i))
        b.grid(row=i//3, column=i%3, padx=6, pady=6)

        b.bind("<Enter>", lambda e,btn=b,i=i:
               btn.config(bg=HOVER) if board[i]==" " else None)
        b.bind("<Leave>", lambda e,btn=b:
               btn.config(bg=BTN))

        buttons.append(b)

    tk.Button(root, text="Restart",
              bg=ACCENT, fg="WHITE",
              command=reset).pack(pady=10)

    tk.Button(root, text="Main Menu",
              bg=BTN, fg=TEXT,
              command=menu).pack()

# ---------- RUN ----------
menu()
root.mainloop()