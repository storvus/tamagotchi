import pygame

from lib.constants import Color

# Default button images/pygame.Surfaces.
IMAGE_NORMAL = pygame.Surface((100, 32))
IMAGE_NORMAL.fill(pygame.Color('dodgerblue1'))
IMAGE_HOVER = pygame.Surface((100, 32))
IMAGE_HOVER.fill(pygame.Color('lightskyblue'))
IMAGE_DOWN = pygame.Surface((100, 32))
IMAGE_DOWN.fill(pygame.Color('aquamarine1'))


class MenuButton(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, callback, font=None, text='', text_color=Color.BLACK,
                 image_normal=IMAGE_NORMAL, image_hover=IMAGE_HOVER, image_down=IMAGE_DOWN):
        super().__init__()
        if not font:
            font = pygame.font.Font(pygame.font.get_default_font(), 12)
        # Scale the images to the desired size (doesn't modify the originals).
        self.image_normal = pygame.transform.scale(image_normal, (width, height))
        self.image_hover = pygame.transform.scale(image_hover, (width, height))
        self.image_down = pygame.transform.scale(image_down, (width, height))
        self.text = text
        self.image = self.image_normal  # The currently active image.
        self.rect = self.image.get_rect(topleft=(x, y))
        # This function will be called when the button gets pressed.
        self.callback = callback
        self.button_down = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.image = self.image_down
                self.button_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            # If the rect collides with the mouse pos.
            if self.rect.collidepoint(event.pos) and self.button_down:
                self.callback(self.text)  # Call the function.
                self.image = self.image_hover
            self.button_down = False
        elif event.type == pygame.MOUSEMOTION:
            collided = self.rect.collidepoint(event.pos)
            if collided and not self.button_down:
                self.image = self.image_hover
            elif not collided:
                self.image = self.image_normal
