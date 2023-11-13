import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600

# Create a Pygame window and set its dimensions
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the window title
pygame.display.set_caption("Space Attack")

# Backgrounnd
background = pygame.image.load(os.path.join("assets", "images", "space_bg.png")).convert()

# Main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic 

    # Draw surfaces 
    screen.blit(background, (0,0))

    # Update dispay
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()