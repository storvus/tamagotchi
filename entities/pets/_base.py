import abc
import os
import time
from itertools import cycle
from typing import List, Dict

from pygame import Surface

from config import RESOURCES_DIR
from entities.base import GameEntity
from entities.food._base import Food
from entities.pets.constants import PetState


# ToDo: predator or herbivorous (multiplier)
class Base(GameEntity):
    PETS_PATH = os.path.join(RESOURCES_DIR, "pets")
    DEFAULT_TIMER_SECONDS = 1

    def __init__(self, game) -> None:
        super().__init__(game)
        self.alive = True
        self._is_going_to_dead = False
        self.screen = self._game.get_screen()
        self._pet_images = self.image_collections()
        self._image_iterator = None
        self._current_image = None
        self._update_state(PetState.NORMAL)
        self._timer = time.time() + self.DEFAULT_TIMER_SECONDS

    def _configure_image_iterator(self):
        width, height = self._game.get_screen_size()
        self._pet_rect = self._pet_images[self._state][0].get_rect()
        self._pet_rect.midtop = width / 2, height / 4
        self._image_iterator = cycle(iter(self._pet_images[self._state]))

    def _update_state(self, new_state):
        self._state = new_state
        self._configure_image_iterator()

    def _update(self):
        if not self._current_image or time.time() >= self._timer:
            self._timer = time.time() + self.DEFAULT_TIMER_SECONDS
            self._current_image = next(self._image_iterator)
            if self._state == PetState.DEAD and self.alive:
                self.alive = False

    @abc.abstractmethod
    def image_collections(self) -> Dict[str, List[Surface]]:
        pass

    @abc.abstractmethod
    def get_food_multiplier(self, food: Food) -> int:
        pass

    def die(self):
        self._update_state(PetState.DEAD)

    def is_dead(self) -> bool:
        return not self.alive

    def eat(self, food: Food):
        multiplier = self.get_food_multiplier(food)
        self._game.decrease_hunger_level(multiplier * food.satiety_level)
        self._game.shit_expected(1)

    def show(self):
        if self._game.is_critical_level() and self._state not in (PetState.CRITICAL, PetState.DEAD):
            self._update_state(PetState.CRITICAL)
        elif not self._game.is_critical_level() and self._state == PetState.CRITICAL:
            self._update_state(PetState.NORMAL)
        # show the pet in the center of the screen
        self._update()
        self.screen.blit(self._current_image, self._pet_rect)
