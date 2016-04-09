import pygame

class MusicPlayer:
	
	def __init__(self):
		self.sounds = {}

		self.sounds["start"] = pygame.mixer.Sound("start.wav")
		#self.sounds["get_ready"] = pygame.mixer.Sound("get_ready.mp3")
		self.sounds["shot"] = pygame.mixer.Sound("shot.wav")
		#self.sounds["falling"] = pygame.mixer.Sound("falling.mp3")
		#self.sounds["lost_duck"] = pygame.mixer.Sound("lost_duck.mp3")
		#self.sounds["dog_laughing"] = pygame.mixer.Sound("dog_laughing.mp3")
		
		self.tune = self.sounds["start"]
  
	def play_sound(self, tune_name):

		self.tune = self.sounds[tune_name]
		pygame.mixer.Sound.play(self.tune)
	
