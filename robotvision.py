import pygame
import pygame.camera

class Robot_Vision:
  
  def __init__():
    
    init()
    
    camlist = list_cameras()
    
    if(camlist):
      cam = Camera(camlist[0], (640, 480))
    
