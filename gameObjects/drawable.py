from utils import SpriteManager, SCALE, RESOLUTION, vec, WORLD_SIZE

import pygame

class Drawable(object):
    
    OFFSET = vec(0,0)
    
    @classmethod
    def updateOffset(cls, trackingObj):
        Drawable.OFFSET = trackingObj.position + trackingObj.getSize() // 2 - RESOLUTION // 2

        Drawable.OFFSET[0] = int(max(0, min(Drawable.OFFSET[0],
                                            WORLD_SIZE[0] - RESOLUTION[0])))

        Drawable.OFFSET[1] = int(max(0, min(Drawable.OFFSET[1],
                                            WORLD_SIZE[1] - RESOLUTION[1])))
        
        

    @classmethod    
    def translateMousePosition(cls, mousePos):
        newPos = vec(*mousePos)
        newPos /= SCALE
        newPos += cls.OFFSET
        
        return newPos
    
    def __init__(self, position=vec(0,0), fileName="", offset=None):
        if fileName != "":
            self.image = SpriteManager.getInstance().getSprite(fileName, offset)
        
        self.position  = vec(*position)
        self.imageName = fileName
        self.flipImage = [False, False]
    
    def draw(self, drawSurface):
        blitImage = self.image

        if self.flipImage[0] or self.flipImage[1]:
            blitImage = pygame.transform.flip(self.image, *self.flipImage)

        drawSurface.blit(blitImage, list(map(int, self.position - Drawable.OFFSET)))
            
    def getSize(self):
        return vec(*self.image.get_size())
    
    def handleEvent(self, event):
        pass
    
    def update(self, seconds):
        pass
    
    
    def getCollisionRect(self):
        newRect = self.image.get_rect()
        newRect.left = int(self.position[0])
        newRect.top = int(self.position[1])
        return newRect
    
    def doesCollide(self, other):
        return self.getCollisionRect().colliderect(other.getCollisionRect())   
    
    def doesCollideList(self, others):
        rects = [r.getCollisionRect() for r in others]
        return self.getCollisionRect().collidelist(rects)   