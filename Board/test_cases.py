import pygame
import sys
import main_menu  # Import the main_menu module containing game logic

# Initialize Pygame
pygame.init()

# Set screen dimensions
WIDTH = 1280
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Set fonts
font_heading = pygame.font.Font('freesansbold.ttf', 36)
font = pygame.font.Font('freesansbold.ttf', 24)

# Load images
bg = pygame.Surface((WIDTH, HEIGHT))  # Background image
ball = pygame.Surface((150, 150))  # Placeholder for game screen

# Initialize variables
main_menu.main_menu = False
main_menu.exit_menu = False
main_menu.menu_command = 0

# Button class definition
Button = main_menu.Button


# Function to simulate button clicks
def simulate_click(button, mouse_pos):
    if button.check_clicked(mouse_pos):
        main_menu.handle_button_click(button)


# Test Case 1: Clicking Main Menu Buttons
def test_main_menu():
    # Simulate clicking each button in the main menu
    buttons = main_menu.menu_buttons
    for button in buttons:
        simulate_click(button, (50, 50))  # Example mouse position


# Test Case 2: Exiting the Game
def test_exit_game():
    # Simulate clicking the "Exit Menu" button
    simulate_click(main_menu.exit_button, (50, 50))  # Example mouse position

    # Simulate clicking "Yes" on the exit confirmation screen
    simulate_click(main_menu.yes_button, (150, 150))  # Example mouse position


# Test Case 3: Not Saving Before Exiting
def test_no_save_exit():
    # Simulate clicking the "Exit Menu" button
    simulate_click(main_menu.exit_button, (50, 50))  # Example mouse position

    # Simulate clicking "No" on the exit confirmation screen
    simulate_click(main_menu.no_button, (250, 150))  # Example mouse position


# Test Case 4: Saving the Game
def test_save_game():
    # Simulate clicking each save button
    save_buttons = main_menu.save_buttons
    for save_button in save_buttons:
        simulate_click(save_button, (50, 50))  # Example mouse position


# Main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
