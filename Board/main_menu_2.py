'''This module generates the main menu, connects with database and provides savedata for the board to use to initialize games.

Authors: Arjun Atwal, Ryan Chwiecko, Jin Zhao, Sahej Chawla, Comments by Jin Zhao
'''

import pygame
import sys
from queryManager import *
from main import *
from const import *

# constants
WIDTH = 1280
HEIGHT = 800
FPS = 60
state = ''
timer = pygame.time.Clock()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Trivia Trials')
main_menu = False
exit_menu = False
show_too_many_user_error = False
show_no_user_error = False
show_empty_name = False
show_existing_user = False
entering_user_data = False
username_enter = ''
password_enter = ''
player_list = []
username_enter_active = False
password_enter_active = False
font_heading = pygame.font.Font('freesansbold.ttf', 36)
font = pygame.font.Font('freesansbold.ttf', 24)
other_font = pygame.font.get_default_font()
game_data = None
new_game = None
# Load image
bg = pygame.transform.scale(pygame.image.load('assets/transparentduck.png'), (100, 100))
ball = pygame.transform.scale(pygame.image.load('assets/transparentduck.png'), (150, 150))
tutorial1 = pygame.transform.scale(pygame.image.load('./tutorialScreens/tutorial1.png'), (600, 400))
tutorial2 = pygame.transform.scale(pygame.image.load('./tutorialScreens/tutorial2.png'), (600, 400))
tutorial3 = pygame.transform.scale(pygame.image.load('./tutorialScreens/tutorial3.png'), (600, 400))
tutorial4 = pygame.transform.scale(pygame.image.load('./tutorialScreens/tutorial4.png'), (600, 400))
tutorial5 = pygame.transform.scale(pygame.image.load('./tutorialScreens/tutorial5.png'), (600, 400))
tutorial_duck = pygame.transform.scale(pygame.image.load('assets/transparentduck.png'), (400, 400))
menu_command = 0

# Load logo image
logo = pygame.image.load('assets/transparentduck.png')  # Replace 'logo.png' with the path to your logo image
logo = pygame.transform.scale(logo, (100, 100))  # Scale the logo to an appropriate size


class Button:
    '''A class to represent a button.
    
    Attributes:
        text (str): Text to be displayed in button.
        pos (int): x, y-coordinate of the button on the screen.
        width (int): The width of the button
        height (int): The height of the button.
        button (pygame.Rect): The rectangle representing the button.
    '''

    def __init__(self, txt, pos, width=260, height=40):
        self.text = txt
        self.pos = pos
        self.width = width
        self.height = height
        self.button = pygame.Rect(self.pos, (self.width, self.height))

    def draw(self):
        '''Generate blank screen.'''
        pygame.draw.rect(screen, 'light gray', self.button, 0, 5)
        pygame.draw.rect(screen, 'dark gray', self.button, 5, 5)
        text2 = font.render(self.text, True, 'black')
        text_rect = text2.get_rect(center=self.button.center)
        screen.blit(text2, text_rect.topleft)

    def check_clicked(self):
        '''Checks if a user's mouse input was made.
        
        Returns:
            boolean: Whether button is clicked (True) or not (False)
        '''
        return self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]


def draw_heading():
    '''Generate personal info as text for a screen header.
    
    Returns:
        none'''
    drawText("Ryan Chwiecko, Jin Zhao, Arjun Atwal, Sonia Sharma, Sahej Chawla", other_font, 15, WHITE, 10, 10)
    drawText("Team number 69", other_font, 15, WHITE, 10, 25)
    drawText("Term: Winter 2024", other_font, 15, WHITE, 10, 40)
    drawText("This was created as a project under The University of Western Ontario", other_font, 15, WHITE, 10, 55)
    heading_text = font_heading.render("Trivia Trials", True, 'white')
    screen.blit(heading_text, ((WIDTH - heading_text.get_width()) // 2, 50))
    # Blit logo onto the screen above all buttons
    screen.blit(logo, ((WIDTH - logo.get_width()) // 2, 100))  # Adjust position as needed


def draw_menu() -> int:
    '''Generates game initial main menu screen.
    
    Returns:
        int: The command input representing a screen chosen through mouse click by user.
    '''
    command = -1
    menu_width = 300
    menu_height = 400
    menu_x = (WIDTH - menu_width) // 2
    menu_y = (HEIGHT - menu_height) // 2
    pygame.draw.rect(screen, 'black', [menu_x, menu_y, menu_width, menu_height])

    tutorials_button = Button('Tutorials', (menu_x + 20, menu_y + 20))
    tutorials_button.draw()

    button1 = Button('Start', (menu_x + 20, menu_y + 80))  # Adjusted position
    button1.draw()
    button2 = Button('Load Save', (menu_x + 20, menu_y + 140))  # Adjusted position
    button2.draw()
    button3 = Button('Highscore', (menu_x + 20, menu_y + 200))  # Adjusted position
    button3.draw()
    loginbutton = Button('Developer Login', (menu_x + 20, menu_y + 260))  # Adjusted position
    loginbutton.draw()

    exit_button = Button('Exit Game', (menu_x + 20, menu_y + 380))  # Adjusted position
    exit_button.draw()

    if tutorials_button.check_clicked():
        command = 6
    if exit_button.check_clicked():
        command = 5
    if button1.check_clicked():
        command = 1
    if button2.check_clicked():
        command = 2
    if button3.check_clicked():
        command = 3
    if loginbutton.check_clicked():
        draw_password_screen()

    return command

def draw_password_screen():
    '''Generates screen prompting user to enter password.

    args:
        None
    
    Returns:
        int: The command input representing a screen chosen through mouse click by user.
    '''
    password = ''
    password_rect = pygame.Rect(100, 100, 140, 32)
    password_active = False
    password_color = 'white'
    password_font = pygame.font.Font(None, 32)
    password_text = password_font.render(password, True, password_color)
    password_text_rect = password_text.get_rect()
    password_text_rect.center = password_rect.center
    password_rect.w = max(200, password_text_rect.width + 10)
    
    username = ''
    username_rect = pygame.Rect(100, 150, 140, 32)
    username_active = False
    username_color = 'white'
    username_font = pygame.font.Font(None, 32)
    username_text = username_font.render(username, True, username_color)
    username_text_rect = username_text.get_rect()
    username_text_rect.center = username_rect.center
    username_rect.w = max(200, username_text_rect.width + 10)
    
    submit_button = Button('Submit', (100, 200), width=100, height=40)
    
    active = False
    while True:
        screen.fill('black')
        screen.blit(password_text, password_text_rect)
        pygame.draw.rect(screen, 'lightgrey' if password_active else 'white', password_rect, 2)  
        screen.blit(username_text, username_text_rect)
        pygame.draw.rect(screen, 'lightgrey' if username_active else 'white', username_rect, 2)  
        submit_button.draw()

        password_label = font.render("Password:", True, 'white')
        screen.blit(password_label, (password_rect.x + password_rect.width + 10, password_rect.y))
        
        username_label = font.render("Username:", True, 'white')
        screen.blit(username_label, (username_rect.x + username_rect.width + 10, username_rect.y))

        if draw_back_button():
            return 0
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # if window closed, quit game
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:    # check if mouse button is clicked
                if password_rect.collidepoint(event.pos):
                    password_active = not password_active
                else:
                    password_active = False
                password_color = 'white' if password_active else 'black'
                
                if username_rect.collidepoint(event.pos):
                    username_active = not username_active
                else:
                    username_active = False
                username_color = 'white' if username_active else 'black'
                if submit_button.check_clicked():       # check if submit button is clicked
                    if password == '1234':
                        running = True
                        while running:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    running = False
                                    pygame.quit()
                                    sys.exit()
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    if draw_back_button():
                                        return 0
                                after_login_screen()
                            pygame.display.flip()
                        return password, username
                    
            if event.type == pygame.KEYDOWN:
                if password_active:
                    if event.key == pygame.K_RETURN:
                        if password == '1234':
                            after_login_screen()
                    elif event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode
                    password_text = password_font.render(password, True, password_color)
                    password_text_rect = password_text.get_rect()
                    password_text_rect.center = password_rect.center
                    password_rect.w = max(200, password_text_rect.width + 10)
                    
                if username_active:
                    if event.key == pygame.K_RETURN:
                        if password == '1234':
                            after_login_screen()
                        return password, username
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                    username_text = username_font.render(username, True, username_color)
                    username_text_rect = username_text.get_rect()
                    username_text_rect.center = username_rect.center
                    username_rect.w = max(200, username_text_rect.width + 10)
        pygame.display.flip()

def after_login_screen():
    '''Generate screen displaying options for the user upon successful login.
    
    Returns:
        int: The command input representing a screen chosen through mouse click by user.'''
    screen.fill('black')
    # make 2 buttons, one for drawing the player details and one for generate game data
    draw_player_details_button = Button('Player Details', (100, 100), width=200, height=40)
    draw_player_details_button.draw()
    generate_game_data_button = Button('Generate Game Data', (100, 150), width=300, height=40)
    generate_game_data_button.draw()
    draw_change_highscores_button = Button('Change Highscores', (100, 200), width=300, height=40)
    draw_change_highscores_button.draw()
    global state
    if draw_back_button():
        state = ''
        return 0
    if draw_player_details_button.check_clicked():
        draw_player_details()
        state = "draw_details"
    if state == "draw_details":
        draw_player_details()
    if generate_game_data_button.check_clicked():
        state = ''
        generate_game_data()
    if draw_change_highscores_button.check_clicked():   # check if developer user wants to change highscores
        state = ''
        change_highscores()

def show_tutorial(tutorial_state):
    '''Generates screens for the game tutorial.
    
    Args:
        tutorial_state (int): Tutorial state representing each tutorial screen, indicated by an integer 0, 1, 2, 3, 4, 5.
    '''
    if tutorial_state == 0:
        screen.blit(tutorial1, (340, 100))
        drawText("When you begin the game and select to start a new game, you will be directed to a screen that will allow you to", other_font, 20, WHITE, 100, 510)
        drawText("enter user information, when you are done entering your information, select 'Add Players' to add another player,", other_font, 20, WHITE, 100, 530)
        drawText("or 'Start Game' to start the game.", other_font, 20, WHITE, 100, 550)
    elif tutorial_state == 1:
        screen.blit(tutorial2, (340, 100))
        drawText("When you begin the game, you will be shown a countdown that states whos turn it is. Whoevers name that is shown,", other_font, 20, WHITE, 100, 510)
        drawText("it is now their turn to answer the question that will be displayed when the countdown is over.", other_font, 20, WHITE, 100, 530)
    elif tutorial_state == 2:
        screen.blit(tutorial3, (340, 100))
        drawText("When the question is displayed, the current player can type their answer into the question box and press the return", other_font, 20, WHITE, 100, 510)
        drawText("key on the keyboard to submit the answer before the progress bar runs out. Or the player can use a duck by clicking", other_font, 20, WHITE, 100, 530)
        drawText("on the duck in the top right to skip the question. Details on how that mechanic works is in the next slide.", other_font, 20, WHITE, 100, 550)
    elif tutorial_state == 3:
        screen.blit(tutorial_duck, (440, 100))
        drawText("When you go through the board, whichever has the most points out of all the players present in the game, is rewarded", other_font, 20, WHITE, 100, 510)
        drawText("with a duck. What this does is grant the user the opportunity to skip a question of their choice, while being", other_font, 20, WHITE, 100, 530)
        drawText("given full points for the question despite them not having to answer it, this adds on to streaks aswell.", other_font, 20, WHITE, 100, 550)        
    elif tutorial_state == 4:
        screen.blit(tutorial4, (340, 100))
        drawText("When you answer a question and submit the answer, you are shown feedback on your answer. Including your answer", other_font, 20, WHITE, 100, 510)
        drawText("and the actual answer to the question", other_font, 20, WHITE, 100, 530)
    elif tutorial_state == 5:
        screen.blit(tutorial5, (340, 100))
        drawText("When all players are given a chance to answer, a screen displaying all the users scores after question is shown", other_font, 20, WHITE, 100, 510)
        drawText("and diplays the streaks that the users are on to the right of the flame icon. It also shows which player is ", other_font, 20, WHITE, 100, 530)
        drawText("going to be rewarded with a duck at the end of every level", other_font, 20, WHITE, 100, 550)     

def change_highscores():
    '''Generates screen to change highscores.

    args:
        None
    
    Returns:
        int: The command input representing a screen chosen through mouse click by user.
    '''

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if draw_back_button():
                    return 0

        # highscore menu dimensions and position
        highscore_menu_width = 400
        highscore_menu_height = 400
        highscore_menu_x = (WIDTH - highscore_menu_width) // 2
        highscore_menu_y = (HEIGHT - highscore_menu_height) // 2
        pygame.draw.rect(screen, 'black', [highscore_menu_x, highscore_menu_y, highscore_menu_width, highscore_menu_height])
        pygame.draw.rect(screen, 'green', [highscore_menu_x, highscore_menu_y, highscore_menu_width, highscore_menu_height], 5)

        # Display high scores
        high_scores = get_player_scores() # Get high scores from the database
        
        y_offset = highscore_menu_y + 50
        for player, score in high_scores.items():
            text_surface = font.render(f'{player}: {score}', True, 'white')
            screen.blit(text_surface, (highscore_menu_x + 50, y_offset))
            y_offset += 40
        
        # Add buttons to change high scores
        change_highscore_button = Button('Change Highscores', (highscore_menu_x + 50, highscore_menu_y + 300))
        change_highscore_button.draw()

        if change_highscore_button.check_clicked():
            # change the high scores
            # make 2 text boxes to the right of the high scores, one for player and one for score
            player = ''
            player_rect = pygame.Rect(100, 100, 140, 32)
            player_active = False
            player_color = 'white'
            player_font = pygame.font.Font(None, 32)
            player_text = player_font.render(player, True, player_color)
            player_text_rect = player_text.get_rect()
            player_text_rect.center = player_rect.center
            player_rect.w = max(200, player_text_rect.width + 10)

            score = ''
            score_rect = pygame.Rect(100, 150, 140, 32)
            score_active = False
            score_color = 'white'
            score_font = pygame.font.Font(None, 32)
            score_text = score_font.render(score, True, score_color)
            score_text_rect = score_text.get_rect()
            score_text_rect.center = score_rect.center
            score_rect.w = max(200, score_text_rect.width + 10)

            submit_button = Button('Submit', (100, 200), width=100, height=40)

            active = False
            while True:
                screen.fill('black')
                screen.blit(player_text, player_text_rect)
                pygame.draw.rect(screen, 'lightgrey' if player_active else 'white', player_rect, 2)  
                screen.blit(score_text, score_text_rect)
                pygame.draw.rect(screen, 'lightgrey' if score_active else 'white', score_rect, 2)  
                submit_button.draw()

                player_label = font.render("Player:", True, 'white')
                screen.blit(player_label, (player_rect.x + player_rect.width + 10, player_rect.y))
                
                score_label = font.render("Score:", True, 'white')
                screen.blit(score_label, (score_rect.x + score_rect.width + 10, score_rect.y))

                if draw_back_button():
                    return 0
                
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if player_rect.collidepoint(event.pos):
                            player_active = not player_active
                        else:
                            player_active = False
                        player_color = 'white' if player_active else 'black'
                        
                        if score_rect.collidepoint(event.pos):
                            score_active = not score_active
                        else:
                            score_active = False
                        score_color = 'white' if score_active else 'black'
                        if submit_button.check_clicked():
                            # change the high score
                            update_player_score(player, score)
                            running = False
                            return 0
                    if event.type == pygame.KEYDOWN:
                        if player_active:
                            if event.key == pygame.K_RETURN:
                                update_player_score(player, score)
                                running = False
                                return 0
                            elif event.key == pygame.K_BACKSPACE:
                                player = player[:-1]
                            else:
                                player += event.unicode
                            player_text = player_font.render(player, True, player_color)
                            player_text_rect = player_text.get_rect()
                            player_text_rect.center = player_rect.center
                            player_rect.w = max(200, player_text_rect.width + 10)
                            
                        if score_active:
                            if event.key == pygame.K_RETURN:
                                update_player_score(player, score)
                                running = False
                                return 0
                            elif event.key == pygame.K_BACKSPACE:
                                score = score[:-1]
                            else:
                                score += event.unicode
                            score_text = score_font.render(score, True, score_color)
                            score_text_rect = score_text.get_rect()
                            score_text_rect.center = score_rect.center
                            score_rect.w = max(200, score_text_rect.width + 10)
                            

        pygame.display.flip()

def draw_player_details():
    '''Generates text to display player details.
    
    Returns:
        int: The command input representing a screen chosen through mouse click by user.'''
    # use get_player_info() to get the player info, then display it on the screen
    player_info = get_player_info()
    y_offset = 500
    if draw_back_button():
        return 0
    for player, info in player_info.items():
        info_str = ', '.join(f'{k}: {v}' for k, v in info.items())
        text_surface = font.render(f'{player} has {info_str}', True, 'white')
        screen.blit(text_surface, (50, y_offset))
        y_offset += 40

def generate_game_data():
    '''Generates data on a saved game and displays it for developer to manipulate.
    
    Returns:
        int: The command input representing a screen chosen through mouse click by user.'''

    # variables to visualize each player's level
    level = ''
    level_rect = pygame.Rect(100, 100, 140, 32)
    level_active = False
    level_color = 'white'
    level_font = pygame.font.Font(None, 32)
    level_text = level_font.render(level, True, level_color)
    level_text_rect = level_text.get_rect()
    level_text_rect.center = level_rect.center
    level_rect.w = max(200, level_text_rect.width + 10)
    
    # visualizing player's position on the board
    index = ''
    index_rect = pygame.Rect(100, 150, 140, 32)
    index_active = False
    index_color = 'white'
    index_font = pygame.font.Font(None, 32)
    index_text = index_font.render(index, True, index_color)
    index_text_rect = index_text.get_rect()
    index_text_rect.center = index_rect.center
    index_rect.w = max(200, index_text_rect.width + 10)

    # visualizing player's current correct answer streak
    streak = ''
    streak_rect = pygame.Rect(100, 200, 140, 32)
    streak_active = False
    streak_color = 'white'
    streak_font = pygame.font.Font(None, 32)
    streak_text = streak_font.render(streak, True, streak_color)
    streak_text_rect = streak_text.get_rect()
    streak_text_rect.center = streak_rect.center
    streak_rect.w = max(200, streak_text_rect.width + 10)

    # visualizing number of ducks in player's posession
    duck_count = ''
    duck_count_rect = pygame.Rect(100, 250, 140, 32)
    duck_count_active = False
    duck_count_color = 'white'
    duck_count_font = pygame.font.Font(None, 32)
    duck_count_text = duck_count_font.render(duck_count, True, duck_count_color)
    duck_count_text_rect = duck_count_text.get_rect()
    duck_count_text_rect.center = duck_count_rect.center
    duck_count_rect.w = max(200, duck_count_text_rect.width + 10)
    
    # visualizing player's score
    score = ''
    score_rect = pygame.Rect(100, 300, 140, 32)
    score_active = False
    score_color = 'white'
    score_font = pygame.font.Font(None, 32)
    score_text = score_font.render(score, True, score_color)
    score_text_rect = score_text.get_rect()
    score_text_rect.center = score_rect.center
    score_rect.w = max(200, score_text_rect.width + 10)

    # button to confirm changes
    submit_button = Button('Submit', (100, 350), width=100, height=40)

    active = False
    while True:
        screen.fill('black')
        screen.blit(level_text, level_text_rect)
        pygame.draw.rect(screen, 'lightgrey' if level_active else 'white', level_rect, 2)  
        screen.blit(index_text, index_text_rect)
        pygame.draw.rect(screen, 'lightgrey' if index_active else 'white', index_rect, 2)  
        submit_button.draw()
        screen.blit(streak_text, streak_text_rect)
        pygame.draw.rect(screen, 'lightgrey' if streak_active else 'white', streak_rect, 2)
        screen.blit(duck_count_text, duck_count_text_rect)
        pygame.draw.rect(screen, 'lightgrey' if duck_count_active else 'white', duck_count_rect, 2)
        screen.blit(score_text, score_text_rect)
        pygame.draw.rect(screen, 'lightgrey' if score_active else 'white', score_rect, 2)

        level_label = level_font.render("Level:", True, 'white')
        screen.blit(level_label, (level_rect.x + level_rect.width + 10, level_rect.y))
        
        index_label = index_font.render("Index:", True, 'white')
        screen.blit(index_label, (index_rect.x + index_rect.width + 10, index_rect.y))
        
        streak_label = streak_font.render("Streak:", True, 'white')
        screen.blit(streak_label, (streak_rect.x + streak_rect.width + 10, streak_rect.y))
        
        duck_count_label = duck_count_font.render("Duck Count:", True, 'white')
        screen.blit(duck_count_label, (duck_count_rect.x + duck_count_rect.width + 10, duck_count_rect.y))
        
        score_label = score_font.render("Score:", True, 'white')
        screen.blit(score_label, (score_rect.x + score_rect.width + 10, score_rect.y))

        if draw_back_button():
            return 0
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if level_rect.collidepoint(event.pos):
                    level_active = not level_active
                else:
                    level_active = False
                level_color = 'white' if level_active else 'black'
                
                if index_rect.collidepoint(event.pos):
                    index_active = not index_active
                else:
                    index_active = False
                index_color = 'white' if index_active else 'black'
                
                if streak_rect.collidepoint(event.pos):
                    streak_active = not streak_active
                else:
                    streak_active = False
                streak_color = 'white' if streak_active else 'black'
                
                if duck_count_rect.collidepoint(event.pos):
                    duck_count_active = not duck_count_active
                else:
                    duck_count_active = False
                duck_count_color = 'white' if duck_count_active else 'black'
                
                if score_rect.collidepoint(event.pos):
                    score_active = not score_active
                else:
                    score_active = False
                score_color = 'white' if score_active else 'black'
                
                if submit_button.check_clicked():   # if saving game, change turn it into a game data object and save in database
                    sending_level = int(level)
                    sending_index = int(index)
                    sending_streak = int(streak)
                    sending_duck_count = int(duck_count)
                    sending_score = int(score)

                    game_data = {
                        "game_id": 4,
                        "level_number": sending_level,
                        "player_index": sending_index,
                        "players": [
                            {
                            "name": "God",
                            "password": "iamgod",
                            "streak": sending_streak,
                            "duck_count": sending_duck_count,
                            "score": sending_score
                            }
                        ]
                    }
                    game(new_game=False, game_data=game_data)
                    menu_command = 0
                
                    
            if event.type == pygame.KEYDOWN:
                if level_active:
                    if event.key == pygame.K_RETURN:

                        print(level, index, streak, duck_count, score)
                        return level, index, streak, duck_count, score
                    elif event.key == pygame.K_BACKSPACE:
                        level = level[:-1]
                    else:
                        level += event.unicode
                    level_text = level_font.render(level, True, level_color)
                    level_text_rect = level_text.get_rect()
                    level_text_rect.center = level_rect.center
                    level_rect.w = max(200, level_text_rect.width + 10)
                    
                if index_active:
                    if event.key == pygame.K_RETURN:

                        print(level, index, streak, duck_count, score)
                        return level, index, streak, duck_count, score
                    elif event.key == pygame.K_BACKSPACE:
                        index = index[:-1]
                    else:
                        index += event.unicode
                    index_text = index_font.render(index, True, index_color)
                    index_text_rect = index_text.get_rect()
                    index_text_rect.center = index_rect.center
                    index_rect.w = max(200, index_text_rect.width + 10)

                if streak_active:
                    if event.key == pygame.K_RETURN:

                        print(level, index, streak, duck_count, score)
                        return level, index, streak, duck_count, score
                    elif event.key == pygame.K_BACKSPACE:
                        streak = streak[:-1]
                    else:
                        streak += event.unicode
                    streak_text = streak_font.render(streak, True, streak_color)
                    streak_text_rect = streak_text.get_rect()
                    streak_text_rect.center = streak_rect.center
                    streak_rect.w = max(200, streak_text_rect.width + 10)

                if duck_count_active:
                    if event.key == pygame.K_RETURN:
                        print(level, index, streak, duck_count, score)
                        return level, index, streak, duck_count, score
                    elif event.key == pygame.K_BACKSPACE:
                        duck_count = duck_count[:-1]
                    else:
                        duck_count += event.unicode
                    duck_count_text = duck_count_font.render(duck_count, True, duck_count_color)
                    duck_count_text_rect = duck_count_text.get_rect()
                    duck_count_text_rect.center = duck_count_rect.center
                    duck_count_rect.w = max(200, duck_count_text_rect.width + 10)

                if score_active:
                    if event.key == pygame.K_RETURN:
                        print(level, index, streak, duck_count, score)
                        return level, index, streak, duck_count, score
                    elif event.key == pygame.K_BACKSPACE:
                        score = score[:-1]
                    else:
                        score += event.unicode
                    score_text = score_font.render(score, True, score_color)
                    score_text_rect = score_text.get_rect()
                    score_text_rect.center = score_rect.center
                    score_rect.w = max(200, score_text_rect.width + 10)
        pygame.display.flip()

def draw_game() -> bool:
    '''Generate game main menu screen.
    
    Returns: 
        boolean: Whether the menu is drawn (True) or not (False).
    '''
    menu_btn = Button('Main Menu', ((WIDTH - 200) // 2, HEIGHT - 150))
    menu_btn.draw()
    menu = menu_btn.check_clicked()

    screen.blit(ball, ((WIDTH - 150) // 2, (HEIGHT - 150) // 2))

    return menu

def drawText(text, fontname, fontsize, text_col, x, y):
    '''Generates text of a specific size and font at a specified position.
    
    Args:
        text (str): Text content to be generated.
        fontname (str): Desired font for text.
        fontsize (int): Desired size of text.
        text_col (int): Colour of text.
        x (int): x-coordinate position of text.
        y (int): y-coordinate position of text.
    '''
    font = pygame.font.Font(fontname, fontsize)
    text_surface = font.render(text, True, text_col)
    screen.blit(text_surface, ((x, y)))

def draw_save_screen():
    '''Generate game save screen displaying save slots for 3 games. Requires player login to access save files.
    
    Returns:
        int: The command input representing a screen chosen through mouse click by user.
        
    '''

    # screen dimensions and position
    save_menu_width = 300
    save_menu_height = 400
    save_menu_x = (WIDTH - save_menu_width) // 2
    save_menu_y = (HEIGHT - save_menu_height) // 2
    pygame.draw.rect(screen, 'black', [save_menu_x, save_menu_y, save_menu_width, save_menu_height])
    pygame.draw.rect(screen, 'green', [save_menu_x, save_menu_y, save_menu_width, save_menu_height], 5)

    # button dimensions and position
    button_width = 260
    button_height = 40
    button_margin = 20
    button_start_y = save_menu_y + 50

    # buttons representing game save slots
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

    # event handling for button clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if save1_btn.check_clicked():
                game_data = find_game_by_id(1)
                new_game = False
                player_info = player_info_by_saved_game(1)  # Get player info for gameid(1)
                # print(player_info)
                
                
                password1 = ''
                password1_rect = pygame.Rect(100, 100, 140, 32)
                password1_active = False
                password1_color = 'white'
                password1_font = pygame.font.Font(None, 32)
                password1_text = password1_font.render(password1, True, password1_color)
                password1_text_rect = password1_text.get_rect()
                password1_text_rect.center = password1_rect.center
                password1_rect.w = max(200, password1_text_rect.width + 10)
                
                username1 = ''
                username1_rect = pygame.Rect(100, 150, 140, 32)
                username1_active = False
                username1_color = 'white'
                username1_font = pygame.font.Font(None, 32)
                username1_text = username1_font.render(username1, True, username1_color)
                username1_text_rect = username1_text.get_rect()
                username1_text_rect.center = username1_rect.center
                username1_rect.w = max(200, username1_text_rect.width + 10)

                password2 = ''
                password2_rect = pygame.Rect(100, 200, 140, 32)
                password2_active = False
                password2_color = 'white'
                password2_font = pygame.font.Font(None, 32)
                password2_text = password2_font.render(password2, True, password2_color)
                password2_text_rect = password2_text.get_rect()
                password2_text_rect.center = password2_rect.center
                password2_rect.w = max(200, password2_text_rect.width + 10)
                
                username2 = ''
                username2_rect = pygame.Rect(100, 250, 140, 32)
                username2_active = False
                username2_color = 'white'
                username2_font = pygame.font.Font(None, 32)
                username2_text = username2_font.render(username2, True, username2_color)
                username2_text_rect = username2_text.get_rect()
                username2_text_rect.center = username2_rect.center
                username2_rect.w = max(200, username2_text_rect.width + 10)

                password3 = ''
                password3_rect = pygame.Rect(100, 300, 140, 32)
                password3_active = False
                password3_color = 'white'
                password3_font = pygame.font.Font(None, 32)
                password3_text = password3_font.render(password3, True, password3_color)
                password3_text_rect = password3_text.get_rect()
                password3_text_rect.center = password3_rect.center
                password3_rect.w = max(200, password3_text_rect.width + 10)
                
                username3 = ''
                username3_rect = pygame.Rect(100, 350, 140, 32)
                username3_active = False
                username3_color = 'white'
                username3_font = pygame.font.Font(None, 32)
                username3_text = username3_font.render(username3, True, username3_color)
                username3_text_rect = username3_text.get_rect()
                username3_text_rect.center = username3_rect.center
                username3_rect.w = max(200, username3_text_rect.width + 10)

                
                submit_button = Button('Submit', (100, 400), width=100, height=40)

                active = False
                while True:
                    screen.fill('black')
                    screen.blit(password1_text, password1_text_rect)
                    pygame.draw.rect(screen, 'lightgrey' if password1_active else 'white', password1_rect, 2)  
                    screen.blit(username1_text, username1_text_rect)
                    pygame.draw.rect(screen, 'lightgrey' if username1_active else 'white', username1_rect, 2) 
                    screen.blit(password2_text, password2_text_rect)
                    pygame.draw.rect(screen, 'lightgrey' if password2_active else 'white', password2_rect, 2)
                    screen.blit(username2_text, username2_text_rect)
                    pygame.draw.rect(screen, 'lightgrey' if username2_active else 'white', username2_rect, 2)
                    screen.blit(password3_text, password3_text_rect)
                    pygame.draw.rect(screen, 'lightgrey' if password3_active else 'white', password3_rect, 2)
                    screen.blit(username3_text, username3_text_rect)
                    pygame.draw.rect(screen, 'lightgrey' if username3_active else 'white', username3_rect, 2)

                    submit_button.draw()

                    password1_label = font.render("Password1:", True, 'white')
                    screen.blit(password1_label, (password1_rect.x + password1_rect.width + 10, password1_rect.y))
                    
                    username1_label = font.render("Username1:", True, 'white')
                    screen.blit(username1_label, (username1_rect.x + username1_rect.width + 10, username1_rect.y))

                    password2_label = font.render("Password2:", True, 'white')
                    screen.blit(password2_label, (password2_rect.x + password2_rect.width + 10, password2_rect.y))

                    username2_label = font.render("Username2:", True, 'white')
                    screen.blit(username2_label, (username2_rect.x + username2_rect.width + 10, username2_rect.y))

                    password3_label = font.render("Password3:", True, 'white')
                    screen.blit(password3_label, (password3_rect.x + password3_rect.width + 10, password3_rect.y))
                                
                    username3_label = font.render("Username3:", True, 'white')
                    screen.blit(username3_label, (username3_rect.x + username3_rect.width + 10, username3_rect.y))

                    if draw_back_button():
                        return 0
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if password1_rect.collidepoint(event.pos):
                                password1_active = not password1_active
                            else:
                                password1_active = False
                            password1_color = 'white' if password1_active else 'black'
                            
                            if username1_rect.collidepoint(event.pos):
                                username1_active = not username1_active
                            else:
                                username1_active = False
                            username1_color = 'white' if username1_active else 'black'

                            if password2_rect.collidepoint(event.pos):
                                password2_active = not password2_active
                            else:
                                password2_active = False
                            password2_color = 'white' if password2_active else 'black'

                            if username2_rect.collidepoint(event.pos):
                                username2_active = not username2_active
                            else:
                                username2_active = False
                            username2_color = 'white' if username2_active else 'black'

                            if password3_rect.collidepoint(event.pos):
                                password3_active = not password3_active
                            else:
                                password3_active = False
                            password3_color = 'white' if password3_active else 'black'

                            if username3_rect.collidepoint(event.pos):
                                username3_active = not username3_active
                            else:
                                username3_active = False
                            username3_color = 'white' if username3_active else 'black'


                            if submit_button.check_clicked():
                                if len(player_info) == 1 and username1 in player_info and password1 in player_info[username1]:
                                    new_game = False
                                    game(new_game=new_game, game_data=game_data)
                                elif len(player_info) == 2 and username1 in player_info and password1 in player_info[username1] and username2 in player_info and password2 in player_info[username2]:
                                    new_game = False
                                    game(new_game=new_game, game_data=game_data)
                                elif len(player_info) == 3 and username1 in player_info and password1 in player_info[username1] and username2 in player_info and password2 in player_info[username2] and username3 in player_info and password3 in player_info[username3]:
                                    new_game = False
                                    game(new_game=new_game, game_data=game_data)                                   
                                else:
                                    # print("Incorrect username or password. Returning to main menu.")
                                    return 0
                        if event.type == pygame.KEYDOWN:
                            if password1_active:
                                
                                if event.key == pygame.K_BACKSPACE:
                                    password1 = password1[:-1]
                                else:
                                    password1 += event.unicode
                                password1_text = password1_font.render(password1, True, password1_color)
                                password1_text_rect = password1_text.get_rect()
                                password1_text_rect.center = password1_rect.center
                                password1_rect.w = max(200, password1_text_rect.width + 10)

                            if username1_active:
                                if event.key == pygame.K_BACKSPACE:
                                    username1 = username1[:-1]
                                else:
                                    username1 += event.unicode
                                username1_text = username1_font.render(username1, True, username1_color)
                                username1_text_rect = username1_text.get_rect()
                                username1_text_rect.center = username1_rect.center
                                username1_rect.w = max(200, username1_text_rect.width + 10) 

                            if password2_active:
                                    
                                    if event.key == pygame.K_BACKSPACE:
                                        password2 = password2[:-1]
                                    else:
                                        password2 += event.unicode
                                    password2_text = password2_font.render(password2, True, password2_color)
                                    password2_text_rect = password2_text.get_rect()
                                    password2_text_rect.center = password2_rect.center
                                    password2_rect.w = max(200, password2_text_rect.width + 10)

                            if username2_active:
                                if event.key == pygame.K_BACKSPACE:
                                    username2 = username2[:-1]
                                else:
                                    username2 += event.unicode
                                username2_text = username2_font.render(username2, True, username2_color)
                                username2_text_rect = username2_text.get_rect()
                                username2_text_rect.center = username2_rect.center
                                username2_rect.w = max(200, username2_text_rect.width + 10)

                            if password3_active:
                                        
                                if event.key == pygame.K_BACKSPACE:
                                    password3 = password3[:-1]
                                else:
                                    password3 += event.unicode
                                password3_text = password3_font.render(password3, True, password3_color)
                                password3_text_rect = password3_text.get_rect()
                                password3_text_rect.center = password3_rect.center
                                password3_rect.w = max(200, password3_text_rect.width + 10)

                            if username3_active:
                                if event.key == pygame.K_BACKSPACE:
                                    username3 = username3[:-1]
                                else:
                                    username3 += event.unicode
                                username3_text = username3_font.render(username3, True, username3_color)
                                username3_text_rect = username3_text.get_rect()
                                username3_text_rect.center = username3_rect.center
                                username3_rect.w = max(200, username3_text_rect.width + 10)                
                
            elif save2_btn.check_clicked():
                game_data = find_game_by_id(2)
                new_game = False
                player_info = player_info_by_saved_game(2)  # Get player info for gameid(1)
                # print(player_info)
                
                
                password1 = ''
                password1_rect = pygame.Rect(100, 100, 140, 32)
                password1_active = False
                password1_color = 'white'
                password1_font = pygame.font.Font(None, 32)
                password1_text = password1_font.render(password1, True, password1_color)
                password1_text_rect = password1_text.get_rect()
                password1_text_rect.center = password1_rect.center
                password1_rect.w = max(200, password1_text_rect.width + 10)
                
                username1 = ''
                username1_rect = pygame.Rect(100, 150, 140, 32)
                username1_active = False
                username1_color = 'white'
                username1_font = pygame.font.Font(None, 32)
                username1_text = username1_font.render(username1, True, username1_color)
                username1_text_rect = username1_text.get_rect()
                username1_text_rect.center = username1_rect.center
                username1_rect.w = max(200, username1_text_rect.width + 10)

                password2 = ''
                password2_rect = pygame.Rect(100, 200, 140, 32)
                password2_active = False
                password2_color = 'white'
                password2_font = pygame.font.Font(None, 32)
                password2_text = password2_font.render(password2, True, password2_color)
                password2_text_rect = password2_text.get_rect()
                password2_text_rect.center = password2_rect.center
                password2_rect.w = max(200, password2_text_rect.width + 10)
                
                username2 = ''
                username2_rect = pygame.Rect(100, 250, 140, 32)
                username2_active = False
                username2_color = 'white'
                username2_font = pygame.font.Font(None, 32)
                username2_text = username2_font.render(username2, True, username2_color)
                username2_text_rect = username2_text.get_rect()
                username2_text_rect.center = username2_rect.center
                username2_rect.w = max(200, username2_text_rect.width + 10)

                password3 = ''
                password3_rect = pygame.Rect(100, 300, 140, 32)
                password3_active = False
                password3_color = 'white'
                password3_font = pygame.font.Font(None, 32)
                password3_text = password3_font.render(password3, True, password3_color)
                password3_text_rect = password3_text.get_rect()
                password3_text_rect.center = password3_rect.center
                password3_rect.w = max(200, password3_text_rect.width + 10)
                
                username3 = ''
                username3_rect = pygame.Rect(100, 350, 140, 32)
                username3_active = False
                username3_color = 'white'
                username3_font = pygame.font.Font(None, 32)
                username3_text = username3_font.render(username3, True, username3_color)
                username3_text_rect = username3_text.get_rect()
                username3_text_rect.center = username3_rect.center
                username3_rect.w = max(200, username3_text_rect.width + 10)

                
                submit_button = Button('Submit', (100, 400), width=100, height=40)

                active = False
                while True:
                    screen.fill('black')
                    screen.blit(password1_text, password1_text_rect)
                    pygame.draw.rect(screen, 'lightgrey' if password1_active else 'white', password1_rect, 2)  
                    screen.blit(username1_text, username1_text_rect)
                    pygame.draw.rect(screen, 'lightgrey' if username1_active else 'white', username1_rect, 2) 
                    screen.blit(password2_text, password2_text_rect)
                    pygame.draw.rect(screen, 'lightgrey' if password2_active else 'white', password2_rect, 2)
                    screen.blit(username2_text, username2_text_rect)
                    pygame.draw.rect(screen, 'lightgrey' if username2_active else 'white', username2_rect, 2)
                    screen.blit(password3_text, password3_text_rect)
                    pygame.draw.rect(screen, 'lightgrey' if password3_active else 'white', password3_rect, 2)
                    screen.blit(username3_text, username3_text_rect)
                    pygame.draw.rect(screen, 'lightgrey' if username3_active else 'white', username3_rect, 2)

                    submit_button.draw()

                    password1_label = font.render("Password1:", True, 'white')
                    screen.blit(password1_label, (password1_rect.x + password1_rect.width + 10, password1_rect.y))
                    
                    username1_label = font.render("Username1:", True, 'white')
                    screen.blit(username1_label, (username1_rect.x + username1_rect.width + 10, username1_rect.y))

                    password2_label = font.render("Password2:", True, 'white')
                    screen.blit(password2_label, (password2_rect.x + password2_rect.width + 10, password2_rect.y))

                    username2_label = font.render("Username2:", True, 'white')
                    screen.blit(username2_label, (username2_rect.x + username2_rect.width + 10, username2_rect.y))

                    password3_label = font.render("Password3:", True, 'white')
                    screen.blit(password3_label, (password3_rect.x + password3_rect.width + 10, password3_rect.y))
                                
                    username3_label = font.render("Username3:", True, 'white')
                    screen.blit(username3_label, (username3_rect.x + username3_rect.width + 10, username3_rect.y))

                    if draw_back_button():
                        return 0
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if password1_rect.collidepoint(event.pos):
                                password1_active = not password1_active
                            else:
                                password1_active = False
                            password1_color = 'white' if password1_active else 'black'
                            
                            if username1_rect.collidepoint(event.pos):
                                username1_active = not username1_active
                            else:
                                username1_active = False
                            username1_color = 'white' if username1_active else 'black'

                            if password2_rect.collidepoint(event.pos):
                                password2_active = not password2_active
                            else:
                                password2_active = False
                            password2_color = 'white' if password2_active else 'black'

                            if username2_rect.collidepoint(event.pos):
                                username2_active = not username2_active
                            else:
                                username2_active = False
                            username2_color = 'white' if username2_active else 'black'

                            if password3_rect.collidepoint(event.pos):
                                password3_active = not password3_active
                            else:
                                password3_active = False
                            password3_color = 'white' if password3_active else 'black'

                            if username3_rect.collidepoint(event.pos):
                                username3_active = not username3_active
                            else:
                                username3_active = False
                            username3_color = 'white' if username3_active else 'black'

                            if submit_button.check_clicked():
                                if len(player_info) == 1 and username1 in player_info and password1 in player_info[username1]:
                                    new_game = False
                                    game(new_game=new_game, game_data=game_data)
                                elif len(player_info) == 2 and username1 in player_info and password1 in player_info[username1] and username2 in player_info and password2 in player_info[username2]:
                                    new_game = False
                                    game(new_game=new_game, game_data=game_data)
                                elif len(player_info) == 3 and username1 in player_info and password1 in player_info[username1] and username2 in player_info and password2 in player_info[username2] and username3 in player_info and password3 in player_info[username3]:
                                    new_game = False
                                    game(new_game=new_game, game_data=game_data)                                   
                                else:
                                    # print("Incorrect username or password. Returning to main menu.")
                                    return 0
                                
                        if event.type == pygame.KEYDOWN:
                            if password1_active:
                                
                                if event.key == pygame.K_BACKSPACE:
                                    password1 = password1[:-1]
                                else:
                                    password1 += event.unicode
                                password1_text = password1_font.render(password1, True, password1_color)
                                password1_text_rect = password1_text.get_rect()
                                password1_text_rect.center = password1_rect.center
                                password1_rect.w = max(200, password1_text_rect.width + 10)

                            if username1_active:
                                if event.key == pygame.K_BACKSPACE:
                                    username1 = username1[:-1]
                                else:
                                    username1 += event.unicode
                                username1_text = username1_font.render(username1, True, username1_color)
                                username1_text_rect = username1_text.get_rect()
                                username1_text_rect.center = username1_rect.center
                                username1_rect.w = max(200, username1_text_rect.width + 10) 

                            if password2_active:
                                    
                                    if event.key == pygame.K_BACKSPACE:
                                        password2 = password2[:-1]
                                    else:
                                        password2 += event.unicode
                                    password2_text = password2_font.render(password2, True, password2_color)
                                    password2_text_rect = password2_text.get_rect()
                                    password2_text_rect.center = password2_rect.center
                                    password2_rect.w = max(200, password2_text_rect.width + 10)

                            if username2_active:
                                if event.key == pygame.K_BACKSPACE:
                                    username2 = username2[:-1]
                                else:
                                    username2 += event.unicode
                                username2_text = username2_font.render(username2, True, username2_color)
                                username2_text_rect = username2_text.get_rect()
                                username2_text_rect.center = username2_rect.center
                                username2_rect.w = max(200, username2_text_rect.width + 10)

                            if password3_active:
                                        
                                if event.key == pygame.K_BACKSPACE:
                                    password3 = password3[:-1]
                                else:
                                    password3 += event.unicode
                                password3_text = password3_font.render(password3, True, password3_color)
                                password3_text_rect = password3_text.get_rect()
                                password3_text_rect.center = password3_rect.center
                                password3_rect.w = max(200, password3_text_rect.width + 10)

                            if username3_active:
                                if event.key == pygame.K_BACKSPACE:
                                    username3 = username3[:-1]
                                else:
                                    username3 += event.unicode
                                username3_text = username3_font.render(username3, True, username3_color)
                                username3_text_rect = username3_text.get_rect()
                                username3_text_rect.center = username3_rect.center
                                username3_rect.w = max(200, username3_text_rect.width + 10)



            elif save3_btn.check_clicked():
                game_data = find_game_by_id(3)
                new_game = False
                player_info = player_info_by_saved_game(3)  # Get player info for gameid(1)
                # print(player_info)
                
                
                password1 = ''
                password1_rect = pygame.Rect(100, 100, 140, 32)
                password1_active = False
                password1_color = 'white'
                password1_font = pygame.font.Font(None, 32)
                password1_text = password1_font.render(password1, True, password1_color)
                password1_text_rect = password1_text.get_rect()
                password1_text_rect.center = password1_rect.center
                password1_rect.w = max(200, password1_text_rect.width + 10)
                
                username1 = ''
                username1_rect = pygame.Rect(100, 150, 140, 32)
                username1_active = False
                username1_color = 'white'
                username1_font = pygame.font.Font(None, 32)
                username1_text = username1_font.render(username1, True, username1_color)
                username1_text_rect = username1_text.get_rect()
                username1_text_rect.center = username1_rect.center
                username1_rect.w = max(200, username1_text_rect.width + 10)

                password2 = ''
                password2_rect = pygame.Rect(100, 200, 140, 32)
                password2_active = False
                password2_color = 'white'
                password2_font = pygame.font.Font(None, 32)
                password2_text = password2_font.render(password2, True, password2_color)
                password2_text_rect = password2_text.get_rect()
                password2_text_rect.center = password2_rect.center
                password2_rect.w = max(200, password2_text_rect.width + 10)
                
                username2 = ''
                username2_rect = pygame.Rect(100, 250, 140, 32)
                username2_active = False
                username2_color = 'white'
                username2_font = pygame.font.Font(None, 32)
                username2_text = username2_font.render(username2, True, username2_color)
                username2_text_rect = username2_text.get_rect()
                username2_text_rect.center = username2_rect.center
                username2_rect.w = max(200, username2_text_rect.width + 10)

                password3 = ''
                password3_rect = pygame.Rect(100, 300, 140, 32)
                password3_active = False
                password3_color = 'white'
                password3_font = pygame.font.Font(None, 32)
                password3_text = password3_font.render(password3, True, password3_color)
                password3_text_rect = password3_text.get_rect()
                password3_text_rect.center = password3_rect.center
                password3_rect.w = max(200, password3_text_rect.width + 10)
                
                username3 = ''
                username3_rect = pygame.Rect(100, 350, 140, 32)
                username3_active = False
                username3_color = 'white'
                username3_font = pygame.font.Font(None, 32)
                username3_text = username3_font.render(username3, True, username3_color)
                username3_text_rect = username3_text.get_rect()
                username3_text_rect.center = username3_rect.center
                username3_rect.w = max(200, username3_text_rect.width + 10)

                
                submit_button = Button('Submit', (100, 400), width=100, height=40)

                active = False
                while True:
                    screen.fill('black')
                    screen.blit(password1_text, password1_text_rect)
                    pygame.draw.rect(screen, 'lightgrey' if password1_active else 'white', password1_rect, 2)  
                    screen.blit(username1_text, username1_text_rect)
                    pygame.draw.rect(screen, 'lightgrey' if username1_active else 'white', username1_rect, 2) 
                    screen.blit(password2_text, password2_text_rect)
                    pygame.draw.rect(screen, 'lightgrey' if password2_active else 'white', password2_rect, 2)
                    screen.blit(username2_text, username2_text_rect)
                    pygame.draw.rect(screen, 'lightgrey' if username2_active else 'white', username2_rect, 2)
                    screen.blit(password3_text, password3_text_rect)
                    pygame.draw.rect(screen, 'lightgrey' if password3_active else 'white', password3_rect, 2)
                    screen.blit(username3_text, username3_text_rect)
                    pygame.draw.rect(screen, 'lightgrey' if username3_active else 'white', username3_rect, 2)

                    submit_button.draw()

                    password1_label = font.render("Password1:", True, 'white')
                    screen.blit(password1_label, (password1_rect.x + password1_rect.width + 10, password1_rect.y))
                    
                    username1_label = font.render("Username1:", True, 'white')
                    screen.blit(username1_label, (username1_rect.x + username1_rect.width + 10, username1_rect.y))

                    password2_label = font.render("Password2:", True, 'white')
                    screen.blit(password2_label, (password2_rect.x + password2_rect.width + 10, password2_rect.y))

                    username2_label = font.render("Username2:", True, 'white')
                    screen.blit(username2_label, (username2_rect.x + username2_rect.width + 10, username2_rect.y))

                    password3_label = font.render("Password3:", True, 'white')
                    screen.blit(password3_label, (password3_rect.x + password3_rect.width + 10, password3_rect.y))
                                
                    username3_label = font.render("Username3:", True, 'white')
                    screen.blit(username3_label, (username3_rect.x + username3_rect.width + 10, username3_rect.y))

                    if draw_back_button():
                        return 0
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if password1_rect.collidepoint(event.pos):
                                password1_active = not password1_active
                            else:
                                password1_active = False
                            password1_color = 'white' if password1_active else 'black'
                            
                            if username1_rect.collidepoint(event.pos):
                                username1_active = not username1_active
                            else:
                                username1_active = False
                            username1_color = 'white' if username1_active else 'black'

                            if password2_rect.collidepoint(event.pos):
                                password2_active = not password2_active
                            else:
                                password2_active = False
                            password2_color = 'white' if password2_active else 'black'

                            if username2_rect.collidepoint(event.pos):
                                username2_active = not username2_active
                            else:
                                username2_active = False
                            username2_color = 'white' if username2_active else 'black'

                            if password3_rect.collidepoint(event.pos):
                                password3_active = not password3_active
                            else:
                                password3_active = False
                            password3_color = 'white' if password3_active else 'black'

                            if username3_rect.collidepoint(event.pos):
                                username3_active = not username3_active
                            else:
                                username3_active = False
                            username3_color = 'white' if username3_active else 'black'

                            if submit_button.check_clicked():
                                if len(player_info) == 1 and username1 in player_info and password1 in player_info[username1]:
                                    new_game = False
                                    game(new_game=new_game, game_data=game_data)
                                elif len(player_info) == 2 and username1 in player_info and password1 in player_info[username1] and username2 in player_info and password2 in player_info[username2]:
                                    new_game = False
                                    game(new_game=new_game, game_data=game_data)
                                elif len(player_info) == 3 and username1 in player_info and password1 in player_info[username1] and username2 in player_info and password2 in player_info[username2] and username3 in player_info and password3 in player_info[username3]:
                                    new_game = False
                                    game(new_game=new_game, game_data=game_data)                                   
                                else:
                                    # print("Incorrect username or password. Returning to main menu.")
                                    return 0
                                
                        if event.type == pygame.KEYDOWN:
                            if password1_active:
                                
                                if event.key == pygame.K_BACKSPACE:
                                    password1 = password1[:-1]
                                else:
                                    password1 += event.unicode
                                password1_text = password1_font.render(password1, True, password1_color)
                                password1_text_rect = password1_text.get_rect()
                                password1_text_rect.center = password1_rect.center
                                password1_rect.w = max(200, password1_text_rect.width + 10)

                            if username1_active:
                                if event.key == pygame.K_BACKSPACE:
                                    username1 = username1[:-1]
                                else:
                                    username1 += event.unicode
                                username1_text = username1_font.render(username1, True, username1_color)
                                username1_text_rect = username1_text.get_rect()
                                username1_text_rect.center = username1_rect.center
                                username1_rect.w = max(200, username1_text_rect.width + 10) 

                            if password2_active:
                                    
                                    if event.key == pygame.K_BACKSPACE:
                                        password2 = password2[:-1]
                                    else:
                                        password2 += event.unicode
                                    password2_text = password2_font.render(password2, True, password2_color)
                                    password2_text_rect = password2_text.get_rect()
                                    password2_text_rect.center = password2_rect.center
                                    password2_rect.w = max(200, password2_text_rect.width + 10)

                            if username2_active:
                                if event.key == pygame.K_BACKSPACE:
                                    username2 = username2[:-1]
                                else:
                                    username2 += event.unicode
                                username2_text = username2_font.render(username2, True, username2_color)
                                username2_text_rect = username2_text.get_rect()
                                username2_text_rect.center = username2_rect.center
                                username2_rect.w = max(200, username2_text_rect.width + 10)

                            if password3_active:
                                        
                                if event.key == pygame.K_BACKSPACE:
                                    password3 = password3[:-1]
                                else:
                                    password3 += event.unicode
                                password3_text = password3_font.render(password3, True, password3_color)
                                password3_text_rect = password3_text.get_rect()
                                password3_text_rect.center = password3_rect.center
                                password3_rect.w = max(200, password3_text_rect.width + 10)

                            if username3_active:
                                if event.key == pygame.K_BACKSPACE:
                                    username3 = username3[:-1]
                                else:
                                    username3 += event.unicode
                                username3_text = username3_font.render(username3, True, username3_color)
                                username3_text_rect = username3_text.get_rect()
                                username3_text_rect.center = username3_rect.center
                                username3_rect.w = max(200, username3_text_rect.width + 10)




            else:
                game_data = None
            if game_data == None:
                pass
            else:
                game(new_game=new_game, game_data=game_data)
                menu_command = 0
    return 0




def draw_highscore_screen():
    '''Generate highscore screen showing top players in the game.'''
    highscore_menu_width = 400
    highscore_menu_height = 400
    highscore_menu_x = (WIDTH - highscore_menu_width) // 2
    highscore_menu_y = (HEIGHT - highscore_menu_height) // 2
    pygame.draw.rect(screen, 'black', [highscore_menu_x, highscore_menu_y, highscore_menu_width, highscore_menu_height])
    pygame.draw.rect(screen, 'green', [highscore_menu_x, highscore_menu_y, highscore_menu_width, highscore_menu_height],5)

    # Display high scores
    high_scores = get_player_scores() # Get high scores from the database

    y_offset = highscore_menu_y + 50
    for player, score in high_scores.items():
        text_surface = font.render(f'{player}: {score}', True, 'white')
        screen.blit(text_surface, (highscore_menu_x + 50, y_offset))
        y_offset += 40


def draw_back_button() -> bool:
    '''Generate button representing the "Back".
    
    Returns:
        boolean: Whether button is drawn (True) or not (False).
    '''
    back_button = Button('Back', (20, 20), width=100, height=40)
    back_button.draw()
    if back_button.check_clicked():
        return True
    return False

def draw_player_login():
    '''Generate player login screen.
    
    Returns:
        int: Number representing the user mouse input.'''
    entering_user_data = True
    rect_x = (WIDTH - 880) // 2
    rect_y = (HEIGHT - 600) // 2
    pygame.draw.rect(screen, 'black', [0, 0, 1280, 800])
    pygame.draw.rect(screen, 'white', [rect_x, rect_y, 880, 600])
    pygame.draw.rect(screen, 'black', [rect_x+BOARD_OUTLINE_OFFSET, rect_y+BOARD_OUTLINE_OFFSET, 880-(BOARD_OUTLINE_OFFSET*2), 600-(BOARD_OUTLINE_OFFSET*2)])
    drawText("Add Players", other_font, 40, WHITE, rect_x*2+150, rect_y+40)
    drawText("Username: ", other_font, 30, WHITE, rect_x+90, rect_y+200)
    pygame.draw.rect(screen, 'white', [rect_x+275, rect_y+200, 220, 40])
    pygame.draw.rect(screen, 'black', [rect_x+275+USER_ENTER_OFFSET, rect_y+200+USER_ENTER_OFFSET, 220-(USER_ENTER_OFFSET*2), 40-(USER_ENTER_OFFSET*2)])
    drawText("Password: ", other_font, 30, WHITE, rect_x+90, rect_y+270)
    drawText(("Player Count: "+str(len(player_list))), other_font, 30, WHITE, rect_x+90, rect_y+340)
    pygame.draw.rect(screen, 'white', [rect_x+275, rect_y+270, 220, 40])
    pygame.draw.rect(screen, 'black', [rect_x+275+USER_ENTER_OFFSET, rect_y+270+USER_ENTER_OFFSET, 220-(USER_ENTER_OFFSET*2), 40-(USER_ENTER_OFFSET*2)])
    drawText(username_enter, other_font, 30, WHITE, rect_x+277, rect_y+205)
    drawText(str("*"*len(password_enter)), other_font, 30, WHITE, rect_x+277, rect_y+275)
    add_new_user_button = Button('Add User', ((WIDTH - 880) // 2 + 160, (HEIGHT - 600) // 2 + 500))
    add_new_user_button.draw()
    add_new_user_button = Button('Start Game', ((WIDTH - 880) // 2 + 450, (HEIGHT - 600) // 2 + 500))
    add_new_user_button.draw()
    if show_too_many_user_error:
        drawText("Too Many Users Added To Game", other_font, 30, RED, (WIDTH - 880) // 2 + 230, (HEIGHT - 600) // 2 +400)
    elif show_no_user_error:
        drawText("No Users Added", other_font, 30, RED, (WIDTH - 880) // 2+ 320, (HEIGHT - 600) // 2+ 400)
    elif show_empty_name:
        drawText("You Must Fill In Username and Password Field", other_font, 30, RED, (WIDTH - 880) // 2+ 130, (HEIGHT - 600) // 2+ 400)
    elif show_existing_user:
        drawText("Name Taken", other_font, 30, RED, (WIDTH - 880) // 2+ 325, (HEIGHT - 600) // 2+ 400)
tutorial_state = 0
run = True
while run:
    screen.fill('black')
    timer.tick(FPS)

    draw_heading()

    if main_menu:
        menu_command = draw_menu()  # number representing user mouse input
        if menu_command != -1:
            main_menu = False
            if menu_command == 5:   # Exit Menu button pressed
                pygame.quit()
                sys.exit()
    else:
        if menu_command == 2:       # if user clicks on save
            save_command = draw_save_screen()
            if draw_back_button():
                main_menu = True
            if save_command != 0:
                main_menu = True
        elif menu_command == 3:     # Highscore button pressed
            draw_highscore_screen()
            if draw_back_button():
                main_menu = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        elif menu_command == 1:     # Start button pressed
            menu_command = 4

        elif menu_command == 4:
            draw_player_login()
            if draw_back_button():
                main_menu = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key != pygame.K_RETURN:
                    if (username_enter_active):
                        if event.key == pygame.K_BACKSPACE:
                            username_enter = username_enter[0:-1]
                        else:
                            username_enter += event.unicode
                    elif (password_enter_active):
                        if event.key == pygame.K_BACKSPACE:
                            password_enter = password_enter[0:-1]
                        else:
                            password_enter += event.unicode
                    else:
                        pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if (WIDTH - 880) // 2 + 275 <= mouse_pos[0] <= (WIDTH - 880) // 2 + 495 and (HEIGHT - 600) // 2 + 200 <= mouse_pos[1] <=(HEIGHT - 600) // 2 + 240:
                        username_enter_active = True
                        password_enter_active = False
                    elif (WIDTH - 880) // 2 + 275 <= mouse_pos[0] <= (WIDTH - 880) // 2 + 495 and (HEIGHT - 600) // 2 + 270 <= mouse_pos[1] <=(HEIGHT - 600) // 2 + 310:
                        username_enter_active = False
                        password_enter_active = True
                    elif (WIDTH - 880) // 2 + 160 <= mouse_pos[0] <= (WIDTH - 880) // 2 + 420 and (HEIGHT - 600) // 2 + 500 <= mouse_pos[1] <= (HEIGHT - 600) // 2 + 540:
                        if len(player_list) < 3 and username_enter != '' and password_enter != '' and username_enter not in player_list:
                            player_list.append({"name":username_enter,"password":password_enter,"streak":0,"duck_count":0,"score":0})
                            username_enter = ''
                            password_enter = ''
                            show_no_user_error = False
                            show_empty_name = False
                            show_existing_user = False
                            show_too_many_user_error = False
                        elif username_enter == '' or password_enter == '':
                            show_empty_name = True
                            show_no_user_error = False
                            show_too_many_user_error = False
                            show_existing_user = False
                        elif username_enter in player_list:
                            show_existing_user = True
                            show_empty_name = False
                            show_no_user_error = False
                            show_too_many_user_error = False
                        else:
                            show_too_many_user_error = True
                            show_no_user_error = False
                            show_empty_name = False
                            show_existing_user = False

                    elif (WIDTH - 880) // 2 + 450 <= mouse_pos[0] <= (WIDTH - 880) // 2 + 710 and (HEIGHT - 600) // 2 + 500 <= mouse_pos[1] <= (HEIGHT - 600) // 2 + 540:
                        if len(player_list) > 0:
                            game(True, player_list=player_list)
                            player_list = []
                            menu_command = 0
                            username_enter = ''
                            password_enter = ''
                        else:
                            show_too_many_user_error = False
                            show_empty_name = False
                            show_no_user_error = True
                    else:
                        username_enter_active = False
                        password_enter_active = False

        elif menu_command == 6:
            pygame.draw.rect(screen, BLACK, (0,0, 1280, 800))
            show_tutorial(tutorial_state)   # display tutorial screens
            draw_next_button = Button('Next', (700, 700), width=200, height=40)
            draw_next_button.draw()
            draw_prev_button = Button('Previous', (400, 700), width=200, height=40)
            draw_prev_button.draw()
            draw_back_button()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if draw_next_button.check_clicked():    # allows user to scroll through various tutorial screens
                        if tutorial_state < 5:
                            tutorial_state += 1
                    elif draw_prev_button.check_clicked():
                        if tutorial_state > 0:
                            tutorial_state -= 1
                    elif draw_back_button():
                        tutorial_state = 0
                        menu_command = 0
        
        else:
            main_menu = draw_game()
            if menu_command > 0:
                text = font.render(f'Button {menu_command} pressed!', True, 'black')
                screen.blit(text, (150, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if main_menu:       # Only show exit menu in the main menu screen
                    pygame.quit()
                    sys.exit()
    pygame.display.flip()

pygame.quit()   # completely quits game
