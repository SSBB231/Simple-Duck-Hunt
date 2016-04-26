import pygame
import pygame.camera

import mycolors

from pygame.locals import *


pygame.camera.init()

class RobotEye(object):
    def __init__(self, window, target_color = None, brightness = 20):

	if(target_color == None):
	    target_color = mycolors.PURPLE

	self.brightness = brightness


        self.size = (1024,720)
        # create a display surface. standard pygame stuff
        self.display = window
        
        # this is the same as what we saw before
        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        self.cam = pygame.camera.Camera(self.clist[0], self.size)

	self.cam.set_controls(brightness=10)

        self.cam.start()

        # create a surface to capture to.  for performance purposes
        # bit depth is the same as that of the display surface.
        self.snapshot = pygame.surface.Surface(self.cam.get_size(), 0, self.display)

	self.coord = (0, 0)

	self.target_color = target_color

	self.circle_color = mycolors.GREEN

	if(self.target_color == mycolors.GREEN):
	    self.circle_color = mycolors.PURPLE

    def get_snapshot(self):

	print(self.cam.set_controls(brightness = self.brightness))
        # if you don't want to tie the framerate to the camera, you can check 
        # if the camera has an image ready.  note that while this works
        # on most cameras, some will never return true.
        if self.cam.query_image():
            self.snapshot = self.cam.get_image(self.snapshot)

	    

        # threshold against the color we got before
            self.mask = pygame.mask.from_threshold(self.snapshot, self.target_color, (50, 50, 50))
            self.display.blit(self.snapshot,(0,0))
        # keep only the largest blob of that color
            connected = self.mask.connected_component()
        # make sure the blob is big enough that it isn't just noise
            if self.mask.count() > 100:
            # find the center of the blob
                self.coord = self.mask.centroid()

    def change_target_color(self, color):
	self.target_color = color

    def change_brightness(self):
	if(self.brightness >= 50):
		self.brightness = 0

	self.brightness+=4

    def calibrate(self):

	self.target_color = mycolors.PURPLE

	target_color = None

	got_color = False
	
	while(not got_color):
		# capture the image
		self.snapshot = self.cam.get_image(self.snapshot)
		#blit it to the display surface
		self.display.blit(self.snapshot, (0,0))

		self.display.fill(self.target_color, (0, self.display.get_height()-200, self.display.get_width(), self.display.get_height()))

		# make a rect in the middle of the screen
		crect = pygame.draw.rect(self.display, (255,0,0), (self.display.get_width()//2,self.display.get_height()//2,30,30), 4)
		# get the average color of the area inside the rect
		target_color = pygame.transform.average_color(self.snapshot, crect)
		# fill the upper left corner with that color
		self.display.fill(target_color, (0,0,50,50))
		pygame.display.flip()
		
		for event in pygame.event.get():
			if(event.type == pygame.KEYDOWN):
				got_color = True


	if(target_color != None):
	    self.target_color = target_color

    def be_drawn(self):
	pygame.draw.circle(self.display, self.circle_color, self.coord, max(min(50,self.mask.count()/400),5))
	
	snapshot = pygame.transform.scale(self.snapshot, (int(self.display.get_width()*0.2), int(self.display.get_height()*0.2)))
	self.display.blit(snapshot, (int(self.display.get_width()-snapshot.get_width()), int(0)))
	

    #def main(self):
     #   going = True
      #  while going:
       #     events = pygame.event.get()
        #    for e in events:
         #       if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
          #          # close the camera safely
           #         self.cam.stop()
            #        going = False

            #self.get_and_flip()
