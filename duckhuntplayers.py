import pygame

#This module contains all the player classes and their respecsctive helper classes.
##====================================================
class Player(object):
	
	#Player class constructor
	def __init__(self, window):
		
		#Initializes score to zero.
		self.score = 0
		self.name = "P"
		
		self.num_bullets = 10
		
		self.window = window
		
		self.shot_img = pygame.image.load("shot.png")
	
	#Returns a 2-tuple with the location at which
	#the player shot at the screen.
	def shot_at(self, event):

		if(event != None):
			x, y = event.pos
			self.window.blit(self.shot_img, (x - 300//2, y - 300//2))
		self.num_bullets-=1

		return (0,0)
		
	def update_score(self, points):
		self.score += points
		
	def update(self):
		pass
		
	def getName(self):
		pass
		
	def get_num_bullets(self):
		return self.num_bullets
		
	def get_score(self):
		return self.score
		
	def clear_score(self):
		self.score = 0

	def move(self):
		pass

	def recover_stats(self, score, bullets):
		self.score = score
		self.bullets = bullets
		
	def set_bullets(self, bullets):
		self.num_bullets = bullets
	

##====================================================

##====================================================
class InteractivePlayer(Player):
	
	#Player class constructor
	def __init__(self, window):
		Player.__init__(self, window)
		self.name = "P1"
		
	#Returns a 2-tuple with the location at which
	#the player shot at the screen.
	def shot_at(self, event):
	
		Player.shot_at(self, event)

		return event.pos
		
	def update(self):
		pass
		
	def getName(self):
		return self.name

##====================================================

##====================================================
#Class that represents the robot that will play as this game's player.
class Robot(Player):
	
	def __init__(self, window, robot_eye):
		Player.__init__(self, window)
		self.name = "R"

		self.robot_eye = robot_eye

		self.wait_time = 25

		self.shot = False

		self.x = 0
		self.y = 0
		
	def shot_at(self, event):

		self.shot = True
		return Player.shot_at(self, None)
		
	def move(self):

		self.eye_x, self.eye_y = self.robot_eye.coord

		mouse_x, mouse_y = pygame.mouse.get_pos()

		dx = 0
		dy = 0

		#if(self.eye_x > mouse_x):
		#	dx = 5
		#elif(self.eye < mouse_x):
		#	dx = -5
		#else:
		#	dx = 0
		#if(mouse_y < self.eye_y):
		#	dy = 5
		#elif(mouse_y > self.eye_y):
		#	dy = -5
		#else:
		#	dy = 0

		dx = 0.15*(self.eye_x - mouse_x)
		dy = 0.15*(self.eye_y - mouse_y)

		self.x = mouse_x+dx
		self.y = mouse_y+dy

		pygame.mouse.set_pos((self.x, self.y))

		if(self.shot):
			self.wait_time-=1

		if(self.wait_time <= 0):
			self.wait_time = 25

	def get_location(self):

		return (self.x, self.y)
		
##====================================================
