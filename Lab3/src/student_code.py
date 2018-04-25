import common

def minmax_tictactoe(board, turn):
	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);
        if (turn == common.constants.X):
                return max_value(board)
        elif(turn == common.constants.O):
                return min_value(board)
        else:
                return common.constants.NONE

def abprun_tictactoe(board, turn):
	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);

        alpha = common.constants.O
        beta = common.constants.X
        if (turn == common.constants.X):
                return ab_max_value(board, alpha, beta)
        elif (turn == common.constants.O):
                return ab_min_value(board, alpha, beta)
        else:
                return common.constants.NONE

def ab_max_value(board, alpha, beta):
        v = common.constants.O
        result = common.game_status(board)
        if ((result == common.constants.X) or 
            (result == common.constants.O)):
                return result
        elif tie(board, len(board) - 1):
                return common.constants.NONE
        else:
                for i in range(0, len(board)):
                    if board[i] == 0:
                        board[i] = common.constants.X
                        v = maximum(v, ab_min_value(board, alpha, beta))
                        board[i] = 0                        
                        if (v == maximum(v, beta)):
                            return v
                        alpha = maximum(alpha, v)
                return v
        
def ab_min_value(board, alpha, beta):
        v = common.constants.X
        result = common.game_status(board)
        if ((result == common.constants.X) or
            (result == common.constants.O)):
                return result
        elif tie(board, len(board) - 1):
                 return common.constants.NONE
        else:
                for i in range(0, len(board)):
                    if board[i] == 0:
                        board[i] = common.constants.O
                        v = minimum(v, ab_max_value(board, alpha, beta))
                        board[i] = 0                        
                        if (v == minimum(v, alpha)):
                            return v
                        beta = minimum(beta, v)
                return v
                 
        

def max_value(board):
        v = common.constants.O
        result = common.game_status(board)
        if ((result == common.constants.X) or 
            (result == common.constants.O)):
                return result
        elif tie(board,len(board) - 1):
                return common.constants.NONE
        else:
                for i in range(0, len(board)):
                        if board[i] == 0:
                                board[i] = common.constants.X
                                v = maximum(v, min_value(board))
                                board[i] = 0
                return v

def min_value(board):
        v = common.constants.X
        result = common.game_status(board)
        if ((result == common.constants.X) or 
            (result == common.constants.O)):
                return result
        elif tie(board, len(board) - 1):
                return common.constants.NONE
        else:
                for i in range (0, len(board)):
                        if board[i] == 0:
                                board[i] = common.constants.O
                                v = minimum(v, max_value(board))
                                board[i] = 0
                return v


def maximum(v, new_v):
        if v == 1:
                return v
        if new_v == 1:
                return new_v
        if v == 0:
                return v
        if new_v == 0:
                return new_v
        return v

def minimum(v, new_v):
        if v == 2:
                return v
        if new_v == 2:
                return new_v
        if v == 0:
                return v
        if new_v == 0:
                return new_v
        return v

def tie(board,n):
        if n == 0:
                return board[n] != 0
        return (board[n] != 0) and tie(board, n - 1)

x = minmax_tictactoe([1,2,0,0,1,0,0,0,0],1)
print(x)
x = abprun_tictactoe([1,2,0,0,1,0,0,0,0], 2)
print(x)

