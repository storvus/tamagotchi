from typing import Dict

from entities.food._base import Food
from entities.pets._base import Base


class Herbivorous(Base):

    def get_food_multiplier(self, food: Food) -> Dict[str, int]:
        pass
