"""make this a method"""
import pygame
import sys

# pygame initialization preliminaries
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
txtFont = pygame.font.get_default_font()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Leaderboard")

# # Sample leaderboard data (score, player_name)
# leaderboard_data = [
#     (100, "Player 1"),
#     (90, "Player 2"),
#     (80, "Player 3"),
#     (70, "Player 4"),
#     (60, "Player 5")
# ]

# writes text
def drawText(self, text, fontname=txtFont, fontsize=30, text_col=BLACK, x=640, y=400):
    font = pygame.font.Font(fontname, fontsize)
    text_surface = font.render(text, True, text_col)
    screen.blit(text_surface, (x, y))

def drawLeaderboard(screen):

    # leaderboard title
    # drawText(text="Leaderboard", y = 50)
    font = pygame.font.SysFont(None, 80)
    title_text = font.render("Leaderboard", True, BLACK)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 50))

    # make rectangles .rect(scren, color, (x, y, width, height))
    rect1 = pygame.draw.rect(screen, BLACK, (40, 240, 1200, 240))
    rect2 = pygame.draw.rect(screen, WHITE, (42, 242, 1196, 236))

    # top 1
    font = pygame.font.Font(txtFont, 24)
    text_surface = font.render("Top 1", True, BLACK)
    screen.blit(text_surface, (270, 270))

    # top 2
    font = pygame.font.Font(txtFont, 24)
    text_surface = font.render("Top 2", True, BLACK)
    screen.blit(text_surface, (270, 350))

    # top 3
    font = pygame.font.Font(txtFont, 24)
    text_surface = font.render("Top 3", True, BLACK)
    screen.blit(text_surface, (270, 430))

    # get player1 scores
    font = pygame.font.Font(txtFont, 24)
    text_surface = font.render("Player1.getScore", True, BLACK)
    screen.blit(text_surface, (870, 270))

    # get player2 scores
    font = pygame.font.Font(txtFont, 24)
    text_surface = font.render("Player2.getScore", True, BLACK)
    screen.blit(text_surface, (870, 350))

    # get player3 scores
    font = pygame.font.Font(txtFont, 24)
    text_surface = font.render("Player3.getScore", True, BLACK)
    screen.blit(text_surface, (870, 430))

    # back to home button .rect(scren, color, (x, y, width, height)) 
    rect1 = pygame.draw.rect(screen, BLACK, (940, 700, 300, 40))
    rect2 = pygame.draw.rect(screen, WHITE, (942, 702, 296, 36))
    font = pygame.font.Font(txtFont, 20)
    text_surface = font.render("Back to Main Menu", True, BLACK)
    screen.blit(text_surface, (950, 710))

def main():
    pygame.init()
    running = True      # main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)      # generate screen

        # Draw leaderboard
        drawLeaderboard(screen)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
