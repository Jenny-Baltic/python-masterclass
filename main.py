import pygame
import sys
import os
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets", "images", "spaceship_pl.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midleft = (25, HEIGHT // 2)
        self.speed = 5

    def move_player(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
                self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
                self.rect.y += self.speed 
        
    def update(self):
         self.move_player()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, location):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets", "images", "bullet.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.speed = 7

    def move_bullet(self):
        self.rect.x += self.speed

    def destroy_bullet(self):
        if self.rect.right > WIDTH:
            self.kill()

    def update(self):
        self.move_bullet()
        self.destroy_bullet()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type):
        super().__init__()
        if enemy_type == 1:
            self.image = pygame.image.load(os.path.join("assets", "images", "spaceship_en_one.png")).convert_alpha()
        elif enemy_type == 2:
            self.image = pygame.image.load(os.path.join("assets", "images", "spaceship_en_two.png")).convert_alpha()    
        elif enemy_type == 3:       
            self.image = pygame.image.load(os.path.join("assets", "images", "spaceship_en_three.png")).convert_alpha()
        elif enemy_type == 4:
            self.image = pygame.image.load(os.path.join("assets", "images", "spaceship_en_four.png")).convert_alpha()
        else:
            self.image = pygame.image.load(os.path.join("assets", "images", "spaceship_en_five.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH + self.rect.width)
        lane = random.randint(1, 3)
        if lane == 1:
            self.rect.y = 0
        elif lane == 2:
            self.rect.y = (HEIGHT // 2 - (self.rect.height // 2))
        else:
            self.rect.y = (HEIGHT - (self.rect.height))
        self.speed = 5

    def move_enemy(self):
        self.rect.x -= self.speed

    def destroy_enemy(self):
        if self.rect.right < 0:
            self.kill()
    
    def update(self):
        self.move_enemy()
        self.destroy_enemy()

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60
BACKGROUND_SCROLL_SPEED = 2

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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
player_sprite = pygame.sprite.GroupSingle()
player_sprite.add(Player())

# Bullets
bullet_sprites = pygame.sprite.Group()
bullet_cooldown = 800
last_bullet_time = 0

# Score
spaceship = pygame.image.load(os.path.join("assets", "images", "spaceship.png")).convert_alpha()
spaceship_rect = spaceship.get_rect()
spaceship_rect.topleft = (25, 25)
score = 0
info_font = pygame.font.Font(os.path.join("assets", "fonts", "LuckiestGuy-Regular.ttf"), 32)

# Lives
heart_frame_one = pygame.image.load(os.path.join("assets", "images", "hearts", "frame-1.png")).convert_alpha()
heart_frame_two = pygame.image.load(os.path.join("assets", "images", "hearts", "frame-2.png")).convert_alpha()
heart_frame_three = pygame.image.load(os.path.join("assets", "images", "hearts", "frame-3.png")).convert_alpha()
heart_frame_four = pygame.image.load(os.path.join("assets", "images", "hearts", "frame-4.png")).convert_alpha()
heart_frame_five = pygame.image.load(os.path.join("assets", "images", "hearts", "frame-5.png")).convert_alpha()
heart_frame_six = pygame.image.load(os.path.join("assets", "images", "hearts", "frame-6.png")).convert_alpha()
heart_frame_seven = pygame.image.load(os.path.join("assets", "images", "hearts", "frame-7.png")).convert_alpha()
heart_frame_eight = pygame.image.load(os.path.join("assets", "images", "hearts", "frame-8.png")).convert_alpha()
heart_frames = [heart_frame_one, heart_frame_two, heart_frame_three, heart_frame_four, heart_frame_five, heart_frame_six, heart_frame_seven, heart_frame_eight]
heart_rect = heart_frame_one.get_rect()
heart_rect.bottomleft = (25, 575)
current_frame = 0
frame_delay = 200
last_frame_time = 0
lives = 3

# Enemies
ennemy_sprires = pygame.sprite.Group()
spawn_enemy = 3000
last_enemy_time = 0

# Title Screen
title_font = pygame.font.Font(os.path.join("assets", "fonts", "LuckiestGuy-Regular.ttf"), 72)
inst_font = pygame.font.Font(os.path.join("assets", "fonts", "LuckiestGuy-Regular.ttf"), 32)
title_text = "SPACE ATTACK!"
inst_text = "Press ENTER to blast off"
title_text = title_font.render(title_text, True, WHITE)
title_text_rect = title_text.get_rect()
title_text_rect.center = (WIDTH // 2, 120)
inst_text = inst_font.render(inst_text, True, WHITE)
inst_text_rect = inst_text.get_rect()
inst_text_rect.center = ((WIDTH // 2), 480)
title_image = pygame.image.load(os.path.join("assets", "images", "spaceship_pl.png")).convert_alpha()
title_image_rect = title_image.get_rect()
title_image_rect.center = (WIDTH // 2, HEIGHT // 2)

# Sounds
boom = pygame.mixer.Sound(os.path.join("assets", "sounds", "boom.mp3"))
boom.set_volume(0.2)
shoot = pygame.mixer.Sound(os.path.join("assets", "sounds", "shoot.mp3"))
shoot.set_volume(0.2)
pygame.mixer.music.load(os.path.join("assets", "sounds", "xeon6.ogg"))
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

# Main game loop
game_over = True
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic 
    if not game_over:
        current_time = pygame.time.get_ticks()

        # Background Scroll
        if background_rect_one.x < -800:
            background_rect_one.x = 800
        if background_rect_two.x < -800:
            background_rect_two.x = 800
        background_rect_one.x -= BACKGROUND_SCROLL_SPEED
        background_rect_two.x -= BACKGROUND_SCROLL_SPEED
                
        # Create bullets
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and current_time - last_bullet_time >= bullet_cooldown:
                bullet_sprites.add(Bullet(player_sprite.sprite.rect.center))
                last_bullet_time = current_time
                shoot.play()

        # Create enemies
        if current_time - last_enemy_time >= spawn_enemy:
            ennemy_sprires.add(Enemy(random.randint(1, 5)))
            last_enemy_time = current_time

        # # Collision detection
        if pygame.sprite.spritecollide(player_sprite.sprite, ennemy_sprires, True):
            lives -= 1
            boom.play()

        if pygame.sprite.groupcollide(bullet_sprites, ennemy_sprires, True, True):
            score += 1
            boom.play()

        # Update score and check for Game Over
        score_text = info_font.render(f"{score}", True, WHITE)
        if lives < 1:
            game_over = True
        
        # Update lives and Level up
        lives_text = info_font.render(f"{lives}", True, WHITE)
        if score > 5:
            spawn_enemy = 2500
        if score > 10:
            spawn_enemy = 2000
        if score > 15:
            spawn_enemy = 1500
        if score > 20:
            spawn_enemy = 1000

        # Update the heart animation
        if current_time - last_frame_time >= frame_delay:
            current_frame = (current_frame + 1) % len(heart_frames)
            last_frame_time = current_time
        
        # Draw surfaces 
        screen.blit(background, background_rect_one)
        screen.blit(background, background_rect_two)
        screen.blit(spaceship, spaceship_rect)
        screen.blit(score_text, (80, 40))
        screen.blit(heart_frames[current_frame], heart_rect)
        screen.blit(lives_text, (80, 540))

        bullet_sprites.draw(screen)
        bullet_sprites.update()

        player_sprite.draw(screen)
        player_sprite.update()

        ennemy_sprires.draw(screen)
        ennemy_sprires.update()

    else: 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            game_over = False
        screen.fill(BLACK)
        spawn_enemy = 3000
        lives = 3
        score = 0
        screen.blit(background, (0, 0))
        screen.blit(title_text, title_text_rect)
        screen.blit(title_image, title_image_rect)
        screen.blit(inst_text, inst_text_rect)

    # Update dispay
    pygame.display.update()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()