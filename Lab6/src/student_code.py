import common
#import matplotlib.pyplot as plt

def part_one_classifier(data_train,data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 1
	#for f in data_train:
	#	print (f)
	#print (len(data_train))
	n = 2
	w = train(data_train, data_test, n, 200, 0.05)	
	#binary_classifier(data_train, data_test)
	test(data_test,w, n)
	return
'''
def binary_classifier(data_train, data_test):
	w = [0.0 for x in range(3)]

	accuracy = []
	index = []
	v = 0
	error = 1.0	
	t = 1
	count = 0
	while (error > 0.05 and count < 200):
		count += 1
		for i, f in enumerate(data_train):
			sumy = w[0] * f[0] + w[1] * f[1] + w[2]
			y = 0
			if sumy >= 0.0:
				y = 1.0
			else:
				y = -1.0

			classes = [-1.0, 1.0]	
			y_star = f[2]
			if (y != classes[int(y_star)]):
				w[0] += (classes[int(y_star)] * f[0])
				w[1] += (classes[int(y_star)] * f[1])
				w[2] += classes[int(y_star)] 
				v = v + 1
				error = v/ (t + i)
				#print (v, t + i )
				accuracy.append(error)
				index.append(v)
		t = t + i


	print (error)
	plt.plot(index, accuracy)
	plt.show()	

	for f in data_test:
		y = (w[0] * f[0]) + (w[1] * f[1]) + w[2]
		if y >= 0:
			f[2] = 1.0		
		else:
			f[2] = 0.0	
'''			

def train(data_train, data_test, n, epoch, acc):
	# prediction class array
	y = [0.0 for x in range(n)]

	# weights array
	w = [[0.0 for x in range(len(data_train[0]))] for x in range(n)]

	# feature bias all set to 1
	fb = [1.0 for x in range(len(data_train))]

	# accuracy array of n_error/ total_trained
	l_accuracy = []

	# acc_index array of n_errors
	l_n_errors = []

	#v = 0 no of errors
	n_errors = 0.0

	# error = 1.0 fraction of errors in trained  
	ave_error = 1.0

	#t = 1 total number trained 
	total_trained = 1.0

	# count = 0 epoch_count
	epoch_count = 0


	while (ave_error > acc and epoch_count < epoch):	
		epoch_count += 1
		for j,f in enumerate(data_train):
			for i in range(len(y)):
				y[i] = w[i][0] * f[0] +  w[i][1] * f[1] + w[i][2]
			max_y = max(y)
			index = y.index(max_y)
			y_star = f[2]
			new_id = int(y_star)
			
			if index != new_id:
				w[index][0] = w[index][0] - f[0]
				w[index][1] = w[index][1] - f[1]
				w[index][2] = w[index][2] - fb[j]
				w[new_id][0] = w[new_id][0] + f[0]
				w[new_id][1] = w[new_id][1] + f[1]
				w[new_id][2] = w[new_id][2] + fb[j]
				n_errors += 1
				ave_error = n_errors/ (total_trained + j)
				#print (v, t + i )
				l_accuracy.append(ave_error)
				l_n_errors.append(n_errors)
		total_trained += j				

	#print_accuracy(l_accuracy, l_n_errors)
	return w	

def test(data_test, w, n):
	y = [0 for x in range(n)]
	for f in data_test:
		for i in range(len(y)):
			y[i] = w[i][0] * f[0] +  w[i][1] * f[1] + w[i][2]
		max_y = max(y)
		index = y.index(max_y)
		f[2] = float(index)
	return	


def part_two_classifier(data_train,data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 8
	n = 9
	w = train(data_train, data_test, n, 3000, 0.05)
	test(data_test, w, n)
	return
'''
def print_accuracy(l_accuracy, l_n_errors):
	print (l_accuracy[len(l_accuracy) - 1])
	print (l_n_errors[len(l_n_errors) - 1])
	plt.plot(l_n_errors, l_accuracy)
	plt.show()		


'''