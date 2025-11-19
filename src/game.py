import pygame
import random
import math

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 150, 255)
GREEN = (50, 200, 50)
BROWN = (139, 90, 43)
ORANGE = (255, 140, 0)
YELLOW = (255, 215, 0)
GRAY = (128, 128, 128)
RED = (255, 50, 50)

# Game setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cat's Fish Quest")
clock = pygame.time.Clock()

# Helper functions to draw sprites
def draw_cat(surface, x, y, size=30):
    # Body
    pygame.draw.ellipse(surface, ORANGE, (x, y + size // 2, size * 1.3, size * 0.9))
    # Head
    head_x = x + size * 0.65
    head_y = y + size * 0.3
    pygame.draw.circle(surface, ORANGE, (int(head_x), int(head_y)), int(size * 0.45))
    # Ears - pointy triangles
    ear1 = [(head_x - size * 0.25, head_y - size * 0.1), 
            (head_x - size * 0.35, head_y - size * 0.5), 
            (head_x - size * 0.05, head_y - size * 0.25)]
    pygame.draw.polygon(surface, ORANGE, ear1)
    ear2 = [(head_x + size * 0.25, head_y - size * 0.1), 
            (head_x + size * 0.35, head_y - size * 0.5), 
            (head_x + size * 0.05, head_y - size * 0.25)]
    pygame.draw.polygon(surface, ORANGE, ear2)
    # Inner ears
    pygame.draw.polygon(surface, (255, 180, 100), 
                       [(head_x - size * 0.25, head_y - size * 0.1),
                        (head_x - size * 0.3, head_y - size * 0.4),
                        (head_x - size * 0.15, head_y - size * 0.2)], 0)
    pygame.draw.polygon(surface, (255, 180, 100),
                       [(head_x + size * 0.25, head_y - size * 0.1),
                        (head_x + size * 0.3, head_y - size * 0.4),
                        (head_x + size * 0.15, head_y - size * 0.2)], 0)
    # Eyes - cat-like slits
    pygame.draw.ellipse(surface, (100, 200, 100), (head_x - size * 0.2, head_y - size * 0.05, size * 0.15, size * 0.2))
    pygame.draw.ellipse(surface, (100, 200, 100), (head_x + size * 0.05, head_y - size * 0.05, size * 0.15, size * 0.2))
    pygame.draw.ellipse(surface, BLACK, (head_x - size * 0.15, head_y, size * 0.05, size * 0.15))
    pygame.draw.ellipse(surface, BLACK, (head_x + size * 0.1, head_y, size * 0.05, size * 0.15))
    # Nose
    nose_points = [(head_x, head_y + size * 0.1), 
                   (head_x - size * 0.05, head_y + size * 0.15),
                   (head_x + size * 0.05, head_y + size * 0.15)]
    pygame.draw.polygon(surface, (255, 150, 150), nose_points)
    # Whiskers
    pygame.draw.line(surface, BLACK, (int(head_x - size * 0.1), int(head_y + size * 0.12)), 
                    (int(head_x - size * 0.5), int(head_y + size * 0.1)), 1)
    pygame.draw.line(surface, BLACK, (int(head_x - size * 0.1), int(head_y + size * 0.15)), 
                    (int(head_x - size * 0.5), int(head_y + size * 0.2)), 1)
    pygame.draw.line(surface, BLACK, (int(head_x + size * 0.1), int(head_y + size * 0.12)), 
                    (int(head_x + size * 0.5), int(head_y + size * 0.1)), 1)
    pygame.draw.line(surface, BLACK, (int(head_x + size * 0.1), int(head_y + size * 0.15)), 
                    (int(head_x + size * 0.5), int(head_y + size * 0.2)), 1)
    # Tail
    tail_start_x = x
    tail_start_y = y + size
    pygame.draw.arc(surface, ORANGE, (tail_start_x - size * 0.8, tail_start_y - size * 0.5, size * 0.8, size * 0.8), 
                   0, 3.14, 3)
    # Paws
    pygame.draw.circle(surface, ORANGE, (int(x + size * 0.3), int(y + size * 1.3)), int(size * 0.15))
    pygame.draw.circle(surface, ORANGE, (int(x + size * 0.7), int(y + size * 1.3)), int(size * 0.15))

def draw_crow(surface, x, y, size=25):
    # Body
    pygame.draw.ellipse(surface, BLACK, (x, y, size, size))
    # Head
    pygame.draw.circle(surface, BLACK, (int(x + size * 0.7), int(y + size // 3)), size // 3)
    # Wing
    pygame.draw.ellipse(surface, GRAY, (x - size // 4, y + size // 4, size // 2, size // 2))
    # Beak
    points = [(x + size * 0.85, y + size // 3), (x + size + 5, y + size // 3), (x + size * 0.85, y + size // 2)]
    pygame.draw.polygon(surface, YELLOW, points)

def draw_cheese(surface, x, y, size=15):
    # Cheese wedge
    points = [(x, y + size), (x + size, y + size), (x + size // 2, y)]
    pygame.draw.polygon(surface, YELLOW, points)
    pygame.draw.polygon(surface, ORANGE, points, 2)
    # Holes
    pygame.draw.circle(surface, ORANGE, (int(x + size // 2), int(y + size * 0.6)), 2)
    pygame.draw.circle(surface, ORANGE, (int(x + size * 0.3), int(y + size * 0.7)), 2)

def draw_fish(surface, x, y, size=20):
    # Body
    pygame.draw.ellipse(surface, BLUE, (x, y + size // 4, size, size // 2))
    # Tail
    points = [(x, y + size // 2), (x - size // 3, y), (x - size // 3, y + size)]
    pygame.draw.polygon(surface, BLUE, points)
    # Eye
    pygame.draw.circle(surface, BLACK, (int(x + size * 0.7), int(y + size // 2)), 2)

def draw_door(surface, x, y, width, height, locked=True):
    color = RED if locked else GREEN
    pygame.draw.rect(surface, BROWN, (x, y, width, height))
    pygame.draw.rect(surface, color, (x + 5, y + 5, width - 10, height - 10), 3)
    # Door knob
    pygame.draw.circle(surface, color, (int(x + width - 15), int(y + height // 2)), 5)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 40
        self.vel_y = 0
        self.vel_x = 0
        self.speed = 5
        self.jump_power = 12
        self.on_ground = False
        self.gravity = 0.5
        self.lives = 3
        self.invincible = False
        self.invincible_timer = 0
        self.invincible_duration = 120
        
    def move(self, keys, platforms):
        # Update invincibility
        if self.invincible:
            self.invincible_timer -= 1
            if self.invincible_timer <= 0:
                self.invincible = False
        
        self.vel_x = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel_x = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel_x = self.speed
            
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
            self.vel_y = -self.jump_power
            self.on_ground = False
        
        self.vel_y += self.gravity
        if self.vel_y > 15:
            self.vel_y = 15
            
        self.x += self.vel_x
        self.check_collision_x(platforms)
        
        self.y += self.vel_y
        self.on_ground = False
        self.check_collision_y(platforms)
        
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH - self.width:
            self.x = WIDTH - self.width
    
    def take_damage(self):
        if not self.invincible:
            self.lives -= 1
            self.invincible = True
            self.invincible_timer = self.invincible_duration
            return True
        return False
    
    def check_collision_x(self, platforms):
        for plat in platforms:
            if (self.x < plat.x + plat.width and 
                self.x + self.width > plat.x and
                self.y < plat.y + plat.height and
                self.y + self.height > plat.y):
                if self.vel_x > 0:
                    self.x = plat.x - self.width
                elif self.vel_x < 0:
                    self.x = plat.x + plat.width
                    
    def check_collision_y(self, platforms):
        for plat in platforms:
            if (self.x < plat.x + plat.width and 
                self.x + self.width > plat.x and
                self.y < plat.y + plat.height and
                self.y + self.height > plat.y):
                if self.vel_y > 0:
                    self.y = plat.y - self.height
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.y = plat.y + plat.height
                    self.vel_y = 0
    
    def draw(self):
        # Flicker when invincible
        if not self.invincible or (self.invincible_timer % 10 < 5):
            draw_cat(screen, self.x, self.y, 30)

class Platform:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (30, 150, 30), (self.x, self.y, self.width, self.height), 2)

class Crow:
    def __init__(self, x, y, speed, shoot_delay):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 1
        self.start_x = x
        self.range = 150
        self.shoot_timer = 0
        self.shoot_delay = shoot_delay
        
    def update(self):
        self.x += self.speed * self.direction
        if self.x > self.start_x + self.range or self.x < self.start_x - self.range:
            self.direction *= -1
            
        self.shoot_timer += 1
        
    def draw(self):
        draw_crow(screen, self.x, self.y, 25)

class Cheese:
    def __init__(self, x, y, target_x, target_y):
        self.x = x
        self.y = y
        # Only move vertically downward
        self.vel_x = 0
        self.vel_y = 3.5  # Slower speed
        self.size = 15
        
    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        
    def draw(self):
        draw_cheese(screen, int(self.x), int(self.y), self.size)
        
    def off_screen(self):
        return self.y > HEIGHT or self.x < 0 or self.x > WIDTH

class Fish:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.collected = False
        
    def draw(self):
        if not self.collected:
            draw_fish(screen, self.x, self.y, 20)

class Door:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 70
        
    def draw(self, locked):
        draw_door(screen, self.x, self.y, self.width, self.height, locked)

def create_level(level_num):
    platforms = []
    crows = []
    fishes = []
    
    if level_num == 1:
        platforms = [
            Platform(0, 550, 800, 50),  # Ground
            Platform(100, 450, 150, 20),
            Platform(300, 350, 150, 20),
            Platform(500, 450, 150, 20),
        ]
        crows = [
            Crow(250, 300, 2, 90),
            Crow(450, 250, 1.5, 100),
        ]
        fishes = [
            Fish(120, 420),
            Fish(320, 320),
            Fish(520, 420),
        ]
        door = Door(700, 480)
        player_start = (50, 500)
        
    elif level_num == 2:
        platforms = [
            Platform(0, 550, 800, 50),
            Platform(50, 450, 120, 20),
            Platform(220, 380, 120, 20),
            Platform(400, 320, 120, 20),
            Platform(580, 380, 120, 20),
            Platform(350, 200, 100, 20),
        ]
        crows = [
            Crow(150, 350, 2, 80),
            Crow(450, 250, 2, 85),
            Crow(600, 300, 1.5, 90),
        ]
        fishes = [
            Fish(70, 420),
            Fish(420, 290),
            Fish(600, 350),
        ]
        door = Door(700, 480)
        player_start = (50, 500)
        
    elif level_num == 3:
        platforms = [
            Platform(0, 550, 800, 50),
            Platform(100, 470, 100, 20),
            Platform(250, 400, 100, 20),
            Platform(400, 330, 100, 20),
            Platform(550, 260, 100, 20),
            Platform(200, 250, 100, 20),
            Platform(450, 180, 100, 20),
        ]
        crows = [
            Crow(150, 380, 2.5, 75),
            Crow(350, 280, 2, 80),
            Crow(500, 200, 2.5, 70),
            Crow(250, 180, 2, 85),
        ]
        fishes = [
            Fish(120, 440),
            Fish(420, 300),
            Fish(570, 230),
        ]
        door = Door(700, 480)
        player_start = (50, 500)
        
    else:  # Level 4 - Hardest
        platforms = [
            Platform(0, 550, 800, 50),
            Platform(80, 480, 80, 20),
            Platform(200, 430, 80, 20),
            Platform(320, 380, 80, 20),
            Platform(440, 330, 80, 20),
            Platform(560, 280, 80, 20),
            Platform(680, 380, 100, 20),
            Platform(150, 320, 80, 20),
            Platform(300, 250, 80, 20),
            Platform(450, 200, 80, 20),
            Platform(200, 150, 80, 20),
        ]
        crows = [
            Crow(120, 400, 3, 65),
            Crow(280, 330, 2.5, 70),
            Crow(400, 280, 3, 68),
            Crow(520, 220, 2.5, 72),
            Crow(250, 180, 2.5, 75),
            Crow(600, 200, 3, 65),
        ]
        fishes = [
            Fish(100, 450),
            Fish(340, 350),
            Fish(470, 170),
        ]
        door = Door(710, 310)
        player_start = (50, 500)
    
    return platforms, crows, fishes, door, player_start

def main():
    current_level = 1
    max_level = 4
    
    platforms, crows, fishes, door, player_start = create_level(current_level)
    player = Player(player_start[0], player_start[1])
    cheeses = []
    fish_collected = 0
    
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)
    large_font = pygame.font.Font(None, 48)
    
    running = True
    game_over = False
    win = False
    game_complete = False
    
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_over:
                    platforms, crows, fishes, door, player_start = create_level(current_level)
                    player = Player(player_start[0], player_start[1])
                    cheeses = []
                    fish_collected = 0
                    game_over = False
                    win = False
                if event.key == pygame.K_n and win and not game_complete:
                    if current_level < max_level:
                        current_level += 1
                        platforms, crows, fishes, door, player_start = create_level(current_level)
                        player = Player(player_start[0], player_start[1])
                        cheeses = []
                        fish_collected = 0
                        game_over = False
                        win = False
                    else:
                        game_complete = True
                if event.key == pygame.K_SPACE and game_complete:
                    # Restart from beginning
                    current_level = 1
                    platforms, crows, fishes, door, player_start = create_level(current_level)
                    player = Player(player_start[0], player_start[1])
                    cheeses = []
                    fish_collected = 0
                    game_over = False
                    win = False
                    game_complete = False
        
        if not game_over and not win:
            keys = pygame.key.get_pressed()
            player.move(keys, platforms)
            
            # Update crows and shooting
            for crow in crows:
                crow.update()
                if crow.shoot_timer >= crow.shoot_delay:
                    cheeses.append(Cheese(crow.x + 12, crow.y + 12, player.x + 15, player.y + 18))
                    crow.shoot_timer = 0
            
            # Update cheeses
            for cheese in cheeses[:]:
                cheese.update()
                if cheese.off_screen():
                    cheeses.remove(cheese)
                elif (player.x < cheese.x + cheese.size and
                      player.x + player.width > cheese.x and
                      player.y < cheese.y + cheese.size and
                      player.y + player.height > cheese.y):
                    if player.take_damage():
                        cheeses.remove(cheese)
                        if player.lives <= 0:
                            game_over = True
            
            # Check fish collection
            for fish in fishes:
                if not fish.collected:
                    if (player.x < fish.x + fish.width and
                        player.x + player.width > fish.x and
                        player.y < fish.y + fish.height and
                        player.y + player.height > fish.y):
                        fish.collected = True
                        fish_collected += 1
            
            # Check door
            door_unlocked = fish_collected >= 3
            if door_unlocked:
                if (player.x < door.x + door.width and
                    player.x + player.width > door.x and
                    player.y < door.y + door.height and
                    player.y + player.height > door.y):
                    win = True
            
            # Check if player fell
            if player.y > HEIGHT:
                game_over = True
        
        # Draw everything
        screen.fill((135, 206, 235))  # Sky blue
        
        for platform in platforms:
            platform.draw()
        
        for crow in crows:
            crow.draw()
        
        for cheese in cheeses:
            cheese.draw()
        
        for fish in fishes:
            fish.draw()
        
        door.draw(fish_collected < 3)
        player.draw()
        
        # UI
        level_text = small_font.render(f"Level {current_level}", True, BLACK)
        screen.blit(level_text, (10, 10))
        
        fish_text = small_font.render(f"Fish: {fish_collected}/3", True, BLACK)
        screen.blit(fish_text, (10, 40))
        
        # Draw lives
        lives_text = small_font.render(f"Lives:", True, BLACK)
        screen.blit(lives_text, (10, 70))
        for i in range(player.lives):
            pygame.draw.circle(screen, RED, (80 + i * 25, 80), 8)
        
        if player.invincible and not game_over:
            invincible_text = small_font.render("INVINCIBLE!", True, YELLOW)
            screen.blit(invincible_text, (WIDTH // 2 - 50, 10))
        
        if game_over:
            text = font.render("GAME OVER! Press R to Retry", True, RED)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
        
        if win and not game_complete:
            if current_level < max_level:
                text = font.render("LEVEL COMPLETE!", True, GREEN)
                screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 30))
                text2 = small_font.render("Press N for Next Level", True, BLACK)
                screen.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 2 + 10))
        
        if game_complete:
            # Victory screen
            screen.fill((50, 20, 80))  # Dark purple background
            
            # Stars animation
            for i in range(20):
                star_x = (WIDTH // 4) + (i * 30) % (WIDTH // 2)
                star_y = 50 + ((i * 47) % 150)
                pygame.draw.circle(screen, YELLOW, (star_x, star_y), 3)
            
            # Title
            title = large_font.render("CONGRATULATIONS!", True, YELLOW)
            screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
            
            # Sub text
            text1 = font.render("You completed all 4 levels!", True, WHITE)
            screen.blit(text1, (WIDTH // 2 - text1.get_width() // 2, HEIGHT // 2 - 20))
            
            text2 = font.render("The cat found all the fish!", True, (100, 200, 255))
            screen.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 2 + 30))
            
            # Draw big cat
            draw_cat(screen, WIDTH // 2 - 40, HEIGHT // 2 + 80, 60)
            
            # Restart instruction
            restart_text = small_font.render("Press SPACE to play again from Level 1", True, GREEN)
            screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT - 80))
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
