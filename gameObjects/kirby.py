from . import Mobile
from FSMs import WalkingFSM, AccelerationFSM
from utils import vec, RESOLUTION

from pygame.locals import *

import pygame
import numpy as np
from gameObjects import Drawable


class Kirby(Mobile):
   def __init__(self, position):
      super().__init__(position, "kirby.png")

      self.hatOffset = vec(-3,-5)
      self.hat = Drawable(position, "hat.png")
      self.hat.image = pygame.transform.flip(self.hat.image, True, False)
        
      # Animation variables specific to Kirby
      self.framesPerSecond = 2 
      self.nFrames = 2
      
      self.nFramesList = {
         "moving"   : 4,
         "standing" : 2
      }
      
      self.rowList = {
         "moving"   : 1,
         "standing" : 0
      }
      
      self.framesPerSecondList = {
         "moving"   : 8,
         "standing" : 2
      }
            
      self.FSManimated = WalkingFSM(self)
      self.LR = AccelerationFSM(self, axis=0)
      self.UD = AccelerationFSM(self, axis=1)
      
      
   def handleEvent(self, event):
      if event.type == KEYDOWN:
         if event.key == K_UP:
            self.UD.decrease()
             
         elif event.key == K_DOWN:
            self.UD.increase()
            
         elif event.key == K_LEFT:
            self.LR.decrease()
            
         elif event.key == K_RIGHT:
            self.LR.increase()
            
      elif event.type == KEYUP:
         if event.key == K_UP:
            self.UD.stop_decrease()
             
         elif event.key == K_DOWN:
            self.UD.stop_increase()


            
         elif event.key == K_LEFT:
            self.LR.stop_decrease()
            
         elif event.key == K_RIGHT:
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
   
  
