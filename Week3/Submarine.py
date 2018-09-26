from random import randint #Importing from a library

def prBlue(skk): print("\033[94m {}\033[00m".format(skk))#Function for printing in blue
def prRed(skk): print("\033[91m {}\033[00m".format(skk))#Function for printing in red 
def prGrey(skk): print("\033[90m {}\033[00m".format(skk))#Function for printing in grey


def playBattleship(): #Define game function

	board = []#Create empty list

	length = 10	#Length of list

	for x in range(length):	#Create rows
	    board.append(["~"] * length)


	def printBoardBlue(board):#Function for printing board in blue    
	    for column in board:
	        prBlue ("  ".join(row))

	def printBoardRed(board):	#Function for printing board in blue  
	    for row in board:
	        prRed ("  ".join(row))

	shipRow = randint(0, (length - 1))	#Create random numbers for ship's coordinates
	shipCol = randint(0, (length - 1))

	prGrey("WELCOME TO... \n")
	prBlue("""  
                             ____       _______ _______ _      ______  _____ _    _ _____ _____  
                            |  _ \   /\|__   __|__   __| |    |  ____|/ ____| |  | |_   _|  __ \ 
                            | |_) | /  \  | |     | |  | |    | |__  | (___ | |__| | | | | |__) |
                            |  _ < / /\ \ | |     | |  | |    |  __|  \___ \|  __  | | | |  ___/ 
                            | |_) / ____ \| |     | |  | |____| |____ ____) | |  | |_| |_| |     
                            |____/_/    \_\_|     |_|  |______|______|_____/|_|  |_|_____|_|     """)

	prBlue("""
	                                                                   .
                                                     .                 |
                                                     +                 |
                                            .        |                *+W+-*
                                 .         +y        +W+              . H                 .
                            .   +y           |I.   y  |               ! H= .           .  ^
                            !    |     .    |H '. /   |  ___.        .! H  !   +--.--y !  V
                            !    |    |  +=|H|=='.=+ | |=====|   _  '_H_H__H_. H_/=  J !  !
                          . !    |'     VVV_HHH_/__'._H |  E  |_|=|_|========|_|==|____H. ! _______.
                          I-H_I=I=HH_==_|I_IIIII_I_I_=HH|======.I-I-I-=======-I=I=I=I_=H|=H'===I=I/
~~^~~~^~~~~~^~~^~~~^~^~~^~|                                                                      ,~~~^~~^~~~~^~~~^~^~~~^~~~~^~~~^^
^~~~^^~~~~^~^~^~~^~~^^^~^~|       o     o     o     o     o     o     o     o     o     o       /~~^~~~^^~~~~~^~~~^^~^~~~~^~~~^~~~~
~^~~~~~^~~~~^~~^~~~~^^~~^~.___________________________________________________ ________________'~~~~^^~~^~~~~^~~~^~~~~^~~~^^~~~~^
^~~~~^~~^~~~^~~~^^~~~~^~~~~^~~^~~~^~~^~~~^~~~~^~~^~~~^~~~^^~~~~^~~~~^~~^~~~^~~~~^~~~~^~~^~~~^~~~^^~~~~^~~~~^~~^~~~^~~^^~^~~~~^~~~~^""")

	level1 = raw_input ("CHOOSE YOUR LEVEL: \n1: 10 lives \n2: 8 lives \n3: 6 lives \n")

#Different levels, different amount of lives
	if level1 == "1":
	    lives = 10

	elif level1 == "2":
	    lives = 8

	elif level1 == "3":
	    lives = 6

	else:
		prGrey(level1 + " is too hardcore for us. Let's say level 3")
		lives = 6

	prGrey("\n")
	prGrey ("-----GET READY TO PLAY!----- \n----- THIS IS YOUR BOARD -----")
	printBoardBlue(board)
	prGrey("LIVES: " + str(lives) + "\n")

	for x in range(0, lives):#Looping until player one wins or finishes his lives

		guessRow = raw_input ("GUESS A ROW. \n[Remember there are " + str(length) + " rows.""]\n" )
		guessCol = raw_input ("GUESS A COLUMN .\n[Remember there are " + str(length) + " columns.]\n" )
		intGuessRow = int(guessRow) - 1 #Needs - 1 because computer goes from 0 to 9, not 1 to 10
		intGuessCol = int(guessCol) - 1
		if (intGuessRow == shipRow) and (intGuessCol == shipCol):
			board[intGuessRow][intGuessCol] = "X" #Changes ~ to X on the board to mark the guesses
			printBoardBlue(board)
			prGrey ("YEEES! YOU HIT THE SHIP!\n")
			prBlue( """ 
				  	      	 '==8 > 
				          	  /||
				  	        / o||
				 	       / o o||
				 	     / o o o||
					    / o o o o|| 
					   | o o o o|| 
					   |o o o o o||      
					   |o o o o o||--.   
					   |o o o o o||  |
				~~~~~~~o^^~~^~~~^~^~~~~oo^^~~~~~
				~~~8~~~ ~ ~~.o~~~^~~~~^~~~^~~~~
				~~~~~^o~^~~^o~^^~^~~o~~~~^^~~~~~""")
			prGrey("CONGRATULATIONS!\n")
			break
		else:
				prGrey("OH NO! YOU MISSED!\nTHE SHIP IS STILL FLOATING.\n")
				board[intGuessRow][intGuessCol] = "X"
				printBoardBlue(board)
				x = x + 1
				prGrey("LIVES: " + str(lives - x) + "\n")
	else: #This happens once x reaches the amount of lives, meaning the lives reach 0		
		board[shipRow][shipCol] = "S"  #Changes ~ to S on the board to mark where the ship us
		prRed ("Loser...")
		printBoardRed(board)
		prRed("""

   _____          __  __ ______    ______      ________ _____  
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
 | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
 | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\
                                                               
                                                               
 
""")
#Function playBattleship ends here


prGrey("WELCOME PLAYER ONE!")
play = raw_input ("READY TO PLAY?\n")

if play == ("yes"):
	prGrey("LET'S BEGIN!")
	playBattleship() #Runs playBattleship

	play2 = raw_input ("RESTART?\n") #Asks if player wants to play again
	while play2 == ("yes"):#Will keep looping as long as the answer to restart is yes, if it isn't it exits the loop
		prGrey("LET'S BEGIN!")
		playBattleship()
		play2 = raw_input ("RESTART?\n")

else:
	prGrey("YOUR LOSS... \nYOU WOULD HAVE LOST ANYWAY...")






