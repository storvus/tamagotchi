from entities.food.apple import Apple
from entities.food.fish import Fish
from entities.food.milk import Milk
from lib.constants import Food
from entities.food._base import Food as FoodEntity


class FoodFactory:

    @staticmethod
    def get_food_by_name(name: Food) -> FoodEntity:
        if name == Food.APPLE:
            return Apple()
        if name == Food.FISH:
            return Fish()
        if name == Food.MILK:
            return Milk()
        raise ValueError("Unexpected food name")
