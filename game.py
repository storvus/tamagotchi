from pygame.event import Event

from entities.controls import PetControl
from entities.food._base import Food
from entities.stats.health import Health
from entities.stats.hunger import Hunger
from entities.pets.factory import PetFactory
from entities.statistic import Statistic
from entities.stats.shit import Shit
from lib.constants import PetName


class Game:

    def __init__(self, screen, pet_name=PetName.CAT):
        self._is_pet_dead = False
        self._screen = screen
        self._width, self._height = screen.get_size()

        # stats
        self._hunger = Hunger(game=self)
        self._shit = Shit(game=self)
        self._stats = [self._hunger, self._shit]

        # entities
        self._pet = PetFactory(game=self).get_pet_by_name(pet_name)
        self._health = Health(game=self)

        self._statistic = Statistic(game=self)
        self._menu = PetControl(game=self)

    def display(self):
        self._menu.show()
        for stat in self._stats:
            stat.update()

        harm_level = self._get_harm_level()
        self._health.set_harm_level(harm_level)
        self._health.update()

        self._pet.show()
        self._statistic.show()

    # health block
    def get_health_level(self) -> int:
        return self._health.get_current_level()

    def get_max_health_level(self) -> int:
        return self._health.get_max_level()

    def is_harm_received(self) -> bool:
        return self._get_harm_level() > 0

    def is_health_critical(self) -> bool:
        return self._health.is_critical_level()

    # hunger
    def decrease_hunger_level(self, value: int):
        self._hunger.decrease_level(value)

    def get_hunger_level(self) -> int:
        return self._hunger.get_current_level()

    def is_hunger_critical(self) -> bool:
        return self._hunger.is_critical_level()

    def get_max_hunger_level(self) -> int:
        return self._hunger.get_max_level()

    # shit
    def shit_expected(self, value: int):
        self._shit.add_expected_shit(value)

    # pet
    def feed_pet(self, food: Food):
        self._pet.eat(food)

    def kill_pet(self):
        self._pet.die()

    def is_over(self):
        return self._pet.is_dead()

    def get_screen(self):
        return self._screen

    def get_screen_size(self):
        return self._width, self._height

    def handle_event(self, event: Event):
        self._menu.handle_event(event)

    def _get_harm_level(self) -> int:
        return sum([stat.get_harm_level() for stat in self._stats])

    def is_critical_level(self):
        return any([stat.is_critical_level() for stat in self._stats])
