# Chess by Guy and Jay
#Modules
import os

#Functions
def refresh():
	global turn, error
	# if turn == "white":
	print("   \033[4m  A  B  C  D  E  F  G  H  \033[0m")
	print(f" 1 | {board[0][0]}  {board[0][1]}  {board[0][2]}  {board[0][3]}  {board[0][4]}  {board[0][5]}  {board[0][6]}  {board[0][7]} |")
	print(f" 2 | {board[1][0]}  {board[1][1]}  {board[1][2]}  {board[1][3]}  {board[1][4]}  {board[1][5]}  {board[1][6]}  {board[1][7]} |")
	print(f" 3 | {board[2][0]}  {board[2][1]}  {board[2][2]}  {board[2][3]}  {board[2][4]}  {board[2][5]}  {board[2][6]}  {board[2][7]} |")
	print(f" 4 | {board[3][0]}  {board[3][1]}  {board[3][2]}  {board[3][3]}  {board[3][4]}  {board[3][5]}  {board[3][6]}  {board[3][7]} |")
	print(f" 5 | {board[4][0]}  {board[4][1]}  {board[4][2]}  {board[4][3]}  {board[4][4]}  {board[4][5]}  {board[4][6]}  {board[4][7]} |")
	print(f" 6 | {board[5][0]}  {board[5][1]}  {board[5][2]}  {board[5][3]}  {board[5][4]}  {board[5][5]}  {board[5][6]}  {board[5][7]} |")
	print(f" 7 | {board[6][0]}  {board[6][1]}  {board[6][2]}  {board[6][3]}  {board[6][4]}  {board[6][5]}  {board[6][6]}  {board[6][7]} |")
	print(f" 8 | {board[7][0]}  {board[7][1]}  {board[7][2]}  {board[7][3]}  {board[7][4]}  {board[7][5]}  {board[7][6]}  {board[7][7]} |")
	
	if error != "":
		print(error + ": " + answer)

def clear():
	os.system("clear")

def checkMove():
	global answer, error, turn, whiteKingHasMoved, blackKingHasMoved, whiteRookHasMovedRight, blackRookHasMovedRight, whiteRookHasMovedLeft, blackRookHasMovedLeft
	# check answer
	# 0=CurrentPos, 1=GoToPos
	answerParts = answer.split(",")
	black = ["♖","♘","♗","♔","♕","♙"]
	white = ["♜","♞","♝","♚","♛","♟"]
	validLetters = ["A","B","C","D","E","F","G","H"]
	try:
		if int(answerParts[0][1]) not in range(1,9) or answerParts[0][0].upper() not in validLetters:
			error = "Incorrect Format"
			return False
		if int(answerParts[1][1]) not in range(1,9) or answerParts[1][0].upper() not in validLetters:
			error = "Incorrect Format"
			return False
	except:
		error = "Incorrect Format"
		return False

	# 0=Number, 1=Letter
	currentPos = [int(answerParts[0][1])-1, validLetters.index(answerParts[0][0].upper())]
	targetPos = [int(answerParts[1][1])-1, validLetters.index(answerParts[1][0].upper())]
	# check piece
	currentPiece = board[int(answerParts[0][1])-1][ord(answerParts[0][0].upper())-65] #Get the current piece; max is 7, min is 0
	targetPiece = board[int(answerParts[1][1])-1][ord(answerParts[1][0].upper())-65] #Get the target peice; max is 7, min is 0
	# 0=row 1=column
	if turn=="black" and currentPiece not in black:
		error = "Wrong Color"
		return False
	if turn=="white" and currentPiece not in white:
		error = "Wrong Color"
		return False
	if currentPiece == "□":
		error = "No Piece Selected"
		return False
	
	# pice select
	if turn=="white" and targetPiece in white:
		error = "Can't Take Piece"
		return False
	if turn=="black" and targetPiece in black:
		error = "Can't Take Piece"
		return False
	# move pawn
	if currentPiece=="♙":
		if targetPos[1] == currentPos[1] and targetPos[0] == currentPos[0]+1:
			if targetPiece!="□":
				error = "Invalid Move"
				return False
		# double first move
		elif currentPos[0] == 1 and targetPos[1] == currentPos[1] and targetPos[0] == currentPos[0]+2:
			if targetPiece!="□" and board[currentPos[0]+1][currentPos[1]+1]!="□":
				error = "Invalid Move"
				return False
		# ✓ diagonal
		elif targetPos[0] == currentPos[0]-1 or currentPos[0]+1 and targetPos[1] != currentPos[1]-1:
			if targetPiece not in white:
				error = "Invalid Move"
				return False
		else:
			error = "Invalid Move"
			return False
	if currentPiece=="♟":
		if targetPos[1] == currentPos[1] and targetPos[0] == currentPos[0]-1:
			if targetPiece!="□":
				error = "Invalid Move"
				return False
		# double first move
		elif currentPos[0] == 6 and targetPos[1] == currentPos[1] and targetPos[0] == currentPos[0]-2:
			if targetPiece!="□" and board[currentPos[0]+1][currentPos[1]+1]!="□":
				error = "Invalid Move"
				return False
		# ✓ diagonal
		elif targetPos[0] == currentPos[0]-1 or currentPos[0]+1 and targetPos[1] != currentPos[1]-1:
			if targetPiece in white or targetPiece=="□":
				error = "Invalid Move"
				return False
		else:
			error = "Invalid Move, else"
			return False
	
	# king
	if currentPiece=="♚" or currentPiece=="♔": #working
		if currentPos[0]+1 == targetPos[0] or currentPos[0]-1==targetPos[0]:
			if currentPos[1]+1 == targetPos[1] or currentPos[1]-1==targetPos[1]:
				if currentPiece=="♚":
					whiteKingHasMoved == True
				elif currentPiece=="♔":
					blackKingHasMoved == True
			else:
				if currentPiece=="♚":
					whiteKingHasMoved == True
				elif currentPiece=="♔":
					blackKingHasMoved == True
				
		# castle
		# we still need to add queenside castling and connect hasmoved
		
		# White Castle-kingside
		elif currentPiece=="♚" and whiteKingHasMoved==False and whiteRookHasMovedRight==False and targetPos[0]==7 and targetPos[1]==6:
			for i in range(1,3):
				print(board[currentPos[0]][currentPos[1]+i])
				if board[currentPos[0]][currentPos[1]+i] != "□":
					error = "Path is Blocked"
					return False
			board[currentPos[0]][currentPos[1]] = "□"
			board[currentPos[0]][currentPos[1]+2] = currentPiece
			board[currentPos[0]][currentPos[1]+3] = "□"
			board[currentPos[0]][currentPos[1]+1] = "♜"
		# Black Castle-kingside
		elif currentPiece=="♔" and blackKingHasMoved==False and blackRookHasMovedRight==False and targetPos[0]==0 and targetPos[1]==6:
			for i in range(1,3):
				print(board[currentPos[0]][currentPos[1]+i])
				if board[currentPos[0]][currentPos[1]+i] != "□":
					error = "Path is Blocked"
					return False
			board[currentPos[0]][currentPos[1]] = "□"
			board[currentPos[0]][currentPos[1]+2] = currentPiece
			board[currentPos[0]][currentPos[1]+3] = "□"
			board[currentPos[0]][currentPos[1]+1] = "♖"
		
		# White Castle-queenside
		elif currentPiece=="♚" and whiteKingHasMoved == False and whiteRookHasMovedLeft == False and targetPos[0] == 7 and targetPos[1] == 2: #Check for can castle
			if board[7][3]=="□" and board[7][2]=="□" and board[7][1]=="□": #Check for pieces are in right spot
				board[7][0]="□"
				board[7][2]="♚"
				board[7][3]="♜"
				board[7][4]="□"
			else:
				error="Castle is Blocked"
				return False
		# Black Castle-queenside
		elif currentPiece=="♔" and blackKingHasMoved == False and blackRookHasMovedLeft == False and targetPos[0] == 0 and targetPos[1] == 2:
			print("can castle")
			if board[0][3]=="□" and board[0][2]=="□" and board[0][1]=="□": #Check for pieces are in right spot
				board[0][0]="□"
				board[0][2]="♚"
				board[0][3]="♜"
				board[0][4]="□"
			else:
				error="Castle is Blocked"
				return False
		
		# Castling errors
		elif currentPiece=="♚" and whiteKingHasMoved==True or whiteRookHasMovedLeft==True or whiteRookHasMovedRight==True and targetPos[0]==7 and targetPos[1]==1:
			error = "Too late to castle"
			return False
		elif currentPiece=="♔" and blackKingHasMoved==True or blackRookHasMovedLeft==True or blackRookHasMovedRight==True and targetPos[0]==0 and targetPos[1]==1:
			error = "Too late to castle"
			return False
		else:
			error = "Invalid Move, castle"
			return False
	
	# move knightmatrix
	# moves 2 right/left and 1 down/up OR 2 up/down and 1 right/left
	if currentPiece=="♞":
		if (targetPos[0] == currentPos[0]+1 or currentPos[0]-1) and (targetPos[1] == currentPos[1]+2 or currentPos[1]-2):
			pass #not works, though it may
		elif (targetPos[0] == currentPos[0]+2 or currentPos[0]-2) and (targetPos[1] == currentPos[1]+1 or currentPos[1]-1):
			pass #works
		else:
			error = "Invalid Move"
			return False

	# move rook
	if currentPiece=="♜" or currentPiece=="♖": #check for rook
		if currentPos[0]==targetPos[0] or currentPos[1]==targetPos[1]: #checks if the position is valid
			# Get Driection
			if targetPos[1]>currentPos[1]: direction="right"
			elif targetPos[1]<currentPos[1]: direction="left"
			elif targetPos[0]<currentPos[0]: direction="up"
			elif targetPos[0]>currentPos[0]: direction="down"
			print(direction)
			# Check path
			if direction=="right": #good
				for space in range(abs(targetPos[1]-currentPos[1])-1): #raycasts
					if board[currentPos[0]][currentPos[1]+space+1]!="□":
						error = "Path is Blocked"
						return False
			if direction=="left": #good
				for space in range(abs(targetPos[1]-currentPos[1])-1): #raycasts
					if board[currentPos[0]][currentPos[1]-space-1]!="□":
						error = "Path is Blocked"
						return False
			if direction=="up": #good?
				for space in range(abs(targetPos[0]-currentPos[0])-1): #raycasts
					if board[currentPos[0]-space-1][currentPos[1]]!="□":
						error = "Path is Blocked"
						return False
			if direction=="down": #good?
				for space in range(abs(targetPos[0]-currentPos[0])-1): #raycasts
					if board[currentPos[0]+space+1][currentPos[1]]!="□":
						error = "Path is Blocked"
						return False
		else:
			error = "Invalid Move"
			return False

		if currentPiece=="♜" and whiteRookHasMovedRight==False and currentPos==[7,7]:
			whiteRookHasMovedRight=True
		if currentPiece=="♖" and blackRookHasMovedRight==False and currentPos==[0,7]:
			blackRookHasMovedRight=True
		if currentPiece=="♜" and whiteRookHasMovedLeft==False and currentPos==[7,0]:
			whiteRookHasMovedLeft=True
		if currentPiece=="♖" and blackRookHasMovedLeft==False and currentPos==[0,0]:
			blackRookHasMovedLeft=True
		print(f"WR{whiteRookHasMovedRight}\nBR{blackRookHasMovedRight}\nWL{whiteRookHasMovedLeft}\nBL{blackRookHasMovedLeft}")

	#Bishop
	#0=Row, 1=Column
	if currentPiece=="♝" or currentPiece=="♗":
		# fixed it
		if abs(currentPos[0]-targetPos[0]) == abs(currentPos[1]-targetPos[1]):
			togo = abs(currentPos[0]-targetPos[0])
			direction = ""
			if targetPos[0]>currentPos[0] and targetPos[1]>currentPos[1]:
				direction="rd" #Correct
			elif targetPos[0]<currentPos[0] and targetPos[1]>currentPos[1]:
				direction="ru" #Correct
			elif targetPos[0]<currentPos[0] and targetPos[1]<currentPos[1]:
				direction="lu" #Correct
			elif targetPos[0]>currentPos[0] and targetPos[1]<currentPos[1]:
				direction="ld" #Correct
			else:
				error = "Invalid Move"
				return False
			for loop in range(1,togo):
				if direction == "ru":
					if board[currentPos[0]-loop][currentPos[1]+loop] != "□":
						error = "Path is Blocked"
						return False
				elif direction == "lu":
					if board[currentPos[0]-loop][currentPos[1]-loop] != "□":
						error = "Path is Blocked"
						return False
				elif direction == "rd":
					if board[currentPos[0]+loop][currentPos[1]+loop] != "□":
						error = "Path is Blocked"
						return False
				elif direction == "ld":
					if board[currentPos[0]+loop][currentPos[1]-loop] != "□":
						error = "Path is Blocked"
						return False
				else:
					error = "Invalid Move"
					return False
		else:
			error = "Invalid Move"
			return False
	
	#Queen
	if currentPiece=="♛" or currentPiece=="♕":
		if abs(currentPos[0]-targetPos[0]) == abs(currentPos[1]-targetPos[1]):
			togo = abs(currentPos[0]-targetPos[0])
			direction = ""
			if targetPos[0]>currentPos[0] and targetPos[1]>currentPos[1]:
				direction="rd" #Correct
			elif targetPos[0]<currentPos[0] and targetPos[1]>currentPos[1]:
				direction="ru" #Correct
			elif targetPos[0]<currentPos[0] and targetPos[1]<currentPos[1]:
				direction="lu" #Correct
			elif targetPos[0]>currentPos[0] and targetPos[1]<currentPos[1]:
				direction="ld" #Correct
			else:
				error = "Invalid Move"
				return False
			for loop in range(1,togo):
				if direction == "ru":
					if board[currentPos[0]-loop][currentPos[1]+loop] != "□":
						error = "Path is Blocked"
						return False
				elif direction == "lu":
					if board[currentPos[0]-loop][currentPos[1]-loop] != "□":
						error = "Path is Blocked"
						return False
				elif direction == "rd":
					if board[currentPos[0]+loop][currentPos[1]+loop] != "□":
						error = "Path is Blocked"
						return False
				elif direction == "ld":
					if board[currentPos[0]+loop][currentPos[1]-loop] != "□":
						error = "Path is Blocked"
						return False
				else:
					error = "Invalid Move"
					return False
		elif currentPos[0]==targetPos[0] or currentPos[1]==targetPos[1]: #checks if the position is valid
			# Get Driection
			if targetPos[1]>currentPos[1]: direction="right"
			elif targetPos[1]<currentPos[1]: direction="left"
			elif targetPos[0]<currentPos[0]: direction="up"
			elif targetPos[0]>currentPos[0]: direction="down"
			print(direction)
			# Check path
			if direction=="right": #good
				for space in range(abs(targetPos[1]-currentPos[1])-1): #raycasts
					if board[currentPos[0]][currentPos[1]+space+1]!="□":
						error = "Path is Blocked"
						return False
			if direction=="left": #good
				for space in range(abs(targetPos[1]-currentPos[1])-1): #raycasts
					if board[currentPos[0]][currentPos[1]-space-1]!="□":
						error = "Path is Blocked"
						return False
			if direction=="up": #good?
				for space in range(abs(targetPos[0]-currentPos[0])-1): #raycasts
					if board[currentPos[0]-space-1][currentPos[1]]!="□":
						error = "Path is Blocked"
						return False
			if direction=="down": #good?
				for space in range(abs(targetPos[0]-currentPos[0])-1): #raycasts
					if board[currentPos[0]+space+1][currentPos[1]]!="□":
						error = "Path is Blocked"
						return False
		else:
			error = "Invalid Move"
			return False
	
	board[currentPos[0]][currentPos[1]] = "□"
	board[targetPos[0]][targetPos[1]] = currentPiece

	# white pawn promotion
	pawnPromote(targetPos, 0, ["♝", "♞", "♜", "♛"])
	# black pawn promotion
	pawnPromote(targetPos, 7, ["♗", "♘", "♖", "♕"])
	# error = str(blackKingHasMoved)
	# addToStats(answer)
	return True

def kingCheck():
	global won
	if any("♚" in sub for sub in board) == False:
		won = "b"
		return True
	elif any("♔" in sub for sub in board) == False:
		won = "w"
		return True

# done
def pawnPromote(targetPos, line, color):
	global board
	change = ""
	piecesList = ("".join(color))
	pieces = ""
	for piece in piecesList:
		if piece=="♛" or piece=="♕":
			pieces+=piece
			break
		pieces+=(piece+" ")
	for i in board[line]:
		if i=="♟" or i=="♙":
			clear()
			refresh()
			print(f"\n                 ({pieces})")
			while change not in ["B","N","R","Q"]:
				change = input("Promote Pawn To: (B,N,R,Q) ").upper()
			if change == "B":
				board[targetPos[0]][targetPos[1]] = color[0]
			if change == "N":
				board[targetPos[0]][targetPos[1]] = color[1]
			if change == "R":
				board[targetPos[0]][targetPos[1]] = color[2]
			if change == "Q":
				board[targetPos[0]][targetPos[1]] = color[3]

# def addToStats(lineToAdd):
# 	file_path = './stats.txt'
	
# 	with open(file_path, 'a') as file:
# 	    file.write(lineToAdd + '\\n')
# def clearFile():
# 	file_path = 'path/to/your/file.txt'

# 	with open(file_path, 'w') as file:
# 	    file.truncate(0)
	
# 	print('The file has been cleared!')
	
#Variables
board = [
	# 0   1   2   3   4   5   6   7 y -->
	["♖","♘","♗","♕","♔","♗","♘","♖",], #0
	["♙","♙","♙","♙","♙","♙","♙","♙",], #1
	["□","□","□","□","□","□","□","□",], #2
	["□","□","□","□","□","□","□","□",], #3
	["□","□","□","□","□","□","□","□",], #4
	["□","□","□","□","□","□","□","□",], #5		 ^
	["♟","♟","♟","♟","♟","♟","♟","♟",], #6     |
	["♜","♞","♝","♛","♚","♝","♞","♜",], #7  x
]
won = ""
turn = "white" #default-white
error = ""
answer = ""
whiteKingHasMoved = False
whiteRookHasMovedRight = False
whiteRookHasMovedLeft = False
blackKingHasMoved = False
blackRookHasMovedRight = False
blackRookHasMovedLeft = False

#Loop
while won == "":
	clear()
	refresh()
	error = ""
	print("\nKey:")
	print("white: ♚ | black: ♔\n")
	answer = input(f"{turn.capitalize()} | Format as: Current Position, Place To Go i.e.(C1,D2)\n")
	if checkMove() == True:
		if turn == "white": turn = "black"
		elif turn == "black": turn = "white"
	if kingCheck() == True:
		clear()
		refresh()
		break
if won == "w":
	print("WHITE WINS")
elif won == "b":
	print("BLACK WINS")