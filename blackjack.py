import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Point Game")

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Point settings
point_radius = 10
point_speed = 5

# Initial position of the red point
point_x = random.randint(point_radius, WIDTH - point_radius)
point_y = random.randint(point_radius, HEIGHT - point_radius)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the red point randomly
    point_x += random.choice([-point_speed, 0, point_speed])
    point_y += random.choice([-point_speed, 0, point_speed])

    # Keep the point within the screen bounds
    point_x = max(point_radius, min(point_x, WIDTH - point_radius))
    point_y = max(point_radius, min(point_y, HEIGHT - point_radius))

    # Clear the screen
    screen.fill(WHITE)

    # Draw the red point
    pygame.draw.circle(screen, RED, (point_x, point_y), point_radius)

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.delay(100)

# Quit Pygame
pygame.quit()
