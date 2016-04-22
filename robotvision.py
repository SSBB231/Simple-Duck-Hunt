import pygame
import pygame.camera

import mycolors

from pygame.locals import *


pygame.camera.init()

class RobotEye(object):
    def __init__(self, window):
        self.size = (1024,720)
        # create a display surface. standard pygame stuff
        self.display = window
        
        # this is the same as what we saw before
        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        self.cam = pygame.camera.Camera(self.clist[0], self.size)
        self.cam.start()

        # create a surface to capture to.  for performance purposes
        # bit depth is the same as that of the display surface.
        self.snapshot = pygame.surface.Surface(self.cam.get_size(), 0, self.display)

	self.coord = (0, 0)

    def get_snapshot(self):
        # if you don't want to tie the framerate to the camera, you can check 
        # if the camera has an image ready.  note that while this works
        # on most cameras, some will never return true.
        if self.cam.query_image():
            self.snapshot = self.cam.get_image(self.snapshot)

        # threshold against the color we got before
            self.mask = pygame.mask.from_threshold(self.snapshot, mycolors.WHITE, (30, 30, 30))
            self.display.blit(self.snapshot,(0,0))
        # keep only the largest blob of that color
            connected = self.mask.connected_component()
        # make sure the blob is big enough that it isn't just noise
            if self.mask.count() > 100:
            # find the center of the blob
                self.coord = self.mask.centroid()

    def be_drawn(self):
	pygame.draw.circle(self.display, mycolors.GREEN, self.coord, max(min(50,self.mask.count()/400),5))
	
	snapshot = pygame.transform.scale(self.snapshot, (int(self.display.get_width()*0.2), int(self.display.get_height()*0.2)))
	self.display.blit(snapshot, (int(self.display.get_width()*0.8), int(self.display.get_height()*0.75)))
	

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
