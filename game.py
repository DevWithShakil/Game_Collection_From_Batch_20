import tkinter as tk
import random

GRID_SIZE = 5
CELL_SIZE = 60
COLORS = ["#FF5733", "#33FF57", "#3357FF", "#F1C40F"]  # Red, Green, Blue, Yellow

class DotsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Dots")
        self.score = 0

        # Score board
        self.label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 18, "bold"))
        self.label.pack(pady=10)

        # Game Canvas
        self.canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE, bg="#2C3E50")
        self.canvas.pack(padx=20, pady=10)
        self.canvas.bind("<Button-1>", self.click_dot)

        # Initialize grid with random colors
        self.grid = [[random.choice(COLORS) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.draw_grid()

    def draw_grid(self):
        """Redraws all dots on the grid."""
        self.canvas.delete("all")
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                x = c * CELL_SIZE + CELL_SIZE // 2
                y = r * CELL_SIZE + CELL_SIZE // 2
                color = self.grid[r][c]
                self.canvas.create_oval(x-20, y-20, x+20, y+20, fill=color, outline="")

    def click_dot(self, event):
        """Triggers when a player clicks a dot."""
        c = event.x // CELL_SIZE
        r = event.y // CELL_SIZE

        if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE:
            target_color = self.grid[r][c]
            matches = self.find_connected(r, c, target_color, set())

            # Only clear if 2 or more matching adjacent dots are found
            if len(matches) > 1:
                for mr, mc in matches:
                    self.grid[mr][mc] = random.choice(COLORS)
                
                self.score += len(matches) * 10
                self.label.config(text=f"Score: {self.score}")
                self.draw_grid()

    def find_connected(self, r, c, color, visited):
        """Recursively checks adjacent dots for matching colors."""
        if (r, c) in visited or not (0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE):
            return visited
        if self.grid[r][c] != color:
            return visited

        visited.add((r, c))
        # Check adjacent neighbors: Up, Down, Left, Right
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            self.find_connected(r + dr, c + dc, color, visited)
        return visited

if __name__ == "__main__":
    root = tk.Tk()
    game = DotsGame(root)
    root.mainloop()