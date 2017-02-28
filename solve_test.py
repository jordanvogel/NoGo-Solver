from board import GoBoard
from board_util import GoBoardUtil, BLACK, WHITE, EMPTY, BORDER, FLOODFILL

def solve(board, color):
	winner = color
	moveList = []
	newBoard = board.copy()


def search(color,newBoard):
	legalMoves = generate_legal_moves(color,board)
	
	if legalMoves.size() > 1:
		for child in legalMoves:
			newBoard._play_move(child)
			switchColor = GoBoardUtil.opponent(color)
			search(switchColor, newBoard)

	elif legalMoves.size() == 1:
		return color
	
	else:
		switchColor = GoBoardUtil.opponent(color)
		return switchColor
