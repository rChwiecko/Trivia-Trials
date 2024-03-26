import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display surface
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rectangle Example")

# Define rectangle properties
rect_width = 100
rect_height = 50
rect_color = (255, 0, 0)  # Red color
x = (width - rect_width) // 2
y = (height - rect_height) // 2

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((255, 255, 255))  # Fill with white

    # Draw the rectangle
    pygame.draw.rect(screen, rect_color, (x, y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()
