#This module contains all duck classes.
#RGBA color definitions.
import mycolors

class Duck:
	
	def __init__(self, window, speed, pos):
		self.x, self.y = pos
		
		self.width = window.get_width()//10
		self.height = self.width
		
		self.x_speed = speed
		self.y_speed = 0
		
		self.window = window
		
		self.color = mycolors.YELLOW
		
		self.dead = False
		
		self.visible = True
		
		self.wait_time = 20
		
	def is_dead(self):
		return self.dead
		
	def is_visible(self):
		return self.visible
		
	#draw duck  
	def beDrawn(self):
		if(self.visible):
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