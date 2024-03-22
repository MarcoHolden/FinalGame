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
        self.earths = [self.earth1, self.earth2, self.earth3, self.earth4, self.earth5, self.earth6]
        self.square = Drawable((144, 710), "square2.png")
        self.square1 = Drawable((156, 710), "square2.png")
        self.square2 = Drawable((168, 710), "square2.png")
        self.square3 = Drawable((180, 710), "square2.png")
        self.square4 = Drawable((500, 715), "square2.png")
        self.square5 = Drawable((100, 715), "square2.png")
        self.square6 = Drawable((400, 715), "square2.png")
        self.square7 = Drawable((300, 715), "square2.png")
        self.square8 = Drawable((100, 470), "square2.png")
        self.squares = [self.square, self.square1, self.square2, self.square3, self.square4, self.square5, self.square6, self.square7, self.square8]
        self.arrow = Drawable((50, 773), "arrow3.png")
        self.kirbyColliders = [self.square, self.square1, self.square2, self.square3, self.square4, self.square5, self.square6, self.square7, self.square8, self.earth1, self.earth2, self.earth3, self.earth4, self.earth5, self.earth6]

    def draw(self, drawSurface):
        self.background0.draw(drawSurface)
        self.background4.draw(drawSurface)
        self.background3.draw(drawSurface)
        self.background1.draw(drawSurface)
        for i in self.kirbyColliders:
            i.draw(drawSurface)
        self.arrow.draw(drawSurface)
        self.kirby.draw(drawSurface)
        self.dragon.draw(drawSurface)
        self.bob.draw(drawSurface)

            
    def handleEvent(self, event):
        self.kirby.handleEvent(event)
        self.dragon.handleEvent(event)
        self.bob.handleEvent(event)
    
    def update(self, seconds):
        self.kirby.update(seconds, self.kirbyColliders)

        self.dragon.update(seconds)
        self.bob.update(seconds)

        Drawable.updateOffset(self.kirby)
    

