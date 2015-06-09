import random

class SlotMachine():
	
	slotIndex=['BAR','LEMON','CHERRY','LUCKY7']
    
	def __init__(self, name):
		self.__name__ = name

	# Return a random position from slotIndex
	# For example, slotIndex[0] = 'BAR', 
	# slotIndex[1] = LEMON, etc...
	def getSlotIndex(self):
		#IMPLEMENT
	
	# Method for pulling the lever and returns an array
	# of 3 random things from slotIndex
	def pullLever(self):
		#IMPLEMENT
	
	# Simulates pulling the lever and returning a score
	# based on that array. Print out your array
	# Scores are as follows:
	# 3 x LUCKY7 = 777
	# 3 x BAR = 50
	# 3 x LEMON = 25
	# 3 x CHERRY = 3
	# ['CHERRY', 'CHERRY', *] = 2, * = wild card
	# ['CHERRY', *, *] = 1, * = wild card
	def getScore(self):
		#IMPLEMENT

