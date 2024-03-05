import pygame

from . import Drawable, Kirby
from .dragon import Dragon
from .bob import Bob

from utils import vec, RESOLUTION

class GameEngine(object):
    import pygame

    def __init__(self):       
        self.kirby = Kirby((0,774))
        self.dragon = Dragon((0, 0))
        self.bob = Bob((0,0))
        self.size = vec(*RESOLUTION)
        self.background0 = Drawable((0, 0), "background0.png")
        self.background0.image = pygame.transform.scale_by(self.background0.image, (6, 8))
        self.background1 = Drawable((0, 0), "background1.png")
        self.background3 = Drawable((0, 0), "background3.png")
        self.background4 = Drawable((0,0), "background4.png")
        self.earth1 = Drawable((0, 790), "earth2.png")
        self.earth2 = Drawable((513, 790), "earth2.png")
        self.earth3 = Drawable((1026, 790), "earth2.png")
        self.earth4 = Drawable((1539, 790), "earth2.png")
        self.earth5 = Drawable((1410, 590), "earth2.png")
        self.earth6 = Drawable((1923, 590), "earth2.png")
    def draw(self, drawSurface):
        self.background0.draw(drawSurface)
        self.background4.draw(drawSurface)
        self.background3.draw(drawSurface)
        self.background1.draw(drawSurface)
        self.earth1.draw(drawSurface)
        self.earth2.draw(drawSurface)
        self.earth3.draw(drawSurface)
        self.earth4.draw(drawSurface)
        self.earth5.draw(drawSurface)
        self.earth6.draw(drawSurface)
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
    

