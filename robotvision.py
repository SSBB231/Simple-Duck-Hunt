import pygame
import pygame.camera

from pygame.locals import *

pygame.camera.init()

class RobotEye:
	
	def __init__(self):
		
		camlist = pygame.camera.list_cameras()
		
		self.cam = None
		
		if(camlist):
			self.cam = pygame.camera.Camera(camlist[0], (640, 480))
			
			self.cam.start()
			
			print(cam.get_controls())
			
	def get_vision(self):
		return self.cam.get_image()