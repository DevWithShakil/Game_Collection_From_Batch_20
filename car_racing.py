import pygame
import random

pygame.init()

# Screen
WIDTH = 500
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🏎️ Car Racing Game")

clock = pygame.time.Clock()

# Colors
GREEN = (40, 150, 40)
GRAY = (60, 60, 60)
WHITE = (255, 255, 255)
RED = (220, 30, 30)
BLUE = (30, 100, 220)
BLACK = (0, 0, 0)

# Player car
player = pygame.Rect(220, 580, 50, 90)
player_speed = 7

# Enemy cars
enemies = []
enemy_speed = 5

# Score
score = 0
font = pygame.font.Font(None, 40)

# Road lines
road_lines = []

for y in range(0, HEIGHT, 100):
    road_lines.append(pygame.Rect(245, y, 10, 60))

running = True
game_over = False

while running:

    clock.tick(60)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Restart after game over
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                player.x = 220
                enemies.clear()
                score = 0
                enemy_speed = 5
                game_over = False

    if not game_over:

        # Player movement
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.x -= player_speed

        if keys[pygame.K_RIGHT]:
            player.x += player_speed

        # Keep car on road
        if player.x < 150:
            player.x = 150

        if player.x > 300:
            player.x = 300

        # Move road lines
        for line in road_lines:
            line.y += enemy_speed

            if line.y > HEIGHT:
                line.y = -60

        # Create enemy cars
        if random.randint(1, 50) == 1:
            x = random.choice([160, 220, 280])
            enemy = pygame.Rect(x, -100, 50, 90)
            enemies.append(enemy)

        # Move enemies
        for enemy in enemies:
            enemy.y += enemy_speed

        # Remove enemies that leave screen
        for enemy in enemies[:]:
            if enemy.y > HEIGHT:
                enemies.remove(enemy)
                score += 1

        # Increase difficulty
        if score > 0 and score % 10 == 0:
            enemy_speed = 5 + score // 10

        # Collision
        for enemy in enemies:
            if player.colliderect(enemy):
                game_over = True

    # ---------------- DRAW ----------------

    # Grass
    screen.fill(GREEN)

    # Road
    pygame.draw.rect(screen, GRAY, (140, 0, 220, HEIGHT))

    # Road lines
    for line in road_lines:
        pygame.draw.rect(screen, WHITE, line)

    # Player car
    pygame.draw.rect(screen, BLUE, player)

    # Player windows
    pygame.draw.rect(
        screen,
        BLACK,
        (player.x + 10, player.y + 10, 30, 25)
    )

    # Enemy cars
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

        pygame.draw.rect(
            screen,
            BLACK,
            (enemy.x + 10, enemy.y + 10, 30, 25)
        )

    # Score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (20, 20))

    # Game over screen
    if game_over:
        game_over_text = font.render("GAME OVER!", True, RED)
        restart_text = font.render("Press R to restart", True, WHITE)

        screen.blit(
            game_over_text,
            (170, 300)
        )

        screen.blit(
            restart_text,
            (130, 350)
        )

    pygame.display.update()

pygame.quit()