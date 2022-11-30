import logging
import os

import pygame

from components.button import MenuButton
from config import RESOURCES_DIR
from entities.food.factory import FoodFactory
from lib.constants import Food

logger = logging.getLogger(__name__)


class PetControl:
    CONTROLS_PATH = os.path.join(RESOURCES_DIR, "controls")

    def __init__(self, game) -> None:
        self._game = game
        self.control_panel = pygame.sprite.Group()
        self._section = None
        self._render_menu()

    def _render_menu(self):
        self.control_panel = pygame.sprite.Group()
        menu = self._get_menu()
        width, _ = self._game.get_screen_size()
        start_point = width - 30 * len(menu.keys())
        for idx, (menu_key, menu_value) in enumerate(menu.items()):
            self.control_panel.add(
                MenuButton(
                    x=start_point + idx * 30,
                    y=10,
                    width=25,
                    height=25,
                    text=menu_key,
                    callback=menu_value["value"] if menu_value["type"] == "action" else self._set_section,
                    image_normal=menu_value["image"],
                )
            )

    def _set_section(self, menu_name):
        print(f'Setting section {menu_name}')
        self._section = menu_name
        self._render_menu()

    def show(self):
        self.control_panel.draw(self._game.get_screen())

    def handle_event(self, event: pygame.event.Event):
        for button in self.control_panel:
            button.handle_event(event)

    def _clear(self, *args, **kwargs):
        logger.debug("Syringe!")

    def _syringe(self, *args, **kwargs):
        logger.debug("Syringe!")

    def _back(self, *args, **kwargs):
        logger.debug("Going back!")
        self._set_section(None)

    def _feed(self, food: Food):
        logger.debug(f"Feeding with {food}!")
        self._game.feed_pet(FoodFactory.get_food_by_name(food))

    def _get_menu(self):
        menu = {
            "Food": {
                "type": "submenu",
                "image": pygame.image.load(os.path.join(self.CONTROLS_PATH, "buttons/fork_n_knife.jpg")),
                "value": {
                    "Milk": {
                        "type": "action",
                        "image": pygame.image.load(os.path.join(self.CONTROLS_PATH, "buttons/milk.png")),
                        "value": lambda t: self._feed(Food.MILK),
                    },
                    "Fish": {
                        "type": "action",
                        "image": pygame.image.load(os.path.join(self.CONTROLS_PATH, "buttons/fish.png")),
                        "value": lambda t: self._feed(Food.FISH),
                    },
                    "Apple": {
                        "type": "action",
                        "image": pygame.image.load(os.path.join(self.CONTROLS_PATH, "buttons/apple.png")),
                        "value": lambda t: self._feed(Food.APPLE),
                    },
                    "Back": {
                        "type": "action",
                        "image": pygame.image.load(os.path.join(self.CONTROLS_PATH, "buttons/back.png")),
                        "value": self._back,
                    },
                }
            },
            "Syringe": {
                "type": "action",
                "image": pygame.image.load(os.path.join(self.CONTROLS_PATH, "buttons/syringe.png")),
                "value": self._syringe
            },
            "Clear": {
                "type": "action",
                "image": pygame.image.load(os.path.join(self.CONTROLS_PATH, "buttons/scoop.png")),
                "value": self._clear
            }
        }
        return menu[self._section]["value"] if self._section in menu else menu
