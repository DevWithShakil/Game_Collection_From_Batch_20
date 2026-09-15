import pygame
import random

pygame.init()

# Screen
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Snake
snake = [(300, 200), (290, 200), (280, 200)]
direction = "RIGHT"

# Food
food = (
    random.randrange(0, WIDTH, 10),
    random.randrange(0, HEIGHT, 10)
)

clock = pygame.time.Clock()
score = 0
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"

            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"

            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"

            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Move snake
    head_x, head_y = snake[0]

    if direction == "UP":
        head_y -= 10
    elif direction == "DOWN":
        head_y += 10
    elif direction == "LEFT":
        head_x -= 10
    elif direction == "RIGHT":
        head_x += 10

    new_head = (head_x, head_y)
    snake.insert(0, new_head)

    # Eat food
    if new_head == food:
        score += 1
        food = (
            random.randrange(0, WIDTH, 10),
            random.randrange(0, HEIGHT, 10)
        )
    else:
        snake.pop()

    # Game over
    if (
        head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT or
        new_head in snake[1:]
    ):
        running = False

    # Draw
    screen.fill(BLACK)

    for part in snake:
        pygame.draw.rect(screen, GREEN, (part[0], part[1], 10, 10))

    pygame.draw.rect(screen, RED, (food[0], food[1], 10, 10))

    # Score
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(12)

pygame.quit()

print("Game Over!")
print("Your Score:", score)