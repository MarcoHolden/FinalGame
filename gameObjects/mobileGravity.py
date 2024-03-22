from . import Mobile
from FSMs import GravityFSM, AccelerationFSM
from utils import vec, magnitude, scale

class MobileGravity(Mobile):
    def __init__(self, position, fileName=""):
        super().__init__(position, fileName)
        self.UD = GravityFSM(self)
        self.LR = AccelerationFSM(self)

    def update(self, seconds, colliders):
        super().update(seconds)
        self.UD.updateState()
        self.LR.updateState()

        if self.UD ==  "jumping":
            for items in colliders:
                if items.getCollisionRect().colliderect(self.getCollisionRect()):
                    print(items.getCollisionRect(), "/n", self.getCollisionRect())
                    rc = items.getCollisionRect().clip(self.getCollisionRect())
                    w = rc.width
                    h = rc.height
                    print("width", w)
                    print("height", h)
                    if h<w:
                        self.position[1] +=h
                        self.UD.jumpTimer = 0
                        self.UD.fall()
                    else:
                        if self.position[0] < items.getCollisionRect().left:
                            self.position[0] -= w
                        else:
                            self.position[0] +=w


        if self.UD == "falling":
            for item in colliders:
                if item.getCollisionRect().colliderect(self.getCollisionRect()):
                    print(item.getCollisionRect(), "/n", self.getCollisionRect())
                    rc = item.getCollisionRect().clip(self.getCollisionRect())
                    w = rc.width
                    h = rc.height
                    print("width", w)
                    print("height", h)
                    if h < w:
                        self.position[1] += h
                        self.UD.fall()
                    else:
                        if self.position[0] < item.getCollisionRect().left:
                            self.position[0] -= w
                        else:
                            self.position[0] += w

                if self.position[0] >= item.getCollisionRect()[0] and self.position[0] <= item.getCollisionRect()[0]+item.getSize()[0] and self.position[1] >= item.getCollisionRect()[1]-self.getSize()[1] and item.position[1] >= self.position[1]:
                    self.UD.land()
                    self.position[1] = item.getCollisionRect()[1]-self.getSize()[1]



            #if self.getCollisionRect()in colliders.