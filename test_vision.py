import pygame
import pygame.camera

import mycolors

from pygame.locals import *

pygame.init()
pygame.camera.init()

class RobotEye(object):
    def __init__(self):
        self.size = (640,480)
        # create a display surface. standard pygame stuff
        self.display = pygame.display.set_mode(self.size, 0)
        
        # this is the same as what we saw before
        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        self.cam = pygame.camera.Camera(self.clist[0], self.size)
        self.cam.start()

        # create a surface to capture to.  for performance purposes
        # bit depth is the same as that of the display surface.
        self.snapshot = pygame.surface.Surface(self.size, 0, self.display)

    def get_and_flip(self):
        # if you don't want to tie the framerate to the camera, you can check 
        # if the camera has an image ready.  note that while this works
        # on most cameras, some will never return true.
        if self.cam.query_image():
            self.snapshot = self.cam.get_image(self.snapshot)

        # threshold against the color we got before
            mask = pygame.mask.from_threshold(self.snapshot, mycolors.PURPLE, (30, 30, 30))
            self.display.blit(self.snapshot,(0,0))
        # keep only the largest blob of that color
            connected = mask.connected_component()
        # make sure the blob is big enough that it isn't just noise
            if mask.count() > 100:
            # find the center of the blob
                coord = mask.centroid()
            # draw a circle with size variable on the size of the blob
                pygame.draw.circle(self.display, mycolors.GREEN, coord, max(min(50,mask.count()/400),5))
            pygame.display.flip()

    def main(self):
        going = True
        while going:
            events = pygame.event.get()
            for e in events:
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    # close the camera safely
                    self.cam.stop()
                    going = False

            self.get_and_flip()
			
			
			
app = RobotEye()
app.main()

pygame.camera.quit()
pygame.quit()

quit()
