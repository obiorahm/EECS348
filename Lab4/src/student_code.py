import common
import copy

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
	get_domain_unassigned_variables(unassigned_variables, domain, sudoku)
	print fowardchecking(sudoku, 0, domain, unassigned_variables)
	return variables.counter


def get_domain_unassigned_variables(unassigned_variables, domain, sudoku):
	for i in range(0, len(unassigned_variables)):
		var = unassigned_variables[i]
		domain.append([])
		for j in order_domain_values:
			if common.can_yx_be_z(sudoku, var[0], var[1], j):
				domain[i].append(j)





def fowardchecking(sudoku, n, domain, unassigned_variables):
	variables.counter += 1
	if n == len(unassigned_variables):
		return True
	var = unassigned_variables[n]
	for val in domain[n]:
		sudoku[var[0]][var[1]] = val
		curr_domain = copy.deepcopy(domain)													
		curr_domain, x = update_domain(sudoku, var, curr_domain, unassigned_variables, n)
		#print("update_domain ",x)
		if x:
			result = fowardchecking(sudoku, n + 1, curr_domain, unassigned_variables)
			if result: 
				return result				
		sudoku[var[0]][var[1]] = 0							
	return False

def update_domain(sudoku, var, domain, unassigned_variables,n):
	p = curr_domain = list(domain)	
	for j in range(n + 1, len (unassigned_variables)):
		curr_var = unassigned_variables[j]
		if((var[0] == curr_var[0]) or 
			(var[1] == curr_var[1]) or 
			(var[0] / 3 * 3 + var[1] / 3 == curr_var[0]/3 * 3 + curr_var[1])):
			for k in domain[j]:
				#print(k,"k")
				#print(i, "i")
				if not common.can_yx_be_z(sudoku, curr_var[0], curr_var[1], k):
					p[j].remove(k)
				if not p[j]:
					return p, False
	#print("domain")
	#print_table(domain)				
	return p, True

def copy_list(list):
	new_list 



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
