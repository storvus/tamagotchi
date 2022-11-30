import sys
import time

import pygame

from game import Game
from lib.constants import Color

pygame.init()
pygame.display.set_caption('Tamagotchi')

width, height = 500, 500
screen = pygame.display.set_mode([width, height])
fps = pygame.time.Clock()

game = Game(screen)

while True:
    screen.fill(Color.WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        else:
            game.handle_event(event)

    game.display()
    pygame.display.update()
    if game.is_over():
        time.sleep(5)
        pygame.quit()
        quit()

    fps.tick(30)
