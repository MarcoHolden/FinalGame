from . import Mobile
from FSMs import WalkingFSM, AccelerationFSM
from utils import vec, RESOLUTION

from pygame.locals import *

import pygame
import numpy as np
from gameObjects import Drawable


class Bob(Mobile):
    def __init__(self, position):
        super().__init__(position, "bob.png")

        self.hatOffset = vec(-3, -5)
        self.hat = Drawable(position, "hat.png")
        self.hat.image = pygame.transform.flip(self.hat.image, True, False)
        self.LR = AccelerationFSM(self, axis=0)
        self.UD = AccelerationFSM(self, axis=1)

    def handleEvent(self, event):
        if event.type == KEYDOWN:
            if event.key == K_f:
                self.UD.decrease()

            elif event.key == K_j:
                self.UD.increase()

            elif event.key == K_v:
                self.LR.decrease()

            elif event.key == K_n:
                self.LR.increase()

        elif event.type == KEYUP:
            if event.key == K_f:
                self.UD.stop_decrease()

            elif event.key == K_j:
                self.UD.stop_increase()



            elif event.key == K_v:
                self.LR.stop_decrease()

            elif event.key == K_n:
                self.LR.stop_increase()

    def update(self, seconds):
        self.LR.update(seconds)
        self.UD.update(seconds)

        super().update(seconds)

        self.hat.position = self.hatOffset + self.position

    def draw(self, drawSurface):
        super().draw(drawSurface)
        self.hat.draw(drawSurface)

    def updateMovement(self):
        pass