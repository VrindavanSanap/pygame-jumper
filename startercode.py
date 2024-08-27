#!/usr/bin/python3

from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform
from blob import Blob
RED = (200, 0, 0)
class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))
        self.blob = Blob(self.w, self.h)

    def update(self):
        self.blob.update()

    def keyDown(self, key):
        if (key== 32):
            print("jump")

    def keyUp(self, key):
        pass

    def mouseUp(self, button, pos):
        pass  
        
    def mouseMotion(self, buttons, pos, rel):
        pass
        
    def draw(self):
        self.screen.fill((255,255,255))
        pygame.draw.rect(self.screen, self.blob.color, (self.blob.get_coords(), self.blob.get_dims()))

s = Starter()
s.mainLoop(40)
