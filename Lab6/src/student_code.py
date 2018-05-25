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
	binary_classifier(data_train, data_test)
	return

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

		#print f[0], f[1], w[0], w[1], y, y_star, classes[int(y_star)]

	print (w[0])
	print (w[1])
	print (w[2])
	plt.plot(index, accuracy)
	plt.show()	

	for f in data_test:
		y = (w[0] * f[0]) + (w[1] * f[1]) + w[2]
		if y >= 0:
			f[2] = 1.0
			#print (y)			
		else:
			f[2] = 0.0	
			#print (y)


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
	y = [0.0 for x in range(9)]
	w = [[0.0 for x in range(3)] for x in range(9)]
	fb = [1.0 for x in range(len(data_train))]

	for b in w:
		b[2] = 0.0
	accuracy = []
	acc_index = []
	v = 0
	error = 1.0	
	t = 1
	count = 0
	while (error > 0.05 and count < 3000):	
		count += 1
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
				v = v + 1
				error = v/ (t + j)
				#print (v, t + i )
				accuracy.append(error)
				acc_index.append(v)
		t = t + j				
		#print w, index, y_star
		#print f[0], f[1], w[index][0], w[index][1], index, y_star  

	print (accuracy[len(accuracy) - 1])
	print (acc_index[len(acc_index) - 1])
	print (w[2])
	plt.plot(acc_index, accuracy)
	plt.show()	

	for f in data_test:
		for i in range(len(y)):
			y[i] = w[i][0] * f[0] +  w[i][1] * f[1] + w[i][2]
		max_y = max(y)
		index = y.index(max_y)
		f[2] = float(index)
	return

