#This module contains all the player classes and their respecsctive helper classes.
##====================================================
class Player(object):
	
	#Player class constructor
	def __init__(self):
		
		#Initializes score to zero.
		self.score = 0
		self.name = "P"
	
	#Returns a 2-tuple with the location at which
	#the player shot at the screen.
	def shotAt(self):
		return (0,0)
		
	def update_score(self, points):
		self.score += points
		
	def update(self):
		pass
		
	def getName(self):
		pass
		
	def __eq__(self , other):
		self.name == other.name

##====================================================

##====================================================
class InteractivePlayer(Player):
	
	#Player class constructor
	def __init__(self):
		Player.__init__(self)
		self.name = "P1"
		
	#Returns a 2-tuple with the location at which
	#the player shot at the screen.
		
	def update(self):
		pass
		
	def getName(self):
		return self.name

##====================================================

##====================================================
#Class that represents the robot that will play as this game's player.
class Robot(Player):
	
	def __init__(self):
		Player.__init__(self)
		self.name = "R"
		
	def shotAt(self):
		return (0,0)
		
	def update():
		pass
		
##====================================================