import pygame
from minigames.mirrors.entities.blaster import Blaster
import random


class BlasterBase:
    SCALE = 8

    def __init__(self, game, num_players):
        self.game = game
        self.blasters = []
        self.gfx = pygame.image.load("minigames/mirrors/images/blaster_base.png")
        self.gfx = pygame.transform.scale(self.gfx, (self.gfx.get_width() * BlasterBase.SCALE, self.gfx.get_height() * BlasterBase.SCALE)).convert_alpha()

        for player in range(0, num_players):
            self.blasters.append(Blaster(self.game, player))

    def get_points(self, mirrors):
        # If two bullets collide with a single mirror,
        # check for collisions with a shuffled list of
        # blasters (to try and make it fairer...)
        blasters = sorted(self.blasters, key=lambda *args: random.random())

        for blaster in blasters:
            for bullet in blaster.bullets:
                for mirror in mirrors:
                    if bullet.collides_with(mirror):
                        mirror.destroy()
                        yield blaster.player

    def display(self, screen):
        b = self.blasters[:]
        random.shuffle(b)

        while len(b) > 0:
            b.pop().display(screen)

        screen.blit(self.gfx, ((screen.get_width() / 2) - (self.gfx.get_width() / 2), (screen.get_height() / 2) - (self.gfx.get_height() / 2)))