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

class Background(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets", "images", "space_bg.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.x = position
        self.scroll_speed = 1

    def draw_static(self):
        screen.blit(self.image, self.rect)

    def move_background(self):
        self.rect.x -= self.scroll_speed
        if self.rect.right < 0:
            self.rect.x = WIDTH 

    def update(self):
        self.move_background()

class Hud():
    def __init__(self):
        self.spaceship = pygame.image.load(os.path.join("assets", "images", "spaceship.png")).convert_alpha()
        self.spaceship_rect = self.spaceship.get_rect()
        self.spaceship_rect.topleft = (25, 25)
        self.info_font = pygame.font.Font(os.path.join("assets", "fonts", "LuckiestGuy-Regular.ttf"), 32)
        self.heart_frame_one = pygame.image.load(os.path.join("assets", "images", "hearts", "frame-1.png")).convert_alpha()
        self.heart_frame_two = pygame.image.load(os.path.join("assets", "images", "hearts", "frame-2.png")).convert_alpha()
        self.heart_frame_three = pygame.image.load(os.path.join("assets", "images", "hearts", "frame-3.png")).convert_alpha()
        self.heart_frame_four = pygame.image.load(os.path.join("assets", "images", "hearts", "frame-4.png")).convert_alpha()
        self.heart_frame_five = pygame.image.load(os.path.join("assets", "images", "hearts", "frame-5.png")).convert_alpha()
        self.heart_frame_six = pygame.image.load(os.path.join("assets", "images", "hearts", "frame-6.png")).convert_alpha()
        self.heart_frame_seven = pygame.image.load(os.path.join("assets", "images", "hearts", "frame-7.png")).convert_alpha()
        self.heart_frame_eight = pygame.image.load(os.path.join("assets", "images", "hearts", "frame-8.png")).convert_alpha()
        self.heart_frames = [self.heart_frame_one, self.heart_frame_two, self.heart_frame_three, self.heart_frame_four, self.heart_frame_five, self.heart_frame_six, self.heart_frame_seven, self.heart_frame_eight]
        self.heart_rect = self.heart_frame_one.get_rect()
        self.heart_rect.bottomleft = (25, 575)
        self.current_frame = 0
        self.frame_delay = 200
        self.last_frame_time = 0

    def animate_heart(self):
        global current_frame
        if current_time - self.last_frame_time >= self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.heart_frames)
            self.last_frame_time = current_time  
    
    def update_score(self):
        global score
        score += 1

    def update_lives(self):
        global lives
        lives -= 1

    def draw_hud(self):
        self.animate_heart()
        global score, lives
        lives_text = self.info_font.render(f"{lives}", True, WHITE)
        score_text = self.info_font.render(f"{score}", True, WHITE)
        screen.blit(self.spaceship, self.spaceship_rect)
        screen.blit(score_text, (80, 40))
        screen.blit(self.heart_frames[self.current_frame], self.heart_rect)
        screen.blit(lives_text, (80, 540))

class title_screen():
    def __init__(self):
        self.title_font = pygame.font.Font(os.path.join("assets", "fonts", "LuckiestGuy-Regular.ttf"), 72)
        self.inst_font = pygame.font.Font(os.path.join("assets", "fonts", "LuckiestGuy-Regular.ttf"), 32)
        self.title_text = "SPACE ATTACK!"
        self.inst_text = "Press ENTER to blast off"
        self.title_text = self.title_font.render(self.title_text, True, WHITE)
        self.title_text_rect = self.title_text.get_rect()
        self.title_text_rect.center = (WIDTH // 2, 120)
        self.inst_text = self.inst_font.render(self.inst_text, True, WHITE)
        self.inst_text_rect = self.inst_text.get_rect()
        self.inst_text_rect.center = ((WIDTH // 2), 480)
        self.title_image = pygame.image.load(os.path.join("assets", "images", "spaceship_pl.png")).convert_alpha()
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.center = (WIDTH // 2, HEIGHT // 2)

    def draw_title_screen(self):
        static_background.draw_static()
        screen.blit(self.title_text, self.title_text_rect)
        screen.blit(self.title_image, self.title_image_rect)
        screen.blit(self.inst_text, self.inst_text_rect)

class Sounds():
    def __init__(self):
        self.boom = pygame.mixer.Sound(os.path.join("assets", "sounds", "boom.mp3"))
        self.boom.set_volume(0.2)
        self.shoot = pygame.mixer.Sound(os.path.join("assets", "sounds", "shoot.mp3"))
        self.shoot.set_volume(0.2)
        self.music = pygame.mixer.music.load(os.path.join("assets", "sounds", "xeon6.ogg"))
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

    def play_boom(self):
        self.boom.play()
    
    def play_shoot(self):
        self.shoot.play()


# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60

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
background = pygame.sprite.Group()
background.add(Background(0))
background.add(Background(WIDTH))   
static_background = Background(0)

# Player
player_sprite = pygame.sprite.GroupSingle()
player_sprite.add(Player())

# Bullets
bullet_sprites = pygame.sprite.Group()
bullet_cooldown = 800
last_bullet_time = 0

# Hud
hud = Hud()
lives = 3
score = 0

# Enemies
ennemy_sprires = pygame.sprite.Group()
spawn_enemy = 3000
last_enemy_time = 0

# Title Screen
title_screen = title_screen()

# Sounds
sounds = Sounds()


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
                
        # Create bullets
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and current_time - last_bullet_time >= bullet_cooldown:
                bullet_sprites.add(Bullet(player_sprite.sprite.rect.center))
                last_bullet_time = current_time
                sounds.play_shoot()

        # Create enemies
        if current_time - last_enemy_time >= spawn_enemy:
            ennemy_sprires.add(Enemy(random.randint(1, 5)))
            last_enemy_time = current_time

        # # Collision detection
        if pygame.sprite.spritecollide(player_sprite.sprite, ennemy_sprires, True):
            lives -= 1
            sounds.play_boom
        if pygame.sprite.groupcollide(bullet_sprites, ennemy_sprires, True, True):
            score += 1
            sounds.play_boom()

        # Check for Game Over
        if lives < 1:
            game_over = True
        
        # Level up
        if score > 5:
            spawn_enemy = 2500
        if score > 10:
            spawn_enemy = 2000
        if score > 15:
            spawn_enemy = 1500
        if score > 20:
            spawn_enemy = 1000
        
        # Draw surfaces 
        background.draw(screen) 
        hud.draw_hud()
        background.update() 
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
            spawn_enemy = 3000
            lives = 3
            score = 0
        title_screen.draw_title_screen()

    # Update dispay
    pygame.display.update()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()