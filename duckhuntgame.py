#This is the module which will hold game classes and their respective helping classes.

#Import the player classes.
from duckhuntplayers import *

#Import ducks
from ducks import *

#Import mycolors.
import mycolors

#import interface
from display import *



#Importing pygame.
import pygame, time

class Game:
	##==========================================================================
	##==========================================================================
	def __init__(self):

		#Create clock to manage fps.
		self.clock = pygame.time.Clock()
		#game states, True for current game state
		self.game_states = {"beginning": True, "modes": False, "in": False, "over": False, "quit": False}

		#Create info object for screen resolution and other info.
		self.info = pygame.display.Info()
		#set window
		self.window = pygame.display.set_mode((int(self.info.current_w*0.6),int(self.info.current_h*0.6)))
			#window size for convinience
		self.w = self.window.get_width()
		self.h = self.window.get_height()

		self.mode = None
	
	#Create the ducks for this game.
	#self.makeDucks(3)
		#Give this game a list of players to pick from.
		#self.players = {"P1": InteractivePlayer(), "R": Robot()}
		#self.player = self.players["P1"]
		#Ducks list.
		#self.ducks = []


	##==========================================================================
	##==========================================================================
	#switch game state, must turn off all other game states
	def switch_state(self, state):
		for i in self.game_states.keys():
			self.game_states[i] = False
		self.game_states[state] = True

	##==========================================================================
	##==========================================================================
	#Display beginning screen
	#Include: blue background, grass, "Duck Hunt", start game button, quit button
	def beginning_screen(self):
		self.window.fill(mycolors.LIGHT_BLUE)
		display = Display(self.window)
		display.draw_grass()
		display.text("Duck Hunt", int(self.h*0.2), mycolors.RED, 1, (self.h*0.8/2), True)
		display.draw_buttons("beginning")
		pygame.display.update()
		
	#Display game over screen
	#Include: blue background, grass, "Game Over"(text), start new game button, quit button
	def game_over_screen(self):
		self.window.fill(mycolors.LIGHT_BLUE)
		display = Display(self.window)
		display.draw_grass()
		display.text("Game Over", int(self.h*0.2), mycolors.RED, 1, (self.h*0.8/2), True)
		display.draw_buttons("over")
		pygame.display.update()
		
	#Display in game screen
	#Include: blue background, grass, "Duck: ", "Bullets: ", "Score: "
	def ingame_screen(self):
		self.window.fill(mycolors.LIGHT_BLUE)
		display = Display(self.window)
		display.draw_grass()
		display.text("Ducks:"  , int(self.h*0.1), mycolors.BLACK, int(self.w*0.1), int(self.h*0.85), False)
		display.text("Bullets:", int(self.h*0.1), mycolors.BLACK, int(self.w*0.4), int(self.h*0.85), False)
		display.text("Score:"  , int(self.h*0.1), mycolors.BLACK, int(self.w*0.7), int(self.h*0.85), False)
		pygame.display.update()
		
	#Display mode selection screen
	#Include: some instruction
	def mode_selection_screen(self):
		self.window.fill(mycolors.LIGHT_BLUE)
		display = Display(self.window)
		display.text("Press E for Easy Mode"	, int(self.h*0.1), mycolors.BLACK, 1, int(self.h*0.5), True)
		display.text("Press M for Medium Mode"  , int(self.h*0.1), mycolors.BLACK, 1, int(self.h*0.6), True)
		display.text("Press H for Hard Mode"	, int(self.h*0.1), mycolors.BLACK, 1, int(self.h*0.7), True)
		pygame.display.update()
		
	##==========================================================================
	##==========================================================================
	#Events handling
	#Possible events: quit, start&quit buttons
	def mouse_action_beginning(self):
				   
		#Go over events for event handling.
		for event in pygame.event.get():
  
			#Event handling to quit game.
			if(event.type == pygame.QUIT):
				self.switch_state("quit")
				
			#Mouse event handling.
			if event.type == pygame.MOUSEBUTTONDOWN:
				#mouse position
				cur = pygame.mouse.get_pos()
				
				#click start button
				if self.w*0.6 > cur[0] > self.w*0.4 and self.h*0.6 > cur[1] > self.h*0.5:
					self.switch_state("modes")
				
				#click quit button
				elif self.w*0.6 > cur[0] > self.w*0.4 and self.h*0.7 > cur[1] > self.h*0.6:
					self.switch_state("quit")
					
	#Possible events: quit, restart&quit buttons
	def mouse_action_game_over(self):
		
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				self.switch_state("quit")

			#Mouse event handling.
			if event.type == pygame.MOUSEBUTTONDOWN:
				#mouse position
				cur = pygame.mouse.get_pos()
				
				#click start new game button
				if self.w*0.6 > cur[0] > self.w*0.4 and self.h*0.6 > cur[1] > self.h*0.5:
					self.switch_state("modes")
				
				#click quit button
				elif self.w*0.6 > cur[0] > self.w*0.4 and self.h*0.7 > cur[1] > self.h*0.6:
					self.switch_state("quit")
				
	#Possible events: quit, shoot
	def mouse_action_ingame(self):
		
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				self.switch_state("quit")

			if event.type == pygame.MOUSEBUTTONDOWN:
				#mouse position
				cur = pygame.mouse.get_pos()
				
				#click start new game button
				if self.w*0.6 > cur[0] > self.w*0.4 and self.h*0.6 > cur[1] > self.h*0.5:
					self.switch_state("over")
	
	#Possible events: KEYS(E, H, M), quit
	def select_mode(self):
		
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				self.switch_state("quit")

			if event.type == pygame.KEYDOWN:
				
				if event.key == pygame.K_e:
					self.mode = "easy"
					self.switch_state("in")
					
				elif event.key == pygame.K_h:
					self.mode = "hard"
					self.switch_state("in")
					
				elif event.key == pygame.K_m:
					self.mode = "medium"
					self.switch_state("in")
	#==========================================================================
	##==========================================================================

	#initialize game
	def init(self):
		self.beginning_screen()
		
		#main game loop
		while(not self.game_states["quit"]):
			
			if self.game_states["beginning"] == True:
				while self.game_states["beginning"]:
					self.mouse_action_beginning()
				#beginning state ----> mode selection / quit game
				self.mode_selection_screen()

		
			elif self.game_states["modes"] == True:
				while self.game_states["modes"]:
					self.select_mode()
				#mode selection state ---> ingame state / quit game
				self.ingame_screen()


			
			elif self.game_states["in"] == True:
				while self.game_states["in"]:
					self.mouse_action_ingame()
				#in game state   ----> game over state / quit game
				self.game_over_screen()


			
			elif self.game_states["over"] == True:
				while self.game_states["over"]:
					self.mouse_action_game_over()
				#game over state ----> mode selection / quit game
				self.mode_selection_screen()
			


# self.render_Objects()
#pygame.display.update()

		
	#def checkDucksGone(self):
	##	if(len(self.ducks) <= 0):
	#		return True
	#	else:
	#		return False


		

	#update objects
	#def updateObjects(self):
	#	for duck in self.ducks:
	#		duck.move()




	#def makeDucks(self, how_many):
	#	for i in range(how_many):
	#		self.ducks.append(self.createDuck(self.window, "easy"))




	#def createDuck(self, window, typeDuck):
	
	#	if(typeDuck == "hard"):
	#		return Duck(window, 10)
	#	elif(typeDuck == "medium"):
	#		return  Duck(window, 7)
	#	else:
	#		return Duck(window, 5)
			

		#def quit(self): 
		#	return self.quit_game	



			
			
	 ##==========================================================================
	#def render_Objects(self):
	
	
	#	for duck in self.ducks:
	#		duck.beDrawn()
			
#		pygame.display.update()
		
#		self.clock.tick(20)



#	locationWhereShot = self.player.shotAt()
	#	isShot = self.check_hit_duck(locationWhereShot)


				#check if duck is shot
	#def check_hit_duck(self, location):
	
	#if self.window.get_at(location) == mycolors.YELLOW:
	###		return True
	#	else:
	#		return False
				
	##==========================================================================
			
