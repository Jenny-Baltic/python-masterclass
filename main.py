import pygame
import sys
import os
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60
PLAYER_SPEED = 5
BACKGROUND_SCROLL_SPEED = 2

# Create a Pygame window and set its dimensions
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the window title
pygame.display.set_caption("Space Attack")

# Clock
clock = pygame.time.Clock()

# Backgrounnd
background = pygame.image.load(os.path.join("assets", "images", "space_bg.png")).convert()
background_rect_one = background.get_rect()
background_rect_one.x = 0
background_rect_two = background.get_rect()
background_rect_two.x = 800

# Player
player = pygame.image.load(os.path.join("assets", "images", "spaceship_pl.png")).convert_alpha()
player_rect = player.get_rect()
player_rect.midleft = (25, HEIGHT //2)

# Enemies
enemy_one = pygame.image.load(os.path.join("assets", "images", "spaceship_en_one.png")).convert_alpha()
enemy_two = pygame.image.load(os.path.join("assets", "images", "spaceship_en_two.png")).convert_alpha()
enemy_three = pygame.image.load(
    os.path.join("assets", "images", "spaceship_en_three.png")).convert_alpha()
enemy_four = pygame.image.load(os.path.join("assets", "images", "spaceship_en_four.png")).convert_alpha()
enemy_five = pygame.image.load(os.path.join("assets", "images", "spaceship_en_five.png")).convert_alpha()
enemy_images = [enemy_one, enemy_two, enemy_three, enemy_four, enemy_five]
enemy_speed = 5
spawn_enemy = 3000
last_enemy_time = 0
enemies = []


# Main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic 
    current_time = pygame.time.get_ticks()

    # Background Scroll
    if background_rect_one.x < -800:
        background_rect_one.x = 800
    if background_rect_two.x < -800:
        background_rect_two.x = 800
    background_rect_one.x -= BACKGROUND_SCROLL_SPEED
    background_rect_two.x -= BACKGROUND_SCROLL_SPEED

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > 0:
            player_rect.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN] and player_rect.bottom < HEIGHT:
            player_rect.y += PLAYER_SPEED

    # Move and remove off screen enemies
    for enemy_image, enemy_rect in enemies:
            enemy_rect.x -= enemy_speed
    enemies = [(enemy_image, enemy_rect)
                   for enemy_image, enemy_rect in enemies if enemy_rect.right > 0]

     # Spawn enemies
    if current_time - last_enemy_time >= spawn_enemy:
        enemy_image = random.choice(enemy_images)
        enemy_rect = enemy_image.get_rect()
        enemy_rect.x = (WIDTH + enemy_rect.width)
        lane = random.randint(1, 3)
        if lane == 1:
            enemy_rect.y = 0
        elif lane == 2:
            enemy_rect.y = (HEIGHT // 2 - (enemy_rect.height // 2))
        else:
            enemy_rect.y = (HEIGHT - (enemy_rect.height))
        enemies.append((enemy_image, enemy_rect))
        last_enemy_time = current_time


    # Draw surfaces 
    screen.blit(background, background_rect_one)
    screen.blit(background, background_rect_two)
    screen.blit(player, player_rect)
    for enemy_image, enemy_rect in enemies:
            screen.blit(enemy_image, enemy_rect)

    # Update dispay
    pygame.display.update()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()