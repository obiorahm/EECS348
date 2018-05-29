import common
import matplotlib.pyplot as plt

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
	w = train(data_train, data_test, n, 500, 0.05)	
	#binary_classifier(data_train, data_test)
	test(data_test,w, n)
	return
		

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
	total_trained = 0.0

	# count = 0 epoch_count
	epoch_count = 0

	best_w = [0.0,0.0,0.0]
	best_accuracy = 1.0

	past_acc = 1.0
	present_acc = 0.0

	#start_time = time.time()

#	while (ave_error > acc and epoch_count < epoch):	
	while (epoch_count < epoch):	
#	while (ave_error > acc):	
		epoch_count += 1
		for j,f in enumerate(data_train):
			for i in range(len(y)):
				y[i] = w[i][0] * f[0] +  w[i][1] * f[1] + w[i][2]
			max_y = max(y)
			index = y.index(max_y)
			y_star = f[2]
			new_id = int(y_star)
			
			if index != new_id:
				w[index][0] -= f[0]
				w[index][1] -= f[1]
				w[index][2] -=  1.0
				w[new_id][0] += f[0]
				w[new_id][1] += f[1]
				w[new_id][2] += 1.0
				n_errors += 1
				ave_error = n_errors/ (total_trained + j + 1)
				#print (v, t + i )
				l_accuracy.append(ave_error)
				l_n_errors.append(n_errors)
				if ave_error < best_accuracy:
					best_accuracy = ave_error
					best_w = list(w)
		total_trained += j	
	#print ("epoch count: ", epoch_count, "training data length: ", len(data_train))			
	#print(l_accuracy[len(l_accuracy) - 1])
	#print ("accuracy: ", best_accuracy)
	draw_graph(l_accuracy, l_n_errors)
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
	w = train(data_train, data_test, n, 20000, 0.05)
	test(data_test, w, n)
	return

def draw_graph(l_accuracy, l_n_errors):
	print (l_accuracy[len(l_accuracy) - 1])
	print (l_n_errors[len(l_n_errors) - 1])
	plt.plot(l_n_errors, l_accuracy)
	plt.show()		


