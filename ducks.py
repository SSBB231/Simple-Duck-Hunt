#This module contains all duck classes.
#RGBA color definitions.
import mycolors
import pygame
class Duck:

	def __init__(self, window, mode, x_pos):
		self.window = window
		#duck info
		self.width = window.get_width()//10
		self.height = self.width
		self.x = x_pos
		self.y = window.get_height()*0.7
		self.dead = False
		self.visible = True
		#initialize x and y speed according to mode
		self.x_speed = 0
		self.y_speed = 0
		if(mode == "easy"):
			self.x_speed = 10
			self.y_speed = -5
		elif(mode == "medium"):
			self.x_speed = 18
			self.y_speed = -8
		elif(mode == "hard"):
			self.x_speed = 25
			self.y_speed = -11
		#load and resize images
		up = pygame.image.load("up.gif")
		up = pygame.transform.scale(up, (self.width,self.height))
		down = pygame.image.load("down.gif")
		down = pygame.transform.scale(down, (self.width,self.height))
		flipped_up = pygame.image.load("flipped_up.png")
		flipped_up = pygame.transform.scale(flipped_up, (self.width,self.height))
		flipped_down = pygame.image.load("flipped_down.gif")
		flipped_down = pygame.transform.scale(flipped_down, (self.width,self.height))
		deadimg = pygame.image.load("dead.png")
		deadimg = pygame.transform.scale(deadimg, (self.width,self.height))
		self.images = {"up": up, "down": down, "f_up":flipped_up, "f_down": flipped_down, "dead": deadimg}
		self.img_duck = self.images["up"]
		#timers
		self.round_timer = 100
		#self.wait_time = 20

##=============================================================================
	def is_dead(self):
		return self.dead

	#def is_visible(self):
	#	return self.visible

	def is_hit(self, location):
		if(location == None):
			return False
		else:
			x, y = location
			print(location, (self.x, self.y), (self.width, self.height))
			if((self.x-self.width//2 <= x <= self.x+self.width//2) and (self.y-self.height//2 <= y <= self.y+self.height//2)):
				return True
			else:
				return False
	#check if duck is on screen
	def on_screen(self):
		width, height = self.window.get_size()
		if((-self.width//2 < self.x < width+self.width//2) and (-self.height//2 < self.y < height*0.85)):
			return True
		else:
			return False

##=============================================================================
	#draw duck
	def beDrawn(self):
		#if(self.`visible`):
		self.window.blit(self.img_duck, (self.x-self.width//2,self.y-self.height//2))

	def change_x_speed(self, speed):
		self.x_speed = speed

	def change_y_speed(self, speed):
		self.y_speed = speed

	def change_image(self, name):
		self.img_duck = self.images[name]

	def change_animation(self):
		if self.x_speed > 0:
			if self.img_duck != self.images["up"]:
				self.change_image("up")
			else:
				self.change_image("down")
		else:
			if self.img_duck != self.images["f_up"]:
				self.change_image("f_up")
			else:
				self.change_image("f_down")

	#change x & y speed to stay on screen
	def stay_on_screen(self):
		w, h = self.window.get_size()
		if self.y < self.height:
			self.y_speed *= -1
		if self.x < self.width:
			self.x_speed *= -1
		if self.x > (w-self.width):
			self.x_speed *= -1
		if self.y > h*0.7:
			self.y_speed *= -1

	def move(self):
		if((self.round_timer >= 0) and (not self.is_dead())):
			self.stay_on_screen()
		elif self.is_dead():
			self.change_x_speed(0)
			self.change_y_speed(20)
		else:
			self.change_x_speed(10)
			self.change_y_speed(-50)
		self.x += self.x_speed
		self.y += self.y_speed
		self.round_timer -= 1
		#if(self.dead and self.wait_time > 0):
		#	self.wait_time -= 1
		if(not self.dead):
			self.change_animation()

	#when duck dies
	def die(self):
		print("Calling Die")
		self.change_image("dead")
		self.dead = True

#		if(self.dead and self.wait_time > 0):
#			self.wait_time -= 1
#
#		if(self.wait_time <= 0):
#			self.visible = False



##=========================================================
