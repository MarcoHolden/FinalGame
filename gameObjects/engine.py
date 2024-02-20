import pygame

from . import Drawable, Kirby
from .dragon import Dragon
from .bob import Bob

from utils import vec, RESOLUTION

class GameEngine(object):
    import pygame

    def __init__(self):       
        self.kirby = Kirby((0,0))
        self.kirby.image = pygame.transform.scale_by(self.kirby.image, 4.25)

        self.dragon = Dragon((0, 0))
        self.dragon.image = pygame.transform.scale_by(self.dragon.image, 0.10)

        self.bob = Bob((0,0))
        self.bob.image = pygame.transform.scale_by(self.bob.image, 0.20)

        self.size = vec(*RESOLUTION)
        self.background1 = Drawable((0,0), "background4.png")

    
    def draw(self, drawSurface):

        self.background1.draw(drawSurface)
        self.kirby.draw(drawSurface)
        self.dragon.draw(drawSurface)
        self.bob.draw(drawSurface)
            
    def handleEvent(self, event):
        self.kirby.handleEvent(event)
        self.dragon.handleEvent(event)
        self.bob.handleEvent(event)
    
    def update(self, seconds):
        self.kirby.update(seconds)

        self.dragon.update(seconds)
        self.bob.update(seconds)

        Drawable.updateOffset(self.kirby)
    

