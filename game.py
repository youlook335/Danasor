import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 600
FPS = 60
CAR_SPEED = 2
OBSTACLE_SPEED = 5
OBSTACLE_WIDTH = 20
OBSTACLE_HEIGHT = 100
LANE_WIDTH = 200
WHITE = (0, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Load Car Image
CAR_IMAGE = pygame.image.load("car.png")  # Make sure to have a car image in the same directory
CAR_IMAGE = pygame.transform.scale(CAR_IMAGE, (50, 100))

# Car Class
class Car:
    def __init__(self):
        self.x = WIDTH // 2 - 25
        self.y = HEIGHT - 120
        self.image = CAR_IMAGE

    def move_left(self):
        if self.x > WIDTH // 2 - LANE_WIDTH:
            self.x -= LANE_WIDTH

    def move_right(self):
        if self.x < WIDTH // 2 + LANE_WIDTH - 50:
            self.x += LANE_WIDTH

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Obstacle Class
class Obstacle:
    def __init__(self):
        self.x = random.choice([WIDTH // 2 - LANE_WIDTH, WIDTH // 2, WIDTH // 2 + LANE_WIDTH - 50])
        self.y = -OBSTACLE_HEIGHT
        self.image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.image.fill(RED)

    def update(self):
        self.y += OBSTACLE_SPEED

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Main Game Function
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    car = Car()
    obstacles = []
    score = 0
    font = pygame.font.Font(None, 36)
    running = True
    
    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car.move_left()
                if event.key == pygame.K_RIGHT:
                    car.move_right()
                if event.key == pygame.K_r:
                    main()  # Restart game
        
        if random.randint(1, 100) > 98:
            obstacles.append(Obstacle())
        
        for obstacle in obstacles[:]:
            obstacle.update()
            if obstacle.y > HEIGHT:
                obstacles.remove(obstacle)
                score += 1
            
            if car.x < obstacle.x + OBSTACLE_WIDTH and car.x + 50 > obstacle.x and car.y < obstacle.y + OBSTACLE_HEIGHT and car.y + 100 > obstacle.y:
                running = False  # Collision detected
        
        car.draw(screen)
        for obstacle in obstacles:
            obstacle.draw(screen)
        
        # Score Display
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
