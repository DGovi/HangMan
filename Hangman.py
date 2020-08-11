import pygame
import math

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
PINK = (255, 44, 210)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# loading up hangman images
images = []
for i in range(7):
    anImage = pygame.image.load("hangman" + str(i) + ".png")
    images.append(anImage)

# font
LETTER_FONT = pygame.font.SysFont('comicsans', 40)


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

# methods


def draw():
    disp.fill(PINK)
    # draw buttons
    for letter in letter_buttons:
        x, y, current_letter, visible = letter
        if visible:
            pygame.draw.circle(disp, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(current_letter, 1, BLACK)
            disp.blit(text, (x - text.get_width() / 2, y - text.get_width() / 2))

    disp.blit(images[current_png], (150, 100))
    pygame.display.update()


# game loop
while isRunning:
    clock.tick(MAXFPS)

    draw()

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

pygame.quit()
