#This module contains all duck classes.
#RGBA color definitions.
import mycolors
import pygame
class Duck:
	
	def __init__(self, window, mode):
		
		self.width = window.get_width()//10
		self.height = self.width
		
		self.x = 0
		self.y = window.get_height()*0.7
		
		self.x_speed = 0
		self.y_speed = 0
		self.img_duck = pygame.image.load("duck.png")
		self.img_duck = pygame.transform.scale(self.img_duck, (self.width,self.height))
		if(mode == "easy"):
			self.x_speed = 7
			self.y_speed = -3
		elif(mode == "medium"):
			self.x_speed = 15
			self.y_speed = -7
		elif(mode == "hard"):
			self.x_speed = 20
			self.y_speed = -10
			
		
		self.window = window
		
		self.color = mycolors.YELLOW
		
		self.dead = False
		
		self.visible = False
		
		self.wait_time = 20
		
	def is_dead(self):
		return self.dead
		
	def is_visible(self):
		return self.visible
		
	def set_visible(self, visible):
		self.visible = visible
		
	#draw duck  
	def beDrawn(self):
		if(self.visible):
			self.window.blit(self.img_duck, (self.x,self.y))
		
		
	def was_hit(self, location):
	
		if(location == None):
			pass
		else:
	
			x, y = location
		
			if((self.x-self.width//2 <= x <= self.x+self.width//2) and (self.y-self.height//2 <= y <= self.y+self.height//2)):
				return True
		
	#when duck dies
	def die(self):
		self.color = mycolors.RED
		self.dead = True
		self.change_x_speed(0)
		self.change_y_speed(20)
		
	#check if duck is on screen	
	def onScreen(self):
		width, height = self.window.get_size()		
		return True
			
	def move(self):
		self.x += self.x_speed
		self.y += self.y_speed
		
		if(self.dead and self.wait_time > 0):
			self.wait_time -= 1
			
		if(self.wait_time <= 0):
			self.visible = False
			
			
	def change_x_speed(self, speed):
		self.x_speed = speed
		
	def change_y_speed(self, speed):
		self.y_speed = speed
		
##=========================================================
