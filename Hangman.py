import pygame

# setting up the screen
pygame.init()
WIDTH = 800
HEIGHT = 500
PINK = (255, 44, 210)
disp = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

MAXFPS = 60
clock = pygame.time.Clock()
isRunning = True

# loading up images
images = []
for i in range(7):
    anImage = pygame.image.load("hangman" + str(i) + ".png")
    images.append(anImage)

# game variable
current_png = 0

# game loop
while isRunning:
    clock.tick(MAXFPS)

    disp.fill(PINK)
    disp.blit(images[current_png], (155, 100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()
