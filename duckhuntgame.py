#This is the module which will hold game classes and their respective helping classes.

#Import the player classes.
from duckhuntplayers import *

#Import ducks
from ducks import *

#Import mycolors.
import mycolors

#import interface
from display import *

from game_music import MusicPlayer

import random

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
		self.window = pygame.display.set_mode((self.info.current_w,self.info.current_h))
		
			#window size for convinience
		self.w = self.window.get_width()
		self.h = self.window.get_height()

		self.mode = None
		
		self.music_player = MusicPlayer()
	
		self.num_ducks = 3
		#Ducks list.
		self.duck = None
		#Create the ducks for this game.
		#Give this game a list of players to pick from.
		self.players = {"P1": InteractivePlayer(), "R": Robot()}
		self.player = self.players["P1"]

	##==========================================================================
	##==========================================================================
	def load_cursor(self):
		pass
	##==========================================================================
	##==========================================================================
	
	##==========================================================================
	##==========================================================================
	#switch game state, must turn off all other game states
	def switch_state(self, state):
		self.music_player.stop()
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
		if(self.player.get_score() >= 1500):
			display.text("YOU WIN!!!", int(self.h*0.2), mycolors.RED, 1, (self.h*0.8/2), True)
		else:
			display.text("Game Over", int(self.h*0.2), mycolors.RED, 1, (self.h*0.8/2), True)
		display.draw_buttons("over")
		pygame.display.update()
		
	#Display in game screen
	#Include: blue background, grass, "Duck: ", "Bullets: ", "Score: "
	def ingame_screen(self):
		self.window.fill(mycolors.LIGHT_BLUE)
		display = Display(self.window)
		display.draw_grass()
		display.text("Ducks: " + str(self.num_ducks), int(self.h*0.1), mycolors.BLACK, int(self.w*0.1), int(self.h*0.85), False)
		display.text("Bullets: " + str(self.player.get_num_bullets()), int(self.h*0.1), mycolors.BLACK, int(self.w*0.4), int(self.h*0.85), False)
		display.text("Score: " + str(self.player.get_score())  , int(self.h*0.1), mycolors.BLACK, int(self.w*0.7), int(self.h*0.85), False)
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
	
	#draw duck
	def render_objects(self):
		self.duck.beDrawn()
	#update location
	def update_objects(self):
		self.duck.move()
		
		if(not self.duck.on_screen()):
			self.duck = None
		
	#def make_duck_visible(self):
	#	self.duck.set_visible(True)
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
			if event.type == pygame.KEYDOWN:
				#click start new game button
				if event.key == pygame.K_e:
					self.switch_state("over")
			if(event.type == pygame.MOUSEBUTTONDOWN):
				self.music_player.play_sound("shot")
				locationWhereShot = self.player.shot_at(event)
				hit = self.check_hit_duck(locationWhereShot)
				
				if(hit):
					print("Hit duck")
					self.duck.die()
					self.player.update_score(500)
				else:
					print("Didn't hit duck")
	
	#Possible events: KEYS(E, H, M), quit
	def select_mode(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.switch_state("quit")
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_e:
					self.mode = "easy"
					#self.make_ducks(3, self.mode)
					self.switch_state("in")
				elif event.key == pygame.K_h:
					self.mode = "hard"
					#self.make_ducks(3, self.mode)
					self.switch_state("in")
				elif event.key == pygame.K_m:
					self.mode = "medium"
					#self.make_ducks(3, self.mode)
					self.switch_state("in")
	#==========================================================================
	##==========================================================================

#	def clear_ducks(self):
#		self.duck = None
	
	#initialize game
	def init(self):
		self.music_player.play_sound("start_game")
		self.beginning_screen()
		#main game loop
		while(not self.game_states["quit"]):
			if self.game_states["beginning"] == True:
				while self.game_states["beginning"]:
					self.mouse_action_beginning()
				#beginning state ----> mode selection / quit game
				self.mode_selection_screen()
			elif self.game_states["modes"] == True:
				self.music_player.play_sound("dog_laughing")
				while self.game_states["modes"]:
					self.select_mode()
				#mode selection state ---> ingame state / quit game
				
				
				pygame.display.update()
				self.ingame_screen()
			elif self.game_states["in"] == True:
				self.music_player.play_sound("start_round")
				
				self.num_ducks = 3
				
				self.duck = self.random_duck_creator(self.mode, )
				
				self.player.clear_score()
				self.player.set_bullets(10)

				#Delay move ducks for six seconds until sound ends.
				pygame.display.update()

				time.sleep(6)
				
				while self.game_states["in"]:
					self.mouse_action_ingame()
					if self.num_ducks <= 0 or self.player.get_num_bullets() <= 0:
						self.switch_state("over")
						
						if(self.player.get_score() >= 1500):
							self.music_player.play_sound("end_game")
							
						else:
							self.music_player.play_sound("game_over")
						
					else:
						self.ingame_screen()
						if self.duck == None:
							self.duck = self.random_duck_creator(self.mode)
							self.num_ducks -= 1
						self.render_objects()
						self.update_objects()
						pygame.display.update()
						self.clock.tick(20)
				#in game state   ----> game over state / quit game
				self.game_over_screen()
			elif self.game_states["over"] == True:
				while self.game_states["over"]:
					self.mouse_action_game_over()
				#game over state ----> mode selection / quit game
				self.mode_selection_screen()

		
	#def checkDucksGone(self):
	##	if(len(self.ducks) <= 0):
	#		return True
	#	else:
	#		return False


		



#	

#	def make_ducks(self, how_many, mode):
	
#		if(len(self.ducks) > 0):
#			self.clear_ducks()
			
#		for i in range(how_many):
#			self.ducks.append(self.createDuck(self.window, mode))
#def createDuck(self, window, typeDuck):
	
#		return Duck(window, typeDuck)
			




			
			
	##==========================================================================
	



#	locationWhereShot = self.player.shotAt()
	#	isShot = self.check_hit_duck(locationWhereShot)


				#check if duck is shot
	def check_hit_duck(self, location):
		return self.duck.was_hit(location)
		
				
	##==========================================================================
			

	def random_duck_creator(self, mode):
		return SquareDuck(self.window, mode, int(random.random()*self.window.get_width()*0.7) + 136)