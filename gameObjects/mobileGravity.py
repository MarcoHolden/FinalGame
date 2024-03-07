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


        if self.UD == "falling":
            for item in colliders:
                print(self.position)
                if self.position[0] >= item.getCollisionRect()[0] and self.position[0] <= item.getCollisionRect()[0]+513 and self.position[1] >= item.getCollisionRect()[1]-self.getSize()[1]:
                    self.UD.land()
                    self.position[1] = item.getCollisionRect()[1]-self.getSize()[1]



            #if self.getCollisionRect()in colliders.