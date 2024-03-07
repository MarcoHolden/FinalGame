from . import AbstractGameFSM
from utils import vec, magnitude, EPSILON, scale, RESOLUTION
from FSMs import AnimateFSM
from statemachine import State

class MovementFSM(AbstractGameFSM):
    
    def __init__(self, obj):
        super().__init__(obj)
    
    def update(self, seconds):
        super().update(seconds)

        if self.obj.position[0] < 0:
            self.obj.velocity[0] = max(self.obj.velocity[0], 0)
        elif self.obj.position[0] > 2100 - self.obj.getSize()[0]:
            self.obj.velocity[0] = min(self.obj.velocity[0],0)

        


class AccelerationFSM(MovementFSM):
    """Axis-based acceleration with gradual stopping."""
    not_moving = State(initial=True)
    
    negative = State()
    positive = State()
    
    stalemate = State()
    
    decrease  = not_moving.to(negative) | positive.to(stalemate) | negative.to.itself(internal = True)
    
    increase = not_moving.to(positive) | negative.to(stalemate) | positive.to.itself(internal = True)
    
    stop_decrease = negative.to(not_moving) | stalemate.to(positive) | positive.to.itself(internal = True)
    
    stop_increase = positive.to(not_moving) | stalemate.to(negative) | negative.to.itself(internal = True)
    
    stop_all      = not_moving.to.itself(internal=True) | negative.to(not_moving) | \
                    positive.to(not_moving) | stalemate.to(not_moving)
    
    def __init__(self, obj, axis=0):
        self.axis      = axis
        self.direction = vec(0,0)
        self.direction[self.axis] = 1
        self.accel = 200
        
        super().__init__(obj)

    def update(self, seconds=0):
        if self == "positive":
            self.obj.velocity += self.direction * self.accel * seconds
        elif self == "negative":
            self.obj.velocity -= self.direction * self.accel * seconds
                
        elif self == "stalemate":
            pass
        else:
            if self.obj.velocity[self.axis] > self.accel * seconds:
                self.obj.velocity[self.axis] -= self.accel * seconds
            elif self.obj.velocity[self.axis] < -self.accel * seconds:
                self.obj.velocity[self.axis] += self.accel * seconds
            else:
                self.obj.velocity[self.axis] = 0
        
        
    
        super().update(seconds)

class GravityFSM(AbstractGameFSM):
    grounded = State(initial=True)
    jumping = State()
    falling = State()

    jump = grounded.to(jumping) | falling.to.itself(internal=True)
    fall = jumping.to(falling) | grounded.to(falling)
    land = falling.to(grounded) | jumping.to(grounded)

    stop_jump = jumping.to(falling) | jumping.to(grounded)

    def __init__(self, obj):
        super().__init__(obj)
        self.jumpTimer = 0
        self.gravity = 200
        self.jumpSpeed = 100
        self.jumpTime = 0.2



    def updateState(self):
        if self.canFall() and self == "jumping":
            self.fall()

    def canFall(self):
        return self.jumpTimer < 0

    def on_enter_jumping(self):
        self.jumpTimer = self.jumpTime

    def update(self, seconds=0):
        if self == "falling":
            self.obj.velocity[1] += self.gravity * seconds
        elif self == "jumping":
            self.obj.velocity[1] = -self.jumpSpeed
        else:
            self.obj.velocity[1] = 0
        super().update(seconds)

