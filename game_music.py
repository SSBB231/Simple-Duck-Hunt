import pygame

class MusicPlayer:
	
	def __init__(self):
		self.sounds = {}

		self.sounds["start_game"] = pygame.mixer.Sound("start_game.wav")
		self.sounds["end_game"] = pygame.mixer.Sound("end_game.wav")
		self.sounds["start_round"] = pygame.mixer.Sound("start_round.wav")
		self.sounds["got_duck"] = pygame.mixer.Sound("got_duck.wav")
		self.sounds["shot"] = pygame.mixer.Sound("shot.wav")
		self.sounds["falling"] = pygame.mixer.Sound("falling.wav")
		self.sounds["lost_duck"] = pygame.mixer.Sound("game_over.wav")
		self.sounds["dog_laughing"] = pygame.mixer.Sound("dog_laughing.wav")
		self.sounds["game_over"] = pygame.mixer.Sound("game_over.wav")
		
		self.tune = self.sounds["start_game"]
  
	def play_sound(self, tune_name):

		self.tune = self.sounds[tune_name]
		pygame.mixer.Sound.play(self.tune)
		
	def stop(self):
		self.tune.stop()
	
