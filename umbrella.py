import pygame
import random
import math
from pygame.locals import RLEACCEL

from screen import Screen
from gameSprite import GameSprite


# Define the enemy object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite
class Umbrella(GameSprite):
    Max_Speed = 10
    Min_Speed = 5

    def __init__(self):
        super(Umbrella, self).__init__()
        self.surf = pygame.image.load("icons/umbrella.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0,Screen.width),
                random.randint(0, 0),
            )
        )
        self.speed = random.randint(self.Min_Speed, self.Max_Speed)
        self.time = 0

    # Move the Umbrella based on speed
    # Remove it when it passes the left edge of the screen.py
    def update(self):
        self.time += 1
        speed_x = 0.75 * self.speed \
                  * math.cos(2 * math.pi * self.time / (0.05 * Screen.width))
        speed_y = self.speed
        self.rect.move_ip(speed_x, speed_y)
        if  self.rect.bottom > Screen.height:
            print("paraiguas mort")
            self.kill()

    def clone(self):
        return Umbrella()
