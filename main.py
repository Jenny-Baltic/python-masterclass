import pygame
import sys
import os

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


# Main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic 

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

    # Draw surfaces 
    screen.blit(background, background_rect_one)
    screen.blit(background, background_rect_two)
    screen.blit(player, player_rect)

    # Update dispay
    pygame.display.update()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()