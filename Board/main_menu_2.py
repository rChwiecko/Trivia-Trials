import pygame
import sys
from queryManager import *
from main import *
from const import *
WIDTH = 1280
HEIGHT = 800
FPS = 60
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
menu_command = 0

# Load logo image
logo = pygame.image.load('assets/transparentduck.png')  # Replace 'logo.png' with the path to your logo image
logo = pygame.transform.scale(logo, (100, 100))  # Scale the logo to an appropriate size


class Button:
    def __init__(self, txt, pos, width=260, height=40):
        self.text = txt
        self.pos = pos
        self.width = width
        self.height = height
        self.button = pygame.Rect(self.pos, (self.width, self.height))

    def draw(self):
        pygame.draw.rect(screen, 'light gray', self.button, 0, 5)
        pygame.draw.rect(screen, 'dark gray', self.button, 5, 5)
        text2 = font.render(self.text, True, 'black')
        text_rect = text2.get_rect(center=self.button.center)
        screen.blit(text2, text_rect.topleft)

    def check_clicked(self):
        return self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]


def draw_heading():
    heading_text = font_heading.render("Trivia Trials", True, 'white')
    screen.blit(heading_text, ((WIDTH - heading_text.get_width()) // 2, 50))
    # Blit logo onto the screen above all buttons
    screen.blit(logo, ((WIDTH - logo.get_width()) // 2, 100))  # Adjust position as needed


def draw_menu():
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
    playerdetailsbutton = Button('Player Details', (menu_x + 20, menu_y + 260))  # Adjusted position
    playerdetailsbutton.draw()
    godmodebutton = Button('God Mode', (menu_x + 20, menu_y + 320))  # Adjusted position
    godmodebutton.draw()

    exit_button = Button('Exit Game', (menu_x + 20, menu_y + 380))  # Adjusted position
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
    if playerdetailsbutton.check_clicked():
        draw_password_screen()
    if godmodebutton.check_clicked():
        draw_god_mode()

    return command

def draw_password_screen():
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
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
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
                
                if submit_button.check_clicked():
                    if password == '1234':
                        running = True
                        while running:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    running = False
                                    pygame.quit()
                                    sys.exit()
                            draw_player_details()
                            pygame.display.flip()
                        return password, username
                    
            if event.type == pygame.KEYDOWN:
                if password_active:
                    if event.key == pygame.K_RETURN:
                        if password == '1234':
                            draw_player_details()
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
                            draw_player_details()
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

def draw_player_details():
    # use get_player_info() to get the player info, then display it on the screen
    player_info = get_player_info()
    y_offset = 500
    if draw_back_button():
        return 0
    for player, info in player_info.items():
        text_surface = font.render(f'{player}: {info}', True, 'white')
        screen.blit(text_surface, (50, y_offset))
        y_offset += 40

def draw_god_mode():
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
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
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
                
                if submit_button.check_clicked():
                    if password == '1234':
                        generate_game_data()
                        return password, username
                    
            if event.type == pygame.KEYDOWN:
                if password_active:
                    if event.key == pygame.K_RETURN:
                        if password == '1234':
                            generate_game_data()
                            return password, username
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
                            generate_game_data()
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

def generate_game_data():
    level = ''
    level_rect = pygame.Rect(100, 100, 140, 32)
    level_active = False
    level_color = 'white'
    level_font = pygame.font.Font(None, 32)
    level_text = level_font.render(level, True, level_color)
    level_text_rect = level_text.get_rect()
    level_text_rect.center = level_rect.center
    level_rect.w = max(200, level_text_rect.width + 10)
    
    index = ''
    index_rect = pygame.Rect(100, 150, 140, 32)
    index_active = False
    index_color = 'white'
    index_font = pygame.font.Font(None, 32)
    index_text = index_font.render(index, True, index_color)
    index_text_rect = index_text.get_rect()
    index_text_rect.center = index_rect.center
    index_rect.w = max(200, index_text_rect.width + 10)

    streak = ''
    streak_rect = pygame.Rect(100, 200, 140, 32)
    streak_active = False
    streak_color = 'white'
    streak_font = pygame.font.Font(None, 32)
    streak_text = streak_font.render(streak, True, streak_color)
    streak_text_rect = streak_text.get_rect()
    streak_text_rect.center = streak_rect.center
    streak_rect.w = max(200, streak_text_rect.width + 10)

    duck_count = ''
    duck_count_rect = pygame.Rect(100, 250, 140, 32)
    duck_count_active = False
    duck_count_color = 'white'
    duck_count_font = pygame.font.Font(None, 32)
    duck_count_text = duck_count_font.render(duck_count, True, duck_count_color)
    duck_count_text_rect = duck_count_text.get_rect()
    duck_count_text_rect.center = duck_count_rect.center
    duck_count_rect.w = max(200, duck_count_text_rect.width + 10)
    
    score = ''
    score_rect = pygame.Rect(100, 300, 140, 32)
    score_active = False
    score_color = 'white'
    score_font = pygame.font.Font(None, 32)
    score_text = score_font.render(score, True, score_color)
    score_text_rect = score_text.get_rect()
    score_text_rect.center = score_rect.center
    score_rect.w = max(200, score_text_rect.width + 10)

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
            # main menu
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
                
                if submit_button.check_clicked():
                    # turn it into a game data object
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

def draw_game():
    menu_btn = Button('Main Menu', ((WIDTH - 200) // 2, HEIGHT - 150))
    menu_btn.draw()
    menu = menu_btn.check_clicked()

    screen.blit(ball, ((WIDTH - 150) // 2, (HEIGHT - 150) // 2))

    return menu

def drawText(text, fontname, fontsize, text_col, x, y):
    font = pygame.font.Font(fontname, fontsize)
    text_surface = font.render(text, True, text_col)
    screen.blit(text_surface, ((x, y)))

def draw_save_screen():
    save_menu_width = 300
    save_menu_height = 400
    save_menu_x = (WIDTH - save_menu_width) // 2
    save_menu_y = (HEIGHT - save_menu_height) // 2
    pygame.draw.rect(screen, 'black', [save_menu_x, save_menu_y, save_menu_width, save_menu_height])
    pygame.draw.rect(screen, 'green', [save_menu_x, save_menu_y, save_menu_width, save_menu_height], 5)

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
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if save1_btn.check_clicked():
                game_data =  find_game_by_id(1)
                new_game = False
            elif save2_btn.check_clicked():
                game_data =  find_game_by_id(2)
                new_game = False
            elif save3_btn.check_clicked():
                game_data =  find_game_by_id(3)
                new_game = False
            else:
                game_data = None
            if game_data == None:
                pass
            else:
                game(new_game=new_game, game_data=game_data)
                menu_command = 0
    return 0


def draw_highscore_screen():
    highscore_menu_width = 400
    highscore_menu_height = 400
    highscore_menu_x = (WIDTH - highscore_menu_width) // 2
    highscore_menu_y = (HEIGHT - highscore_menu_height) // 2
    pygame.draw.rect(screen, 'black', [highscore_menu_x, highscore_menu_y, highscore_menu_width, highscore_menu_height])
    pygame.draw.rect(screen, 'green', [highscore_menu_x, highscore_menu_y, highscore_menu_width, highscore_menu_height],
                     5)

    # Display high scores
    high_scores = get_player_scores() # Get high scores from the database

    y_offset = highscore_menu_y + 50
    for player, score in high_scores.items():
        text_surface = font.render(f'{player}: {score}', True, 'white')
        screen.blit(text_surface, (highscore_menu_x + 50, y_offset))
        y_offset += 40


def draw_back_button():
    back_button = Button('Back', (20, 20), width=100, height=40)
    back_button.draw()
    if back_button.check_clicked():
        return True
    return False

def draw_player_login():
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
run = True
while run:
    screen.fill('black')
    timer.tick(FPS)

    draw_heading()

    if main_menu:
        menu_command = draw_menu()
        if menu_command != -1:
            main_menu = False
            if menu_command == 5:  # Exit Menu button pressed
                pygame.quit()
                sys.exit()
    else:
        if menu_command == 2:
            save_command = draw_save_screen()
            if draw_back_button():
                main_menu = True
            if save_command != 0:
                print(f'{save_command}')
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
            screen.fill('black')
            # Display role selection screen
            dev_button = Button('Developer', (WIDTH // 2 - 100, HEIGHT // 2 - 50), width=200)
            dev_button.draw()
            instructor_button = Button('Instructor', (WIDTH // 2 - 100, HEIGHT // 2 + 20), width=200)
            instructor_button.draw()
            player_button = Button('Player', (WIDTH // 2 - 100, HEIGHT // 2 + 90), width=200)
            player_button.draw()

            menu_btn = Button('Main Menu', ((WIDTH - 200) // 2, HEIGHT - 150))
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
                        menu_command = 4
                    elif menu_btn.check_clicked():
                        main_menu = True

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
                if main_menu:  # Only show exit menu in the main menu screen
                    pygame.quit()
                    sys.exit()
    pygame.display.flip()

pygame.quit()
