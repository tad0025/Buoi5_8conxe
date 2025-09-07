import tkinter as tk
from collections import deque

BOARD_SIZE = 8
CELL_SIZE = 60
LIGHT_COLOR = "#f0d9b5"
DARK_COLOR = "#b58863"
ROOK_COLOR = "#1976d2"
FONT_FALLBACK = ("Segoe UI Symbol", int(CELL_SIZE * 0.6))

def bfs():
    start = []
    q = deque([start])

    while q:
        state = q.popleft()
        row = len(state)

        if row == BOARD_SIZE:
            return [(r, state[r]) for r in range(BOARD_SIZE)]

        used = set(state)
        for col in range(BOARD_SIZE):
            if col not in used:
                q.append(state + [col])

    return None

def draw(canvas: tk.Canvas, rooks=None):
    canvas.delete("all")
    # Vẽ bàn cờ
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            x0 = c * CELL_SIZE
            y0 = r * CELL_SIZE
            x1 = x0 + CELL_SIZE
            y1 = y0 + CELL_SIZE
            color = LIGHT_COLOR if (r + c) % 2 == 0 else DARK_COLOR
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=color)

    # Vẽ trục A-H và 1-8
    for i in range(BOARD_SIZE):
        col_label = chr(ord('A') + i)
        canvas.create_text(i * CELL_SIZE + CELL_SIZE/2, 10,
                           text=col_label, font=("Arial", 10, "bold"))
        row_label = str(BOARD_SIZE - i)
        canvas.create_text(10, i * CELL_SIZE + CELL_SIZE/2,
                           text=row_label, font=("Arial", 10, "bold"))

    # Vẽ quân xe
    if rooks:
        for (r, c) in rooks:
            x = c * CELL_SIZE + CELL_SIZE/2
            y = r * CELL_SIZE + CELL_SIZE/2
            canvas.create_text(x, y, text="♖", font=FONT_FALLBACK, fill=ROOK_COLOR)

def start(root: tk.Tk):
    root.title("Đặt 8 Quân Xe bằng BFS")
    root.resizable(False, False)

    wrapper = tk.Frame(root)
    wrapper.pack(padx=12, pady=12)

    left_frame = tk.Frame(wrapper)
    left_frame.grid(row=1, column=0, padx=(0, 12))
    tk.Label(left_frame, text="Bàn cờ trống", font=("Arial", 12)).pack(pady=(0, 8))
    left_canvas = tk.Canvas(left_frame, width=BOARD_SIZE*CELL_SIZE, height=BOARD_SIZE*CELL_SIZE,
                            highlightthickness=1, highlightbackground="#999")
    left_canvas.pack()

    right_frame = tk.Frame(wrapper)
    right_frame.grid(row=1, column=1)
    tk.Label(right_frame, text="Bàn cờ có 8 quân xe (BFS)", font=("Arial", 12)).pack(pady=(0, 8))
    right_canvas = tk.Canvas(right_frame, width=BOARD_SIZE*CELL_SIZE, height=BOARD_SIZE*CELL_SIZE,
                             highlightthickness=1, highlightbackground="#999")
    right_canvas.pack()

    controls = tk.Frame(wrapper)
    controls.grid(row=2, column=0, columnspan=2, pady=10)

    def refresh():
        draw(left_canvas, None)
        draw(right_canvas, bfs())

    tk.Button(controls, text="Giải bằng BFS", command=refresh).pack()
    refresh()

# Run GUI
root = tk.Tk()
start(root)

# Căn giữa màn hình
root.update_idletasks()
width, height = root.winfo_width(), root.winfo_height()
sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
x, y = (sw // 2) - (width // 2), (sh // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")
root.mainloop()