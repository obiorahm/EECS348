import common
import math
import matplotlib.pyplot as plt

def detect_slope_intercept(image):
	# PUT YOUR CODE HERE
	# access the image using "image[chanel][y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# set line.m and line.b
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	line=common.Line()
	line.m=0
	line.b=0
	#print ("Hey there, I'm using whatsApp")
	#print(image[0][:][100])
	#print(image[1][:][100])
	#print(image[2][:][100])



	hough = common.init_space(20, 2000)
	l_m = []
	l_b = []

	for i in range(480):
		for j in range (640):
			if ((image[0][i][j] == image[1][i][j]) and
				(image[1][i][j] == image[2][i][j]) and 
				(image[2][i][j] == 0)):
				for m in range(-10, 10):
					b = (m * -j) + i
					if (b > -1000 and b < 1000):
						l_m.append (m)
						l_b.append(b)
	draw_graph(b, m)

	#print hough
	return line

def detect_normal(image):
	# PUT YOUR CODE HERE
	# access the image using "image[chanel][y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# set line.theta and line.r
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	line=common.Line()
	line.r=0
	line.theta=0
	return line

def detect_circles(image):
	# PUT YOUR CODE HERE
	# access the image using "image[chanel][y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	return 0
				
def draw_graph(l_accuracy, l_n_errors):
	plt.plot(l_n_errors, l_accuracy)
	plt.show()				