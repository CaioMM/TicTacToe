from IPython.display import clear_output

def displayBoard(currentBoard):
	clear_output()
	print("########## Tic Tac Toe ##########")
	print("            {} | {} | {} ".format(currentBoard[6],currentBoard[7],currentBoard[8]))
	print("           -----------")
	print("            {} | {} | {} ".format(currentBoard[3],currentBoard[4],currentBoard[5]))
	print("           -----------")
	print("            {} | {} | {} ".format(currentBoard[0],currentBoard[1],currentBoard[2]))
	print("#################################")

def checkPosi(posi,board):
	return (board[posi-1] == " ")

def placeMarker(posi, board, turn, player):
	if turn % 2 == 0:
		board[posi-1] = player[0]
	else:
		board[posi-1] = player[1]
	
	displayBoard(board)

def playAgain():
	playA = True
	while playA:
		choose = input("Do you want to play again? Y or N\r\n").upper()
		if choose == 'Y' or choose == 'N':
			if choose == 'Y':
				return True
			else:
				print('Thanks for playing, See you next time.')
				return False
		else:
			print('Please enter Y or N.')


def checkWin(currentBoard, turn, player):
	winner = ''
	if turn % 2 == 0:
		marker = player[0]
	else:
		marker = player[1]
#     check lines
	if currentBoard[0] == marker and currentBoard[1] == marker and currentBoard[2] == marker:
		winner = currentBoard[0]
	if currentBoard[3] == marker and currentBoard[4] == marker and currentBoard[5] == marker:
		winner = currentBoard[3]
	if currentBoard[6] == marker and currentBoard[7] == marker and currentBoard[8] == marker:
		winner = currentBoard[6]
#     check rows
	if currentBoard[0] == marker and currentBoard[3] == marker and currentBoard[6] == marker:
		winner = currentBoard[0]
	if currentBoard[1] == marker and currentBoard[4] == marker and currentBoard[7] == marker:
		winner = currentBoard[1]
	if currentBoard[2] == marker and currentBoard[5] == marker and currentBoard[8] == marker:
		winner = currentBoard[2]
#     check diagonal 01
	if currentBoard[0] == marker and currentBoard[4] == marker and currentBoard[8] == marker:
		winner = currentBoard[0]
#     check diagonal 02
	if currentBoard[2] == marker and currentBoard[4] == marker and currentBoard[6] == marker:
		winner = currentBoard[2]
	
	if winner == 'X' or winner == 'O':
		print("Player {} Won!!!\r\nCongratulations".format(winner))
		return False
	else:
		return True

def isBoardFull(board):
	for i in range(1,10):
		if checkPosi(i,board):
			return False
	return True


def matchStart(gameStart, board, player):
	turn = 0
	while gameStart:
		choose = input("Please choose a position between (1-9) to place marker.\r\n")
#         check if input is a digit
		if choose.isdigit():
			posi = int(choose)
#             check if position is between (1-9)
			if posi in range(1,10):
#                 check if position has a marker
				if checkPosi(posi,board):
					placeMarker(posi, board, turn, player)
					gameStart = checkWin(board, turn, player)
					if gameStart == False:
						return playAgain()
					turn += 1
					if isBoardFull(board):
						print("It's a Draw!!!")
						gameStart = False
						return playAgain()
				else:
					print('Position already taken, choose other place.')
			else:
				print("Invalid position, choose a valid one.")
		else:
			print("Invalid position, choose a valid one.")