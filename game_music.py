import pygame

start = pygame.mixer.Sound("start.mp3")

class game_music:
  
  def __init__(self):
	
  
    self.tune = None
  
  def play_sound(self, tune_name):
    self.tune = tune_name
    
    if tune_name == "gameover":
      music.set_pos
