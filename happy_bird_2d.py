import pygame
import math
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 235)
GREEN = (34, 139, 34)
YELLOW = (255, 255, 0)
RED = (255, 69, 0)
ORANGE = (255, 165, 0)
PURPLE = (138, 43, 226)
PINK = (255, 192, 203)

class Bird:
    def __init__(self):
        self.x = 100
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.gravity = 0.8
        self.jump_strength = -12
        self.size = 25
        self.angle = 0
        self.wing_animation = 0
        self.trail = []
        
    def jump(self):
        self.velocity = self.jump_strength
        
    def update(self):
        # Physics
        self.velocity += self.gravity
        self.y += self.velocity
        
        # Rotation based on velocity
        self.angle = max(-45, min(45, self.velocity * 3))
        
        # Wing animation
        self.wing_animation += 0.3
        
        # Trail effect
        self.trail.append((self.x, self.y))
        if len(self.trail) > 8:
            self.trail.pop(0)
        
        # Keep bird on screen
        if self.y < 0:
            self.y = 0
            self.velocity = 0
        elif self.y > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT
            
    def draw(self, screen):
        # Draw trail
        for i, (tx, ty) in enumerate(self.trail):
            alpha = i / len(self.trail)
            trail_size = int(self.size * alpha * 0.5)
            if trail_size > 0:
                trail_color = (int(255 * alpha), int(200 * alpha), int(100 * alpha))
                self.draw_circle_3d(screen, trail_color, tx, ty, trail_size, alpha * 0.5)
        
        # Draw bird body (3D effect)
        self.draw_bird_3d(screen)
        
    def draw_circle_3d(self, screen, color, x, y, radius, depth=1.0):
        # Create 3D effect with multiple circles
        for i in range(int(radius * depth), 0, -2):
            shade = max(0, min(255, int(color[0] * i / radius)))
            shade_color = (shade, int(color[1] * i / radius), int(color[2] * i / radius))
            pygame.draw.circle(screen, shade_color, (int(x), int(y - i * 0.3)), i)
            
    def draw_bird_3d(self, screen):
        # Main body
        body_colors = [YELLOW, ORANGE, RED]
        for i, color in enumerate(body_colors):
            offset = i * 3
            pygame.draw.circle(screen, color, 
                             (int(self.x - offset), int(self.y - offset)), 
                             self.size - offset)
        
        # Wings (animated)
        wing_offset = math.sin(self.wing_animation) * 5
        wing_color = (255, 140, 0)
        
        # Left wing
        wing_points = [
            (self.x - 15, self.y - 5 + wing_offset),
            (self.x - 25, self.y - 15 + wing_offset),
            (self.x - 20, self.y + 5 + wing_offset)
        ]
        pygame.draw.polygon(screen, wing_color, wing_points)
        
        # Right wing
        wing_points = [
            (self.x + 5, self.y - 5 - wing_offset),
            (self.x + 15, self.y - 15 - wing_offset),
            (self.x + 10, self.y + 5 - wing_offset)
        ]
        pygame.draw.polygon(screen, wing_color, wing_points)
        
        # Eye
        pygame.draw.circle(screen, WHITE, (int(self.x + 8), int(self.y - 5)), 8)
        pygame.draw.circle(screen, BLACK, (int(self.x + 10), int(self.y - 3)), 4)
        
        # Beak
        beak_points = [
            (self.x + 20, self.y),
            (self.x + 35, self.y - 3),
            (self.x + 30, self.y + 8)
        ]
        pygame.draw.polygon(screen, ORANGE, beak_points)

class Pipe:
    def __init__(self, x):
        self.x = x
        self.gap_size = 200
        self.gap_y = random.randint(150, SCREEN_HEIGHT - 150 - self.gap_size)
        self.width = 80
        self.speed = 4
        self.passed = False
        
    def update(self):
        self.x -= self.speed
        
    def draw(self, screen):
        # Draw 3D pipes with gradient effect
        pipe_color = GREEN
        
        # Top pipe
        self.draw_pipe_3d(screen, self.x, 0, self.width, self.gap_y, pipe_color)
        
        # Bottom pipe
        bottom_height = SCREEN_HEIGHT - (self.gap_y + self.gap_size)
        self.draw_pipe_3d(screen, self.x, self.gap_y + self.gap_size, 
                         self.width, bottom_height, pipe_color)
        
    def draw_pipe_3d(self, screen, x, y, width, height, base_color):
        # Create 3D effect with multiple rectangles
        for i in range(10):
            shade = max(50, 255 - i * 15)
            pipe_color = (0, shade, 0)
            offset = i * 2
            pygame.draw.rect(screen, pipe_color, 
                           (x - offset, y - offset, width + offset, height + offset))
        
        # Pipe cap (3D effect)
        cap_height = 30
        if y == 0:  # Top pipe
            cap_y = height - cap_height
        else:  # Bottom pipe
            cap_y = y - cap_height
            
        for i in range(5):
            shade = max(100, 255 - i * 20)
            cap_color = (0, shade, 0)
            offset = i * 3
            pygame.draw.rect(screen, cap_color, 
                           (x - 10 - offset, cap_y - offset, 
                            width + 20 + offset, cap_height + offset))
    
    def collides_with(self, bird):
        # Check collision with bird
        bird_rect = pygame.Rect(bird.x - bird.size, bird.y - bird.size, 
                               bird.size * 2, bird.size * 2)
        
        top_pipe = pygame.Rect(self.x, 0, self.width, self.gap_y)
        bottom_pipe = pygame.Rect(self.x, self.gap_y + self.gap_size, 
                                 self.width, SCREEN_HEIGHT - self.gap_y - self.gap_size)
        
        return bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe)
    
    def is_off_screen(self):
        return self.x + self.width < 0

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-5, -1)
        self.life = 30
        self.max_life = 30
        self.color = random.choice([YELLOW, ORANGE, RED, PINK, PURPLE])
        
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.2  # Gravity
        self.life -= 1
        
    def draw(self, screen):
        if self.life > 0:
            alpha = self.life / self.max_life
            size = int(5 * alpha)
            if size > 0:
                color = tuple(int(c * alpha) for c in self.color)
                pygame.draw.circle(screen, color, (int(self.x), int(self.y)), size)
    
    def is_alive(self):
        return self.life > 0

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("3D Happy Bird Game")
        self.clock = pygame.time.Clock()
        
        self.bird = Bird()
        self.pipes = []
        self.particles = []
        self.score = 0
        self.game_over = False
        self.font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 32)
        
        # Background elements
        self.clouds = []
        for _ in range(5):
            self.clouds.append({
                'x': random.randint(0, SCREEN_WIDTH),
                'y': random.randint(50, 200),
                'size': random.randint(30, 60),
                'speed': random.uniform(0.5, 1.5)
            })
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.game_over:
                        self.bird.jump()
                        # Add particles when jumping
                        for _ in range(5):
                            self.particles.append(Particle(self.bird.x, self.bird.y))
                    else:
                        self.restart_game()
                elif event.key == pygame.K_ESCAPE:
                    return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not self.game_over:
                    self.bird.jump()
                    # Add particles when jumping
                    for _ in range(5):
                        self.particles.append(Particle(self.bird.x, self.bird.y))
                else:
                    self.restart_game()
        return True
    
    def update(self):
        if not self.game_over:
            self.bird.update()
            
            # Update clouds
            for cloud in self.clouds:
                cloud['x'] -= cloud['speed']
                if cloud['x'] < -100:
                    cloud['x'] = SCREEN_WIDTH + 50
            
            # Spawn pipes
            if len(self.pipes) == 0 or self.pipes[-1].x < SCREEN_WIDTH - 300:
                self.pipes.append(Pipe(SCREEN_WIDTH))
            
            # Update pipes
            for pipe in self.pipes[:]:
                pipe.update()
                
                # Check for collision
                if pipe.collides_with(self.bird):
                    self.game_over = True
                    # Explosion particles
                    for _ in range(20):
                        self.particles.append(Particle(self.bird.x, self.bird.y))
                
                # Check for scoring
                if not pipe.passed and pipe.x + pipe.width < self.bird.x:
                    pipe.passed = True
                    self.score += 1
                    # Score particles
                    for _ in range(10):
                        self.particles.append(Particle(self.bird.x + 30, self.bird.y - 30))
                
                # Remove off-screen pipes
                if pipe.is_off_screen():
                    self.pipes.remove(pipe)
            
            # Check ground collision
            if self.bird.y >= SCREEN_HEIGHT - 50:
                self.game_over = True
                # Ground collision particles
                for _ in range(15):
                    self.particles.append(Particle(self.bird.x, self.bird.y))
        
        # Update particles
        for particle in self.particles[:]:
            particle.update()
            if not particle.is_alive():
                self.particles.remove(particle)
    
    def draw_background(self):
        # Gradient sky
        for y in range(SCREEN_HEIGHT):
            ratio = y / SCREEN_HEIGHT
            r = int(135 + (255 - 135) * ratio)
            g = int(206 + (255 - 206) * ratio)
            b = int(235 + (200 - 235) * ratio)
            pygame.draw.line(self.screen, (r, g, b), (0, y), (SCREEN_WIDTH, y))
        
        # Draw clouds
        for cloud in self.clouds:
            for i in range(3):
                offset = i * 5
                cloud_color = (255 - offset, 255 - offset, 255 - offset)
                pygame.draw.circle(self.screen, cloud_color,
                                 (int(cloud['x'] + offset), int(cloud['y'] + offset)),
                                 cloud['size'] - offset)
        
        # Ground
        ground_color = (34, 139, 34)
        pygame.draw.rect(self.screen, ground_color, 
                        (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50))
        
        # Ground details (3D effect)
        for i in range(0, SCREEN_WIDTH, 20):
            grass_height = random.randint(5, 15)
            grass_color = (random.randint(20, 60), random.randint(120, 160), random.randint(20, 60))
            pygame.draw.rect(self.screen, grass_color,
                           (i, SCREEN_HEIGHT - 50 - grass_height, 15, grass_height))
    
    def draw(self):
        self.draw_background()
        
        # Draw pipes
        for pipe in self.pipes:
            pipe.draw(self.screen)
        
        # Draw bird
        if not self.game_over:
            self.bird.draw(self.screen)
        
        # Draw particles
        for particle in self.particles:
            particle.draw(self.screen)
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        score_shadow = self.font.render(f"Score: {self.score}", True, BLACK)
        self.screen.blit(score_shadow, (22, 22))
        self.screen.blit(score_text, (20, 20))
        
        # Draw game over screen
        if self.game_over:
            # Semi-transparent overlay
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))
            
            # Game over text
            game_over_text = self.font.render("GAME OVER", True, RED)
            final_score_text = self.small_font.render(f"Final Score: {self.score}", True, WHITE)
            restart_text = self.small_font.render("Press SPACE or Click to Restart", True, WHITE)
            quit_text = self.small_font.render("Press ESC to Quit", True, WHITE)
            
            # Center the text
            go_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
            fs_rect = final_score_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            r_rect = restart_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 40))
            q_rect = quit_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 80))
            
            self.screen.blit(game_over_text, go_rect)
            self.screen.blit(final_score_text, fs_rect)
            self.screen.blit(restart_text, r_rect)
            self.screen.blit(quit_text, q_rect)
        
        # Draw instructions at start
        elif self.score == 0 and len(self.pipes) == 0:
            instruction_text = self.small_font.render("Press SPACE or Click to Flap!", True, WHITE)
            inst_shadow = self.small_font.render("Press SPACE or Click to Flap!", True, BLACK)
            inst_rect = instruction_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 100))
            shadow_rect = inst_shadow.get_rect(center=(SCREEN_WIDTH//2 + 2, SCREEN_HEIGHT//2 + 102))
            
            self.screen.blit(inst_shadow, shadow_rect)
            self.screen.blit(instruction_text, inst_rect)
    
    def restart_game(self):
        self.bird = Bird()
        self.pipes = []
        self.particles = []
        self.score = 0
        self.game_over = False
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()