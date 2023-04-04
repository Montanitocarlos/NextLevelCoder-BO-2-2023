
from dino_runner.components.obstacles.obstacle import Obstacle
import random


class Rock(Obstacle):

    def __init__(self, image_list):
        super().__init__(image_list)
        self.rect.y = 355