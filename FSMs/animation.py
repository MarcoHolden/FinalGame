from . import AbstractGameFSM
from utils import magnitude, EPSILON, SpriteManager

from statemachine import State

class AnimateFSM(AbstractGameFSM):
    """For anything that animates. Adds behavior on
       transitioning into a state to change animation."""
    def on_enter_state(self):
        state = self.current_state.id
        if self.obj.row != self.obj.rowList[state]:
            self.obj.nFrames = self.obj.nFramesList[state]
            self.obj.frame = 0
            self.obj.row = self.obj.rowList[state]
            self.obj.framesPerSecond = self.obj.framesPerSecondList[state]
            self.obj.animationTimer = 0
            self.obj.image = SpriteManager.getInstance().getSprite(self.obj.imageName,
                                                                   (self.obj.frame, self.obj.row))
         
        
class WalkingFSM(AnimateFSM):
    """Two-state FSM for walking / stopping in
       a top-down environment."""
       
    standing = State(initial=True)
    moving   = State()
    
    move = standing.to(moving)
    stop = moving.to(standing)
        
    
    def updateState(self):
        if self.hasVelocity() and self != "moving":
            self.move()
        elif not self.hasVelocity() and self != "standing":
            self.stop()
    
    def hasVelocity(self):
        return magnitude(self.obj.velocity) > EPSILON
    
    def noVelocity(self):
        return not self.hasVelocity()
class JumpingFSM(AnimateFSM):
    standing = State(initial=True)
    moving = State()
    falling = State()
    jumping = State()

    move = standing.to(moving)
    stop = moving.to(standing)
    jump = standing.to(jumping) | moving.to(jumping) | \
           falling.to.itself(internal=True)
    fall = standing.to(falling) | moving.to(falling) | jumping.to(falling)

    land = falling.to(moving, cond="hasVelocity") | \
           falling.to(standing, cond="noVelocity") | \
           jumping.to(moving, cond="hasVelocity") | \
           jumping.to(standing, cond="noVelocity")

    def hasVelocity(self):
        return magnitude(self.obj.velocity) > EPSILON

    def noVelocity(self):
        return not self.hasVelocity()

    def isFalling(self):
        return self.obj.velocity[1] > EPSILON

    def isJumping(self):
        return self.obj.velocity[1] < -EPSILON

    def isGrounded(self):
        return not self.isFalling() and not self.isJumping()

    def updateState(self):
        if self.isJumping() and self != "jumping":
            self.jump()
        elif self.isFalling() and self != "falling":
            self.fall()
        elif self.isGrounding() and self not in ["standing", "moving"]:
            self.land()
        elif self.hasVelocity() and self not in ["moving", "falling", "jumping"]:
            self.move()
        elif self.noVelocity() and self not in ["standing", "falling", "jumping"]:
            self.stop()