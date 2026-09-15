import turtle
import random

# Setup
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Retro Car Racing")
screen.tracer(0)

# Car
car = turtle.Turtle()
car.shape("square")
car.color("red")
car.shapesize(0.8, 1.5)
car.penup()
car.goto(0, -250)

# Game variables
car_speed = 0
obstacles = []
score = 0
game_over = False

# Instructions
info = turtle.Turtle()
info.hideturtle()
info.penup()
info.color("white")
info.goto(-350, 280)
info.write("ARROW KEYS: Move | Space: Accelerate | Score:", font=("Arial", 12, "normal"))

# Score display
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("lime")
score_display.goto(200, 280)

# Game over display
game_over_text = turtle.Turtle()
game_over_text.hideturtle()
game_over_text.penup()
game_over_text.color("white")

# Road lines (decorative)
def draw_road_lines():
    line = turtle.Turtle()
    line.speed(0)
    line.hideturtle()
    line.color("white")
    for y in range(-300, 300, 50):
        line.penup()
        line.goto(-20, y)
        line.pendown()
        line.goto(20, y)

draw_road_lines()

# Obstacle class
class Obstacle:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.shape("square")
        self.turtle.color("yellow")
        self.turtle.shapesize(0.8, 1.5)
        self.turtle.penup()
        x = random.choice([-100, -50, 0, 50, 100])
        self.turtle.goto(x, 300)
        self.speed = 8
    
    def move(self):
        self.turtle.sety(self.turtle.ycor() - self.speed)
    
    def is_offscreen(self):
        return self.turtle.ycor() < -350
    
    def remove(self):
        self.turtle.hideturtle()

# Input handling
def move_left():
    if car.xcor() > -150:
        car.setx(car.xcor() - 20)

def move_right():
    if car.xcor() < 150:
        car.setx(car.xcor() + 20)

def accelerate():
    global car_speed
    car_speed = min(car_speed + 1, 15)

screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(accelerate, "space")
screen.listen()

# Main game loop
spawn_timer = 0

while not game_over:
    screen.update()
    
    # Spawn obstacles
    spawn_timer += 1
    if spawn_timer > max(20, 50 - score // 5):
        obstacles.append(Obstacle())
        spawn_timer = 0
    
    # Move obstacles
    for obs in obstacles:
        obs.move()
        if obs.is_offscreen():
            obs.remove()
            obstacles.remove(obs)
            score += 1
        # Collision detection
        if car.distance(obs.turtle) < 25:
            game_over = True
    
    # Update score
    score_display.clear()
    score_display.write(str(score), font=("Arial", 24, "bold"))
    
    # Slower car deceleration
    if car_speed > 0:
        car_speed -= 0.1

# Game over
game_over_text.goto(0, 0)
game_over_text.write(f"GAME OVER\nFinal Score: {score}", align="center", 
                     font=("Arial", 40, "bold"))

screen.update()
screen.mainloop()