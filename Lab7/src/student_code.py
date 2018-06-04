import common
import math
#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#from PIL import Image
#import cv2
#import random


#import matplotlib.pyplot as plt

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

	hough_space = [[[0.0 for x in range(3)] for x in range(2000)] for x in range(2000)]	
	#print("done")

	max_x = 0
	max_y = 0
	incr = 20.0/2000.0

	for i in range(len(image[0])):		
		for j in range (len(image[0][0])):
			if ((image[2][i][j] == 0) and 
				(image[0][i][j] == image[1][i][j]) and
				(image[1][i][j] == image[2][i][j])):
				m = -10.0
				while (m < 10.0):
					b = (m * -j) + i
					if (b >= -1000.0 and b < 1000.0):
						# select bin[y][x]
						y = int((b + 1000))
						x = int((m + 10) * 100)
						hough_space[y][x][0] = hough_space[y][x][0] + b
						hough_space[y][x][1] = hough_space[y][x][1] + m
						hough_space[y][x][2] = hough_space[y][x][2] + 1	
						if (hough_space[y][x][2] > hough_space[max_y][max_x][2]):
							max_y = y
							max_x = x												
					m += incr
	max_vote = hough_space[max_y][max_x]
	line.b = max_vote[0]/max_vote[2]
	line.m = max_vote[1]/max_vote[2]	

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

	max_x = 0
	max_y = 0	

	H = [[[0.0 for x in range(3)] for x in range(1800)] for x in range(1800)]


	pi = 3.14159265
	incr = pi/1800.0


	for i in range(len(image[0])):		
		for j in range (len(image[0][0])):
			if ((image[2][i][j] == 0) and 
				(image[0][i][j] == image[1][i][j]) and
				(image[1][i][j] == image[2][i][j])):
				theta = 0.0
				while theta < pi:
					w = j * math.cos(theta) + i * math.sin(theta)
					if (w >= -900.0 and w < 900.0):
						y = int(theta * (1.0/incr))
						x = int(w + 900.0)

						H[y][x][0] = H[y][x][0] + theta
						H[y][x][1] = H[y][x][1] + w
						H[y][x][2] = H[y][x][2] + 1.0	
						if (H[y][x][2] > H[max_y][max_x][2]):
							max_y = y
							max_x = x

					theta += incr

	line.theta = H[max_y][max_x][0]/H[max_y][max_x][2]
	line.r = H[max_y][max_x][1]/H[max_y][max_x][2]



	return line

def detect_circles(image):
	# PUT YOUR CODE HERE
	# access the image using "image[chanel][y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# to create an auxiliar bidimensional structure 
	# you can use "space=common.init_space(heigh, width)"
	#new_image = [[[0.0 for x in range(len(image))] for x in range(len(image[0][0]))] for x in range(len(image[0]))]

	new_image = [[[0.0 for x in range (len(image[0][0]))] for x in range(len(image[0]))] for x in range(len(image))]


	hough_space = [[0.0 for x in range(len(image[0]))] for x in range(len(image[0][0]))]


	X = 0
	Y = 1
	RADIUS = 30.0
	GRADIENT = 2
	RADIUS_SQUARED = RADIUS * RADIUS
	MAX_PIXEL_VALUE = 255.0

	max_gradient = 0.0
	min_gradient = 0.0



	#print(new_image)
	#print (len(image[0][0]))
	#print (len(image[0]))
	#print (len(image))

	#print (len(new_image[0][0]))
	#print (len(new_image[0]))
	#print (len(new_image))


	# edge detection values placed in new_image
	for i in range(len(image[0])):
		for j in range(len(image[0][0])):		
			sobel(i, j, image, new_image, X)
			sobel(i, j, image, new_image, Y)

			new_image[GRADIENT][i][j] = (math.sqrt(new_image[X][i][j] * new_image[X][i][j] + new_image[Y][i][j] * new_image[Y][i][j]))

			curr_gradient = new_image[GRADIENT][i][j]

			min_gradient = set_min(min_gradient, curr_gradient)
			max_gradient = set_max(max_gradient, curr_gradient)

	#print ("minimum gradient ", min_gradient)
	#print ("maxmum gradient ", max_gradient)


	#normalize new_image
	s = []
	for k in range(len(new_image)):
		v = []
		for i in range(len(new_image[0])):
			w = []
			for j in range(len(new_image[0][0])):
				curr_image = (new_image[GRADIENT][i][j]/ max_gradient) * MAX_PIXEL_VALUE
				w.append(curr_image)
			v.append(w)
		s.append(v)		


	p = []
	q = []
	# now find number of circles:
	for i in range(1,len(s[0])):
		for j in range(len(s[0][0])):
			val = s[GRADIENT][i][j]
			if val == MAX_PIXEL_VALUE:
				a = 0.0
				while a < 640.0:
					x_minus_a_squared = (j - a) * (j - a)
					if (x_minus_a_squared < RADIUS_SQUARED):					
						b = math.sqrt(RADIUS_SQUARED - x_minus_a_squared) + i
						if (b >= 0.0 and b < 480.0):
							hough_space[int(a)][int(b)] += 1
							p.append(a)
							q.append(b)
					a += 1.0


	count_circles = 0
	for i in range(len(hough_space)):
		for j in range(len(hough_space[0])):
			if hough_space[i][j] >= 20:
				#print (hough_space[i][j])
				count_circles += 1

	#show_image(image)
	#x = input("enter a number")
	#show_image(s)
	#y = input("enter another number")
	#plot_graph(p,q)
	#c = [0.001 for x in range(len(p))]
	#y = np.dstack(s)
	#print("shape",y.shape)
	#plt.imshow(image)
	#plt.imshow(new_image)
	#plt.scatter(p, q, s=c)	
	#plt.show()						

	'''

	img = mpimg.imread('../circles1.bmp')
	imgplot = plt.imshow(image)
	plt.show()
	
	print (image[2][250])
	print(new_image[2][250])



	print(new_image[400])
	'''	
	return count_circles

def show_image(s):
	y = np.dstack(s)
	plt.imshow(y)
	plt.show()

def plot_graph(p,q):
	c = [0.001 for x in range(len(p))]	
	plt.scatter(p, q, s=c)	
	plt.show()			

def sobel(i, j, image, new_image, orientation):
	sobel = [[
				[1, 0, -1],
				[2, 0, -2],
				[1, 0, -1]
			],[
				[1, 2, 1],
				[0, 0, 0],
				[-1, -2, -1]			
			]]			

	#print("i = ", i, "j = ", j)
	new_image[orientation][i][j] = convolution(sobel[orientation], i, j, image)

	




def convolution(sobel, i, j, image):

	return 	((sobel[2][2] * gray_scale(image, i + 1, j + 1)) + 
			(sobel[1][2] * gray_scale(image, i, j + 1)) +
			(sobel[0][2] * gray_scale(image, i - 1, j + 1)) +
			(sobel[2][1] * gray_scale(image, i + 1, j)) +
			(sobel[1][1] * gray_scale(image, i, j))+
			(sobel[0][1] * gray_scale(image, i - 1, j)) +
			(sobel[2][0] * gray_scale(image, i + 1, j - 1)) +
			(sobel[1][0] * gray_scale(image, i, j - 1)) +
			(sobel[0][0] * gray_scale(image, i - 1, j - 1)))


def gray_scale(image, i, j):
	if i < 0 or i > 479 or j < 0 or j > 639:
		return 255.0
	return (image[0][i][j] + image[1][i][j] + image[2][i][j]) / 3.0

def set_min(min_gradient, curr_gradient):
	GRADIENT = 2
	if (curr_gradient < min_gradient):
		return curr_gradient
	return min_gradient

def set_max(max_gradient, curr_gradient):
	GRADIENT = 2
	if (curr_gradient > max_gradient):
		return curr_gradient
	return max_gradient	


			