import pygame
import mycolors
class Display:

	def __init__(self,window):
		self.window = window
		self.w = self.window.get_width()
		self.h = self.window.get_height()
		
	#draw grass
	def draw_grass(self):
		img_grass = pygame.image.load("grass.png")
		img_grass = pygame.transform.scale(img_grass,(self.w,int(self.h*0.3)))
		self.window.blit(img_grass, (0,int(self.h*0.7)))
		

	#text on screen
	#Parameters: text, size, color, x position, y position, center or not(boolean)
	def text(self, msg, size, color, x, y, center):
		font = pygame.font.SysFont(None, size)
		screen_text = font.render(msg, True, color)
		if center == False:
			self.window.blit(screen_text, (x,y)) 
		else:
			#if text needs to be centered
			textRect = screen_text.get_rect()
			textRect.center=(self.w/2), y
			self.window.blit(screen_text, textRect)

	#start button & quit button
	#could be beginning state or game over state
	def draw_buttons(self,state):
		pygame.draw.rect(self.window, mycolors.GREEN , (self.w*0.4, self.h*0.5, self.w*0.2, self.h*0.1))
		pygame.draw.rect(self.window, mycolors.PURPLE, (self.w*0.4, self.h*0.6, self.w*0.2, self.h*0.1))
		if state == "beginning":
			self.text("START", int(self.h*0.1), mycolors.BLACK, 1, self.h*0.55, True)
			self.text("QUIT" , int(self.h*0.1), mycolors.BLACK, 1, self.h*0.65, True)
		else:
			self.text("New", int(self.h*0.1), mycolors.BLACK, 1, self.h*0.55, True)
			self.text("QUIT" , int(self.h*0.1), mycolors.BLACK, 1, self.h*0.65, True)
				
				
