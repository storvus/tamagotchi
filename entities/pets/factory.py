from entities.pets._base import Base
from entities.pets.cat import Cat
from lib.constants import PetName


class PetFactory:

    def __init__(self, game) -> None:
        self.game = game

    def get_pet_by_name(self, pet_name: PetName) -> Base:
        if pet_name == PetName.CAT:
            return Cat(game=self.game)
        raise ValueError("Unexpected pet name")
