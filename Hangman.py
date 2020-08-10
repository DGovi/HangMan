import pygame
import os

# setting up the screen
pygame.init()
WIDTH = 800
HEIGHT = 500
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

MAXFPS = 60
clock = pygame.time.Clock()
isRunning = True

while isRunning:
    clock.tick(MAXFPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False


pygame.quit()
