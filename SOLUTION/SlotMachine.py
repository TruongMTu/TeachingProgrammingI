import random

class SlotMachine():
	
	slotIndex=['BAR','LEMON','CHERRY','LUCKY7']
	luckySeven = ['LUCKY7','LUCKY7','LUCKY7']
	luckyBar = ['BAR','BAR','BAR']
	luckyLemon = ['LEMON','LEMON','LEMON']
	luckyCherry = ['CHERRY','CHERRY','CHERRY']
    
	def __init__(self, name):
		self.__name__ = name

	# Return a random position from slotIndex
	# For example, slotIndex[0] = 'BAR'
	def getSlotIndex(self):
		return self.slotIndex[random.randint(0,3)]
	
	# Method for pulling the lever and returns an array
	# of 3 random things from slotIndex
	def pullLever(self):
		screen = []
		for i in range(0,3):
			screen.append(self.getSlotIndex())
		return screen
	
	# Simulates pulling the lever and returning a score
	# based on that array. Print out your array
	# Scores are as follows:
	# 3 x LUCKY7 = 777
	# 3 x BAR = 50
	# 3 x LEMON = 25
	# 3 x CHERRY = 3
	# ['CHERRY', 'CHERRY', *] = 2, * = wild card
	# ['CHERRY', *, *] = 1, * = wild card
	def getScore(self, scores):
		print(scores)
		if scores == self.luckySeven:
			return 777
		elif scores == self.luckyBar:
			return 50
		elif scores == self.luckyLemon:
			return 25
		elif scores == self.luckyCherry:
			return 3
		elif scores[0] == 'CHERRY' and scores[1] == 'CHERRY':
			return 2
		elif scores[0] == 'CHERRY':
			return 1
		else:
			return 0

