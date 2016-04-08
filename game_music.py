import pygame

pygame.mixer.music.load("Duck Hunt Nes Soundtrack.mp3")
pygame.mixer.music.load("Duck Hunt Sound Effects.mp3")

class game_music:
  
  def __init__(self, tune):
    self.tune = tune
  
  def play_sound(self):
