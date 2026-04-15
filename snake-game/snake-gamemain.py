import pygame
import random

# Initialize
pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("Arial", 25)

# Snake
snake = [(100, 100)]
direction = (BLOCK, 0)

# Food
food = (random.randrange(0, WIDTH, BLOCK), random.randrange(0, HEIGHT, BLOCK))

score = 0
speed = 10

running = True
while running:
    screen.fill(BLACK)
    
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = (0, -BLOCK)
            elif event.key == pygame.K_DOWN:
                direction = (0, BLOCK)
            elif event.key == pygame.K_LEFT:
                direction = (-BLOCK, 0)
            elif event.key == pygame.K_RIGHT:
                direction = (BLOCK, 0)
            elif event.key == pygame.K_r:
                snake = [(100, 100)]
                direction = (BLOCK, 0)
                score = 0
                speed = 10
    
    # Move snake
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, head)
    
    # Eat food
    if head == food:
        score += 1
        food = (random.randrange(0, WIDTH, BLOCK), random.randrange(0, HEIGHT, BLOCK))
        speed += 0.5  # Increase difficulty
    else:
        snake.pop()
    
    # Collision
    if (head in snake[1:] or
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT):
        running = False
    
    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK, BLOCK))
    
    # Draw food
    pygame.draw.rect(screen, RED, (*food, BLOCK, BLOCK))
    
    # Score
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))
    
    pygame.display.update()
    clock.tick(speed)

pygame.quit()
