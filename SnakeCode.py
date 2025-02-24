import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game 🐍")

# Snake and Food Initialization
snake = [(100, 100), (80, 100), (60, 100)]
direction = (GRID_SIZE, 0)
food = (random.randint(0, (WIDTH//GRID_SIZE) - 1) * GRID_SIZE, random.randint(0, (HEIGHT//GRID_SIZE) - 1) * GRID_SIZE)

# Fonts and Clock
font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()
score = 0

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

def draw_food():
    pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))

def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def move_snake():
    global food, score
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    
    if new_head == food:
        snake.insert(0, new_head)
        food = (random.randint(0, (WIDTH//GRID_SIZE) - 1) * GRID_SIZE, random.randint(0, (HEIGHT//GRID_SIZE) - 1) * GRID_SIZE)
        score += 1
    else:
        snake.insert(0, new_head)
        snake.pop()

def check_collision():
    if (snake[0][0] < 0 or snake[0][0] >= WIDTH or snake[0][1] < 0 or snake[0][1] >= HEIGHT or snake[0] in snake[1:]):
        return True
    return False

def main():
    global direction
    running = True
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                    direction = (0, -GRID_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                    direction = (0, GRID_SIZE)
                elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                    direction = (-GRID_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                    direction = (GRID_SIZE, 0)
        
        move_snake()
        if check_collision():
            break
        
        draw_snake()
        draw_food()
        draw_score()
        pygame.display.flip()
        clock.tick(10)
    
    pygame.quit()

if __name__ == "__main__":
    main()
