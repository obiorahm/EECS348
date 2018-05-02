import common

class variables:
	counter=0

def sudoku_backtracking(sudoku):
	# PUT YOUR CODE HERE
	# access the sudoku using "sudoku[y][x]"
	# y between 0 and 9
	# x between 0 and 9
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds 
	# explored is optional but recommended 
	variables.counter=0	
	unassigned_variables = []
	get_unassigned_variables(unassigned_variables, sudoku)
	print (backtracking(sudoku,unassigned_variables))
	#print_table(sudoku)

	#variables.counter+=1000000
	return variables.counter

def print_table(sudoku):
	for i in range (0, len(sudoku)):
		for j in range (0, len(sudoku)):
			print sudoku[i][j],
		print'\n'

def get_unassigned_variables(unassigned_variables, sudoku):
	for i in range (0, len(sudoku)):
		for j in range (0, len(sudoku[0])):
			if sudoku[i][j] == 0:
				unassigned_variables.append([i,j])
				#print (i,j)

order_domain_values = [9,8,7,6,5,4,3,2,1]

def backtracking(sudoku, unassigned_variables):
	variables.counter += 1
	if not unassigned_variables:
		return True
	a_variable = unassigned_variables[0]
	unassigned_variables.pop(0)	
	for i in range( 0,len(order_domain_values)):
		v = order_domain_values[i]
		if (common.can_yx_be_z(sudoku, a_variable[0], a_variable[1],v)):
			sudoku[a_variable[0]][a_variable[1]] = v
			result = backtracking(sudoku, unassigned_variables)
			if result:
				return result
			else: 
				sudoku[a_variable[0]][a_variable[1]] = 0
	unassigned_variables.insert(0, a_variable)
	return False

def row_column_constraint(sudoku,val, var):
	for i in range(0,9):
		if sudoku[i][var[1]] == val:
			return False
		if sudoku[var[0]][i] == val:
			return False
	return True

def cube_constraint(sudoku, val, a_variable):
	if a_variable[1] >= 0 and a_variable[1] <= 2:
		starty = 0
		endy = 3
	elif a_variable[1] >=3 and a_variable[1] <= 5:
		starty = 3
		endy = 6
	else:
		starty = 6
		endy = 9

	if a_variable[0] >= 0 and a_variable[0] <= 2:
		startx = 0
		endx = 3
	elif a_variable[0] >=3 and a_variable[0] <= 5:
		startx = 3
		endx = 6
	else:
		startx = 6
		endx = 9		
	constraint = True 
	for i in range (startx, endx):
		for j in range(starty, endy):
			constraint = constraint and (sudoku[i][j] != val)
	return constraint








def sudoku_forwardchecking(sudoku):
	# PUT YOUR CODE HERE
	# access the sudoku using "sudoku[y][x]"
	# y between 0 and 9
	# x between 0 and 9
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds 
	# explored is optional but recommended 
	variables.counter=0
	variables.counter+=1000000
	return variables.counter

def sudoku_mrv(sudoku):
	# PUT YOUR CODE HERE
	# access the sudoku using "sudoku[y][x]"
	# y between 0 and 9
	# x between 0 and 9
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds 
	# explored is optional but recommended 
	variables.counter=0
	variables.counter+=1000000
	return variables.counter
