import pygame

from lib.constants import Color


class Statistic:

    def __init__(self, game) -> None:
        self.game = game
        self.font = pygame.font.Font(pygame.font.get_default_font(), 12)

    def show(self):
        self.show_health_level()
        self.show_hunger_level()
    
    def show_health_level(self):
        max_health_level = self.game.get_max_health_level()
        health_level = self.game.get_health_level()
        text_surface = self.font.render("L:", True, Color.BLACK)
        screen = self.game.get_screen()
        screen.blit(text_surface, (2, 14))
        color = Color.RED if self.game.is_harm_received() else Color.BLACK
        pygame.draw.rect(screen, color, pygame.Rect(18, 10, max_health_level + 8, 20),  2)
        pygame.draw.rect(screen, color, pygame.Rect(22, 14, health_level, 12))

    def show_hunger_level(self):
        max_hunger_level = self.game.get_max_hunger_level()
        hunger_level = self.game.get_hunger_level()
        text_surface = self.font.render("H:", True, Color.BLACK)
        screen = self.game.get_screen()
        screen.blit(text_surface, (2, 40))
        color = Color.RED if self.game.is_hunger_critical() else Color.BLACK
        pygame.draw.rect(screen, color, pygame.Rect(18, 36, max_hunger_level + 8, 20),  2)
        pygame.draw.rect(screen, color, pygame.Rect(22, 40, hunger_level, 12))

