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
	backtracking(sudoku,unassigned_variables)

	return variables.counter

def print_table(sudoku):
	for i in range (0, len(sudoku)):
		for j in range (0, len(sudoku[i])):
			print sudoku[i][j],
		print '\n'

def get_unassigned_variables(unassigned_variables, sudoku):
	for i in range (0, len(sudoku)):
		for j in range (0, len(sudoku[0])):
			if sudoku[i][j] == 0:
				unassigned_variables.append([i,j])
				#print (i,j)

order_domain_values = [9,8,7,6,5,4,3,2,1]
#order_domain_values = [1,2,3,4,5,6,7,8,9]

def backtracking(sudoku, unassigned_variables):
	variables.counter += 1
	if not unassigned_variables:
		return True
	var = unassigned_variables[0]
	unassigned_variables.pop(0)	
	for i in range( 0,len(order_domain_values)):
		v = order_domain_values[i]
		if (common.can_yx_be_z(sudoku, var[0], var[1],v)):
			sudoku[var[0]][var[1]] = v
			result = backtracking(sudoku, unassigned_variables)
			if result:
				return result
			sudoku[var[0]][var[1]] = 0
	unassigned_variables.insert(0, var)
	return False


def sudoku_forwardchecking(sudoku):
	# PUT YOUR CODE HERE
	# access the sudoku using "sudoku[y][x]"
	# y between 0 and 9
	# x between 0 and 9
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds 
	# explored is optional but recommended 

	variables.counter=0	
	unassigned_variables = []	
	domain = []
	get_unassigned_variables(unassigned_variables, sudoku)
	get_domain_unassigned_variables(unassigned_variables, sudoku)
	fowardchecking(sudoku, unassigned_variables)
	return variables.counter



def get_domain_unassigned_variables(unassigned_variables, sudoku):
	for i in range(0, len(unassigned_variables)):
		var = unassigned_variables[i]
		x = []
		for j in order_domain_values:
			if common.can_yx_be_z(sudoku, var[0], var[1], j):
				x.append(j)
		unassigned_variables[i].append(x)



def fowardchecking(sudoku, unassigned_variables):
	variables.counter += 1
	if not unassigned_variables:
		return True
	var = copy_list(unassigned_variables[0])
	unassigned_variables.pop(0)
	for val in var[2]:
		sudoku[var[0]][var[1]] = val
		new_unassigned_variables = copy_list(unassigned_variables)		
		if update_domain(sudoku, var, new_unassigned_variables):		
			result = fowardchecking(sudoku, new_unassigned_variables)
			if result:
				return result
		sudoku[var[0]][var[1]] = 0
	unassigned_variables.insert(0, var)
	return False


def update_domain(sudoku, var, unassigned_variables):
	for j in range(len(unassigned_variables)):
		curr_var = unassigned_variables[j]
		if((var[0] == curr_var[0]) or 
			(var[1] == curr_var[1]) or 
			(var[0] / 3 * 3 + var[1] / 3 == curr_var[0]/3 * 3 + curr_var[1])):
			for k in curr_var[2]:
				if not common.can_yx_be_z(sudoku, curr_var[0], curr_var[1], k):
					curr_var[2].remove(k)
				if not curr_var[2]:
					return False
	return True	



def copy_list(my_list):
	new_list  = []
	for l in my_list:
		if (isinstance(l,list)):
			new_list.append(copy_list(l))			
		else:
			new_list.append(l)
	return new_list



def sudoku_mrv(sudoku):
	# PUT YOUR CODE HERE
	# access the sudoku using "sudoku[y][x]"
	# y between 0 and 9
	# x between 0 and 9
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds 
	# explored is optional but recommended 
	variables.counter=0	
	unassigned_variables = []	
	domain = []
	get_unassigned_variables(unassigned_variables, sudoku)
	get_domain_unassigned_variables(unassigned_variables,  sudoku)
	mrv(sudoku,unassigned_variables)
	return variables.counter


def mrv(sudoku, unassigned_variables):
	variables.counter += 1
	if not unassigned_variables:
		return True 
	id = get_mrv(sudoku, unassigned_variables)
	var = copy_list(unassigned_variables[id])
	unassigned_variables.pop(id)
	for val in var[2]:
		if (common.can_yx_be_z(sudoku, var[0], var[1],val)):
			sudoku[var[0]][var[1]] = val
			result = mrv(sudoku, unassigned_variables)
			if result:
				return result
			sudoku[var[0]][var[1]] = 0
	unassigned_variables.insert(0, var)
	return False 



def get_mrv(sudoku, unassigned_variables):
	update_domain_mrv(unassigned_variables, sudoku)
	for i in range(9):
		for j in range(len(unassigned_variables)):
			if (len(unassigned_variables[j][2]) == i):
				return j
	return 0

def update_domain_mrv(unassigned_variables, sudoku):
	for i in range(0, len(unassigned_variables)):
		var = unassigned_variables[i]
		unassigned_variables[i]
		x = []
		for j in order_domain_values:
			if common.can_yx_be_z(sudoku, var[0], var[1], j):
				x.append(j)
		unassigned_variables[i][2] = x	




