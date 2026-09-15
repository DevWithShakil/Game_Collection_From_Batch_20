import tkinter as tk
import random

score = 0
time_left = 30

window = tk.Tk()
window.title("🎯 Click the Target")
window.geometry("600x500")

score_label = tk.Label(window, text="Score: 0", font=("Arial", 20))
score_label.pack()

canvas = tk.Canvas(window, width=600, height=430, bg="black")
canvas.pack()


def move_target():
    x = random.randint(30, 570)
    y = random.randint(30, 400)

    canvas.coords(target, x - 20, y - 20, x + 20, y + 20)


def click_target(event):
    global score

    score += 1
    score_label.config(text=f"Score: {score}")
    move_target()


def countdown():
    global time_left

    if time_left > 0:
        time_left -= 1
        window.after(1000, countdown)
    else:
        canvas.delete(target)
        score_label.config(text=f"GAME OVER! 🎮 Score: {score}")


target = canvas.create_oval(
    280, 190, 320, 230,
    fill="red"
)

canvas.tag_bind(target, "<Button-1>", click_target)

move_target()
countdown()

window.mainloop()