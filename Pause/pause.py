# Author: Sonia Sharma
# Date: Tuesday March 26th, 2024
# Class/File: pause.py
# Description: This file contains the pause menu of the application, when user chooses to pausethe game in the middle of a game session

import pygame  # Import the pygame module
import sys  # Import the sys module

pygame.init()  # Initialize the pygame module

WIDTH, HEIGHT = 800, 600  # Set the width and height of the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the game window with the specified dimensions
pygame.display.set_caption("Pause Game")  # Set the caption/title of the game window

duck_image = pygame.image.load("duck.png")  # Load the image of the duck from file
duck_image = pygame.transform.scale(duck_image, (100, 100))  # Scale the duck image to the desired size
duck_rect = duck_image.get_rect()  # Get the rectangular area that bounds the duck image

WHITE = (255, 255, 255)  # Define the color white
BLACK = (0, 0, 0)  # Define the color black

font = pygame.font.SysFont(None, 25)  # Set the font and size for text rendering

def draw_text(text, font, color, surface, x, y):  # Define a function to draw text on the screen
    text_obj = font.render(text, True, color)  # Render the text
    text_rect = text_obj.get_rect()  # Get the rectangular area that bounds the text
    text_rect.topleft = (x, y)  # Set the position of the text
    surface.blit(text_obj, text_rect)  # Blit (draw) the text onto the surface

def draw_button(text, x, y):  # Define a function to draw a button on the screen
    pygame.draw.rect(screen, BLACK, (x, y, 200, 50))  # Draw the button rectangle
    if y == 250:  # Adjust text position based on button position
        draw_text(text, font, WHITE, screen, x + 70, y + 20)
    elif y == 350: 
        draw_text(text, font, WHITE, screen, x + 40, y + 20)
    else: 
        draw_text(text, font, WHITE, screen, x + 20, y + 22)

running = True  # Set a flag to control the main game loop
paused = False
dataSaved = False

while running:  # Main game loop
    screen.fill(WHITE)  # Fill the screen with white color
    for event in pygame.event.get():  # Check for events (e.g., key presses, mouse clicks)
        if event.type == pygame.QUIT:  # If the user tries to close the window
            running = False  # Set the running flag to False, exiting the loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 350 <= mouse_pos[0] <= 450 and 250 <= mouse_pos[1] <= 300:  # Check if mouse click is on "Resume" button
                paused = not paused
            elif 350 <= mouse_pos[1] <= 400:  # Check if mouse click is on "Save and Quit" button
                dataSaved = True
            elif 450 <= mouse_pos[1] <= 500:  # Check if mouse click is on "Don't Save and Quit" button
                running = False

    screen.blit(duck_image, (WIDTH // 2 - duck_rect.width // 2, 100))  # Draw the duck image on the screen

    title_font = pygame.font.SysFont(None, 40)  # Set the font and size for the title text
    draw_text("Pause Game", title_font, BLACK, screen, 320, 50)  # Draw the title text on the screen
    draw_button("Resume", 300, 250)  # Draw the "Resume" button
    draw_button("Save and Quit", 300, 350)  # Draw the "Save and Quit" button
    draw_button("Don't Save and Quit", 300, 450)  # Draw the "Don't Save and Quit" button

    if paused: 
        draw_text("Resume Session", font, BLACK, screen, WIDTH // 4, HEIGHT // 4)  # Draw "Resume Session" text if paused
    else:
        if dataSaved:
            draw_text("Data Saved", font, BLACK, screen, WIDTH // 4, HEIGHT // 4)  # Draw "Data Saved" text if data saved

    pygame.display.flip()  # Update the display

pygame.quit()  # Quit pygame
sys.exit()  # Exit the program
