from . import MobileGravity
from FSMs import JumpingFSM, AccelerationFSM, GravityFSM
from utils import vec, RESOLUTION
from UI.soundManager import SoundManager

from pygame.locals import *

import pygame
import numpy as np
from gameObjects import Drawable


class Kirby(MobileGravity):
   def __init__(self, position):
      super().__init__(position, "kirby.png")

      self.hatOffset = vec(-3,-5)
      self.hat = Drawable(position, "hat.png")
      self.hat.image = pygame.transform.flip(self.hat.image, True, False)
        
      # Animation variables specific to Kirby
      self.framesPerSecond = 2 
      self.nFrames = 2
      
      self.nFramesList = {
         "falling" : 4,
         "jumping" : 1,
         "moving"   : 4,
         "standing" : 2
      }
      
      self.rowList = {
         "falling" : 3,
         "jumping" : 2,
         "moving"   : 1,
         "standing" : 0
      }
      
      self.framesPerSecondList = {
         "falling" : 8,
         "jumping" : 3,
         "moving"   : 8,
         "standing" : 2
      }
            
      self.FSManimated = JumpingFSM(self)
      self.LR = AccelerationFSM(self, axis=0)
      self.UD = GravityFSM(self)
      
      
   def handleEvent(self, event):
      if event.type == KEYDOWN:
         if event.key == K_UP:
            sm = SoundManager.getInstance()
            ch = sm.playSFX("soundeffect1.wav")
            self.UD.jump()
             
         elif event.key == K_DOWN:
            #self.UD.increase()
            pass
            
         elif event.key == K_LEFT:
            self.LR.decrease()
            
         elif event.key == K_RIGHT:
            self.LR.increase()
            
      elif event.type == KEYUP:
         if event.key == K_UP:
            self.UD.stop_jump()
             
         elif event.key == K_DOWN:
            #self.UD.stop_increase()
            pass

            
         elif event.key == K_LEFT:
            self.LR.stop_decrease()
            
         elif event.key == K_RIGHT:
            self.LR.stop_increase()
   
   def update(self, seconds, colliders):
      self.LR.update(seconds)
      self.UD.update(seconds)
      
      super().update(seconds, colliders)

      self.hat.position = self.hatOffset + self.position

   def draw(self, drawSurface):
      super().draw(drawSurface)
      self.hat.draw(drawSurface)

   def updateMovement(self):
      pass
   
  
