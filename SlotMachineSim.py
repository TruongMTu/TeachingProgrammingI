from SlotMachine import *

def main():
	coins = 10
	slots = SlotMachine("Slot Machine")
	while(coins > 0):
		keepPlaying = input("You have %i left. Pull the lever? (yes, no): " %coins)
		if keepPlaying == 'yes':
			coins = coins - 1
			coins = coins + slots.getScore()
		elif keepPlaying == 'no':
			print("You left with %i coins today. Better luck next time!" %coins)
			print("Your coins now turned into cash: $%i" %(coins*5))
			break
		else:
			print("You didn't enter in <yes> or <no>. Try again.")
	print("You lost all your coins! Try again when you have more money!")

main()