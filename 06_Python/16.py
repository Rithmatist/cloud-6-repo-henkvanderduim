'''
The output should be:

'''
import random

# generate random int
goal = random.randint(1,100)

win = False
tries = 0

while win == False and tries < 7:
	try:
		# ask for input
		inpt = int(input("Please input a number between 1 and 100: "))
		# count attempt as a try
		tries += 1

		# check for match
		if inpt == goal:
			win = True
			print("Congrats, you guessed the number!")
			print("It took you", tries, "tries")
		# give hints
		elif inpt < goal:
			print("The number should be higher")
		else:
			print("The number should be lower")

	except:
		print("Please type an integer")

# 
# het enige wat ik hier kan verzinnen is het stuk hieronder.
# Meer dan 7 tries en checken op False.
# ik heb het alks volgt aangepast.
#if win == False:
#	print("Game over! You took more than seven tries")
if tries == 6:
    print("Game over! You took more than seven tries")