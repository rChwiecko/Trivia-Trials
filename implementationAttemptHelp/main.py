import pygame
import sys
import Button
import constants

pygame.init()

run = True
while run:
    constants.screen.fill('black')
    constants.timer.tick(constants.FPS)

    draw_heading()

    if main_menu:
        menu_command = draw_menu()
        if menu_command != -1:
            main_menu = False
            if menu_command == 5:  # Exit Menu button pressed
                exit_menu = True
    elif exit_menu:
        draw_exit_screen()
    else:
        if menu_command == 2:
            save_command = draw_save_screen()
            if save_command != 0:
                print(f'Save {save_command}')
                main_menu = True
        elif menu_command == 3:  # Highscore button pressed
            draw_highscore_screen()
            if draw_back_button():
                main_menu = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        elif menu_command == 1:  # Start button pressed
            constants.screen.fill('black')
            # Display role selection screen
            dev_button = Button('Developer', (constants.WIDTH // 2 - 100, constants.HEIGHT // 2 - 50), width=200)
            dev_button.draw()
            instructor_button = Button('Instructor', (constants.WIDTH // 2 - 100, constants.HEIGHT // 2 + 20), width=200)
            instructor_button.draw()
            player_button = Button('Player', (constants.WIDTH // 2 - 100, constants.HEIGHT // 2 + 90), width=200)
            player_button.draw()

            menu_btn = Button('Main Menu', ((constants.WIDTH - 200) // 2, constants.HEIGHT - 150))
            menu_btn.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if dev_button.check_clicked():
                        # Perform actions for developer
                        pass
                    elif instructor_button.check_clicked():
                        # Perform actions for instructor
                        pass
                    elif player_button.check_clicked():
                        # Perform actions for player
                        pass
                    elif menu_btn.check_clicked():
                        main_menu = True

        else:
            main_menu = draw_game()
            if menu_command > 0:
                text = constants.font.render(f'Button {menu_command} pressed!', True, 'black')
                constants.screen.blit(text, (150, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if main_menu:  # Only show exit menu in the main menu screen
                    exit_menu = True

    pygame.display.flip()

pygame.quit()