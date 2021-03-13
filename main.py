from IPython.display import clear_output
import time, ticTacToe

gameOn = True
gameStart = False
board = [" "," "," ",
		 " "," "," ",
		 " "," "," "]
playAgain = None

ticTacToe.displayBoard(board)

while gameOn:
	

	choose = input("Please choose X or O to start.\r\n")
	if choose.capitalize() == 'X':
		player = ['X','O']
		gameStart = True
	elif choose.capitalize() == 'O':
		player = ['O','X']
		gameStart = True
	else:
		print('Invalid Input, please enter X or O.')
		
	playAgain = ticTacToe.matchStart(gameStart, board, player)
	
	if playAgain:
		gameStart = False
		board = [" "," "," ",
				 " "," "," ",
				 " "," "," "]
		ticTacToe.displayBoard(board)
	elif playAgain == False:
		gameOn = False
		time.sleep(2)