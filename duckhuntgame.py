#This is the module which will hold game classes and their respective helping classes.

#Import the player classes.
from duckhuntplayers import *

#Import ducks
from ducks import *

#Import mycolors.
import mycolors

#Importing pygame.
import pygame

class Game:
	
	def __init__(self):
	
		#Give this game a list of players to pick from.
		self.players = {"P1": InteractivePlayer(), "R": Robot()}
		self.player = self.players["P1"]
		
		#Create clock to manage fps.
		self.clock = pygame.time.Clock()
		#Create info object for screen resolution and other info.
		self.info = pygame.display.Info()
		
		#Ducks list.
		self.ducks = []
		
		#Background Color
		self.color = mycolors.LIGHT_BLUE
		
		#Flag to keep game going.
		self.end = False
		
		#Window for displaying stuff.
		self.window = pygame.display.set_mode((self.info.current_w, self.info.current_h))
		
		#Create the ducks for this game.
		self.makeDucks(5)
	
	def makeDucks(self, how_many):
		for i in range(how_many):
			self.ducks.append(self.createDuck(self.window, "easy", (0, i*150+100)))
	
	def render_Objects(self):
	
		#Fill the window with the given color.
		self.window.fill(self.color)
	
		#This draws the ducks.
		for duck in self.ducks:
			duck.beDrawn()
			
			
		#This updates the entire display.
		pygame.display.update()
		
		#This will maintain 20 fps rate.
		self.clock.tick(20)
		
	def change_background(self, color):
		self.color = color
	
	
	#receiving shotting location from Player
	def handle_inputs(self):
	
		hit = False
		locationWhereShot = None
	
		#Go over events for event handling.
		for event in pygame.event.get():
		
			#Event handling to quit game.
			if(event.type == pygame.QUIT):
				self.end = True
				
			if(self.player == self.players["R"]):
				locationWhereShot = self.player.shotAt()
				hit = self.check_hit_duck(locationWhereShot)
			else:
				if(event.type == pygame.MOUSEBUTTONDOWN):
					locationWhereShot = self.player.shotAt(event)
					hit = self.check_hit_duck(locationWhereShot)
				
			#Check for Key Events.	
			if(event.type == pygame.KEYDOWN):
				
				#Check if key was B
				if(event.key == pygame.K_b):
					if(self.color == mycolors.LIGHT_BLUE):
						self.change_background(mycolors.BLACK)
					else:
						self.change_background(mycolors.LIGHT_BLUE)
		
		if(hit):
			for i in range(len(self.ducks)):
				duck = self.ducks[i]
				if(duck.was_hit(locationWhereShot)):
					duck.die()
					
		
					
		
		
	#check if duck is shot
	def check_hit_duck(self, location):
	
		if(location == None):
			pass
		else:
			if self.window.get_at(location) == mycolors.YELLOW:
				return True
			else:
				return False
			
	#update objects	
	def update_objects(self):
		for duck in self.ducks:
			duck.move()
			
	#Starts the game loop  
	def start(self):
	
		while(not self.quit()):

			self.handle_inputs()

			self.update_objects()

			self.render_Objects()

		
	def checkDucksGone(self):
		if(len(self.ducks) <= 0):
			return True
		else:
			return False
		
		
	def quit(self): 
		return self.end
		
	def createDuck(self, window, typeDuck, pos):
	
		if(typeDuck == "hard"):
			return Duck(window, 10 ,pos)
		elif(typeDuck == "medium"):
			return  Duck(window, 7, pos)
		else:
			return Duck(window, 5, pos)
			
			
			
			
			
			
