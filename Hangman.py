import pygame
import math
import random

# setting up the screen
pygame.init()
WIDTH = 900
HEIGHT = 500
disp = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# game "settings"
isRunning = True
MAXFPS = 60
clock = pygame.time.Clock()

# colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# loading up hangman images
images = []
for i in range(7):
    anImage = pygame.image.load("hangman" + str(i) + ".png")
    images.append(anImage)

# font
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)


# button variables, values are in pixels
RADIUS = 20
GAP = 20
letter_buttons = []
button_xcoor = WIDTH // 14
button_ycoor = 400
for i in range(26):
    x = button_xcoor + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = button_ycoor + (i // 13) * (GAP + RADIUS * 2)
    letter_buttons.append([x, y, chr(65 + i), True])  # 65 is the capital letter "A"

# alternative way to input letters is to use he keyboard keys

# game variables
current_png = 0
words = ["WORD", "ORANGE", "MANGO", "FRUIT", "SAUSAGE", "FLAMINGO", "COMPUTER"]
word = random.choice(words)
guessed = []


# methods
def draw():
    disp.fill(WHITE)
    # DARW TITLE
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    disp.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))
    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    disp.blit(text, (400, 200))
    # draw buttons
    for letter in letter_buttons:
        x, y, current_letter, visible = letter
        if visible:
            pygame.draw.circle(disp, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(current_letter, 1, BLACK)
            disp.blit(text, (x - text.get_width() / 2, y - text.get_width() / 2))

    disp.blit(images[current_png], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    text = WORD_FONT.render(message + " the word was \n" + word, 1, BLACK)
    disp.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


# game loop
while isRunning:
    clock.tick(MAXFPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for letter in letter_buttons:
                x, y, current_letter, visible = letter
                if visible:
                    distance = math.sqrt((x - mouse_x)**2 + (y - mouse_y)**2)
                    if distance < RADIUS:
                        letter[3] = False
                        guessed.append(current_letter)
                        if current_letter not in word:
                            current_png += 1
    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won:
        disp.fill(GREEN)
        display_message("YOU WON!")
        break

    if current_png == 6:
        disp.fill(RED)
        display_message("YOU LOSE!")
        break


pygame.quit()
