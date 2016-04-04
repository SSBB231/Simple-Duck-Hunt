#This module contains all duck classes.
#RGBA color definitions.
import mycolors

class Duck:
	
	def __init__(self, window, speed, pos):
		self.x, self.y = pos
		
		self.width = window.get_width()//10
		self.height = self.width
		
		self.speed = speed
		
		self.window = window
		
		self.color = mycolors.YELLOW
		
	#draw duck  
	def beDrawn(self):
		self.window.fill(self.color, rect = [self.x-self.width//2, self.y-self.height//2, self.width, self.height])
		
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
		
	#check if duck is on screen	
	def onScreen(self):
		width, height = self.window.get_size()		
		return True
			
	
		
	def move(self):
		self.x += self.speed
		
	def changeSpeed(self, speed):
		self.speed = speed
		
##=========================================================