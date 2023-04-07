from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.rock import Rock
from dino_runner.utils.constants import BIRD, ROCK, SMALL_CACTUS
import pygame


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(500)
                    pygame.mixer.music.stop()
                    game.playing = False
                    game.death_count +=1
                    break

        if len(self.obstacles) == 0:
            self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(500)
                    pygame.mixer.music.stop()
                    game.playing = False
                    game.death_count +=1
                    break
                

        if len(self.obstacles) == 0:
            self.obstacles.append(Rock(ROCK))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(500)
                    pygame.mixer.music.stop()
                    game.playing = False
                    game.death_count +=1
                    break
        

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
