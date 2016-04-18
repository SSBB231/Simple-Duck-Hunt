#Import the gaming library: pygame
import pygame

#Import all classes from the duckhuntgame module
from duckhuntgame import *

#Initialize pygame objects.
pygame.init()


game = Game()
game.init()

#End pygame
pygame.quit()
quit()
