from os.path import join
from typing import Dict, List

import pygame

from entities.food._base import Food
from entities.pets._base import Base


class Cat(Base):

    def get_food_multiplier(self, food: Food) -> int:
        return 1

    def image_collections(self) -> Dict[str, List[pygame.Surface]]:
        return {
            "normal": [
                pygame.image.load(join(self.PETS_PATH, "cat/frame_0_delay-0.8s.jpeg")),
                pygame.image.load(join(self.PETS_PATH, "cat/frame_1_delay-0.8s.jpeg")),
            ],
            "critical": [
                pygame.image.load(join(self.PETS_PATH, "cat/frame_2_delay-0.8s.jpeg")),
                pygame.image.load(join(self.PETS_PATH, "cat/frame_3_delay-0.8s.jpeg")),
            ],
            "dead": [
                pygame.image.load(join(self.PETS_PATH, "cat/frame_4_delay-0.8s.jpeg")),
            ]
        }
