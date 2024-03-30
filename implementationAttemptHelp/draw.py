import pygame
import constants
import Button

def draw_heading():
    heading_text = constants.font_heading.render("Trivia Trials", True, 'white')
    constants.screen.blit(heading_text, ((constants.WIDTH - heading_text.get_width()) // 2, 50))
    # Blit logo onto the screen above all buttons
    constants.screen.blit(constants.logo, ((constants.WIDTH - constants.logo.get_width()) // 2, 100))  # Adjust position as needed

def draw_menu():
    command = -1
    menu_width = 300
    menu_height = 400
    menu_x = (constants.WIDTH - menu_width) // 2
    menu_y = (constants.HEIGHT - menu_height) // 2
    pygame.draw.rect(constants.screen, 'black', [menu_x, menu_y, menu_width, menu_height])

    tutorials_button = Button('Tutorials', (menu_x + 20, menu_y + 20))
    tutorials_button.draw()

    button1 = Button('Start', (menu_x + 20, menu_y + 80))  # Adjusted position
    button1.draw()
    button2 = Button('Load Previous', (menu_x + 20, menu_y + 140))  # Adjusted position
    button2.draw()
    button3 = Button('Highscore', (menu_x + 20, menu_y + 200))  # Adjusted position
    button3.draw()

    exit_button = Button('Exit Menu', (menu_x + 20, menu_y + 260))  # Adjusted position
    exit_button.draw()

    if tutorials_button.check_clicked():
        command = 4
    if exit_button.check_clicked():
        command = 5
    if button1.check_clicked():
        command = 1
    if button2.check_clicked():
        command = 2
    if button3.check_clicked():
        command = 3

    return command


def draw_game():
    menu_btn = Button('Main Menu', ((constants.WIDTH - 200) // 2, constants.HEIGHT - 150))
    menu_btn.draw()
    menu = menu_btn.check_clicked()

    constants.screen.blit(constants.ball, ((constants.WIDTH - 150) // 2, (constants.HEIGHT - 150) // 2))

    return menu


def draw_save_screen():
    save_menu_width = 300
    save_menu_height = 400
    save_menu_x = (constants.WIDTH - save_menu_width) // 2
    save_menu_y = (constants.HEIGHT - save_menu_height) // 2
    pygame.draw.rect(constants.screen, 'black', [save_menu_x, save_menu_y, save_menu_width, save_menu_height])
    pygame.draw.rect(constants.screen, 'green', [save_menu_x, save_menu_y, save_menu_width, save_menu_height], 5)

    button_width = 260
    button_height = 40
    button_margin = 20
    button_start_y = save_menu_y + 50

    save1_btn = Button('Save 1', (save_menu_x + (save_menu_width - button_width) // 2, button_start_y),
                       width=button_width, height=button_height)
    save1_btn.draw()

    save2_btn = Button('Save 2', (
        save_menu_x + (save_menu_width - button_width) // 2, button_start_y + button_height + button_margin),
                       width=button_width, height=button_height)
    save2_btn.draw()

    save3_btn = Button('Save 3', (
        save_menu_x + (save_menu_width - button_width) // 2, button_start_y + 2 * (button_height + button_margin)),
                       width=button_width, height=button_height)
    save3_btn.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            constants.sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if save1_btn.check_clicked():
                return 1
            elif save2_btn.check_clicked():
                return 2
            elif save3_btn.check_clicked():
                return 3

    return 0


def draw_highscore_screen():
    highscore_menu_width = 400
    highscore_menu_height = 400
    highscore_menu_x = (constants.WIDTH - highscore_menu_width) // 2
    highscore_menu_y = (constants.HEIGHT - highscore_menu_height) // 2
    pygame.draw.rect(constants.screen, 'black', [highscore_menu_x, highscore_menu_y, highscore_menu_width, highscore_menu_height])
    pygame.draw.rect(constants.screen, 'green', [highscore_menu_x, highscore_menu_y, highscore_menu_width, highscore_menu_height],
                     5)

    # Display high scores
    high_scores = constants.get_player_scores() # Get high scores from the database

    y_offset = highscore_menu_y + 50
    for player, score in high_scores.items():
        text_surface = constants.font.render(f'{player}: {score}', True, 'white')
        constants.screen.blit(text_surface, (highscore_menu_x + 50, y_offset))
        y_offset += 40


def draw_back_button():
    back_button = Button('Back', (20, 20), width=100, height=40)
    back_button.draw()
    if back_button.check_clicked():
        return True
    return False


def draw_exit_screen():
    exit_menu_width = 400
    exit_menu_height = 200
    exit_menu_x = (constants.WIDTH - exit_menu_width) // 2
    exit_menu_y = (constants.HEIGHT - exit_menu_height) // 2
    pygame.draw.rect(constants.screen, 'black', [exit_menu_x, exit_menu_y, exit_menu_width, exit_menu_height])
    # pygame.draw.rect(screen, 'green', [exit_menu_x, exit_menu_y, exit_menu_width, exit_menu_height], 3)

    exit_text = constants.font.render("Do you want to save before exiting?", True, 'white')
    constants.screen.blit(exit_text, (exit_menu_x + 20, exit_menu_y + 20))

    yes_button = Button('Yes', (exit_menu_x + 50, exit_menu_y + 80), width=100, height=40)
    no_button = Button('No', (exit_menu_x + 250, exit_menu_y + 80), width=100, height=40)
    yes_button.draw()
    no_button.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            constants.sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if yes_button.check_clicked():
                # Add code here to save the game before exiting
                pygame.quit()
                constants.sys.exit()
            elif no_button.check_clicked():
                pygame.quit()
                constants.sys.exit()
