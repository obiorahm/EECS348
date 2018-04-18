import common
def astar_search(map):
	found = False
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	start_y, start_x, end_y, end_x = find_start_stop(map)
	man_dist = []
	manhattan_distance(map,end_y, end_x, man_dist)
	#print_map(man_dist)
	frontier = []
	path = []
	path.append([start_y, start_x, -1, -1])
	frontier.append([start_y, start_x, -1, -1, 0])
	return astar(map, path, frontier, man_dist) and set_path(map, path, [end_y, end_x])

def find_start_stop(map):
	found_start = False
	found_end = False
	for i in range(0, len(map)):
		for j in range(0, len(map[0])):
			if map[i][j] == 2:
				start_x = j
				start_y = i
				found_start = True
			if map[i][j] == 3:
				end_x = j
				end_y = i
				found_end = True
			if found_start and found_end:
				return start_y, start_x, end_y, end_x

def manhattan_distance(map, end_y, end_x, man_dist):
	for i in range(0, len(map)):
		man_dist.append([])
		for j in range(0, len(map[0])):
			if (map[i][j] == 0 or
				map[i][j] == 2 or 
				map[i][j] == 3):
				if (end_x > j):
					x_dist = end_x - j
				else: 
					x_dist = j - end_x 
				if(end_y > i):
					y_dist = end_y - i
				else:
					y_dist = i - end_y
				man_dist[i].append(x_dist + y_dist)
			else:
				man_dist[i].append(-1)



def astar(map, path, frontier, man_dist):
	if(not frontier):
		return False
	curr_node = min_frontier(frontier, man_dist)
	y = curr_node[0]
	x = curr_node[1]
	p_y = curr_node[2]
	p_x = curr_node[3]
	dist = curr_node[4]
	if (map[y][x] == 4 or map[y][x] == 1):
		return astar(map, path, frontier, man_dist)
	if (map[y][x] == 3):
		return True
	if (map[y][x] == 0 or map[y][x] == 2):
		map[y][x] = 4
		new_dist = dist + 1
		frontier_append(map, path, frontier, y, x + 1, y, x, new_dist)
		frontier_append(map, path, frontier, y + 1, x, y, x, new_dist)
		frontier_append(map, path, frontier, y, x - 1, y, x, new_dist)
		frontier_append(map, path, frontier, y - 1, x, y, x, new_dist)
		return astar(map, path, frontier, man_dist)


def frontier_append(map, path, frontier, y, x, p_y, p_x, new_dist):
	if ((y < len(map)) and
		(x < len(map[0])) and
		(y >= 0) and
		(x >= 0)):
		path.append([y, x, p_y, p_x])
		frontier.append([y,x,p_y, p_x, new_dist])


def min_frontier(frontier, man_dist):
	j = -1
	if frontier:
		min_frontier = frontier[0]
		j = 0
		for i in range(0, len(frontier)):
			curr_frontier = frontier[i]
			min_fn = min_frontier[4] + man_dist[min_frontier[0]][min_frontier[1]]
			curr_fn = curr_frontier[4] + man_dist[curr_frontier[0]][curr_frontier[1]]
			if(min_fn > curr_fn):
				min_frontier = curr_frontier
				j = i
			elif (min_fn == curr_fn):
				if(curr_frontier[1] < min_frontier[1]):
					min_frontier = curr_frontier
					j = i
				elif(curr_frontier[0] < min_frontier[0]):
					min_frontier = curr_frontier
					j = i
		if j != -1:
			frontier.pop(j)
		return min_frontier


def set_path(map, path, end):
        getDest = False
        j = []
        for i in range(len(path) - 1,-1, -1):
                currPath = [path[i][0], path[i][1]]
                if (getDest == False):
                    if ( currPath == end):
                        getDest = True
                        y = end[0]
                        x = end[1]                         
                        map[y][x] = 5
                        j = [path[i][2], path[i][3]]
                else:
                    if currPath == j:
                            y = path[i][0]
                            x = path[i][1] 
                            j = [path[i][2], path[i][3]]
                            map[y][x] = 5
        return True


b_map = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,1,1,1,1,1,1],
        [0,2,1,0,1,0,0,0,0,0],
        [1,1,1,0,1,0,1,1,1,0],
        [0,0,0,0,1,0,1,0,1,0],
        [0,0,1,0,1,0,1,0,1,0],
        [0,0,1,0,0,0,1,0,1,0],
        [0,0,1,1,1,1,1,0,1,0],
        [0,0,0,0,0,0,0,0,1,0],
        [0,0,1,1,1,1,1,1,1,0],
        [0,0,1,0,0,0,1,0,3,1],
        [1,0,0,0,1,0,1,0,0,1]]

ap_map = [
        [2,0,0,0,0,0,0,0,0,0],
        [0,1,0,1,1,1,1,1,1,1],
        [0,1,0,0,0,0,0,0,0,0],
        [0,1,0,1,1,1,1,1,1,1],
        [0,1,1,1,0,0,0,0,0,1],
        [0,1,0,1,0,1,0,1,1,0],
        [0,1,0,1,0,1,0,0,0,0],
        [0,1,0,0,0,1,1,1,1,0],
        [0,0,1,1,1,1,1,1,1,0],
        [1,0,1,1,1,1,1,1,1,0],
        [1,0,1,1,1,1,1,1,1,0],
        [1,0,0,0,0,0,0,0,0,3]]

a_map =[[0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,0,1,0,1],
        [0,3,0,0,0,1,0,1,0,1],
        [1,1,1,1,0,1,0,1,0,1],
        [0,0,0,1,0,1,0,1,0,1],
        [0,1,0,0,0,1,0,1,0,1],
        [1,1,1,1,0,1,0,1,0,1],
        [0,0,0,0,0,0,0,1,0,1],
        [0,1,1,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,1,0,1],
        [0,1,1,1,1,1,1,1,2,0],
        [0,0,0,0,0,0,0,0,1,0]] 

c_map = [[2,0,0,0,0,0,1,1,1,1],
		[1,1,1,1,1,0,1,1,1,1],
		[1,1,1,1,1,0,1,1,1,1],
		[1,0,0,1,1,0,1,1,1,1],
		[1,1,0,1,1,0,1,1,1,1],
		[1,1,0,0,0,0,0,0,1,1],
		[1,1,1,0,1,1,1,0,1,1],
		[1,1,0,0,1,1,1,0,1,1],
		[1,1,0,1,0,3,0,0,1,1],
		[1,1,1,1,1,1,0,1,1,1],
		[1,1,1,1,1,1,0,1,1,1],
		[1,0,0,0,0,0,0,0,0,1]]

d_map = [[1,0,0,0,1,2,0,0,1,1],
		[1,0,1,0,1,0,1,0,1,1],
		[1,0,1,0,1,0,1,0,1,1],
		[1,0,1,0,1,0,1,0,1,1],
		[1,0,1,0,1,0,1,0,1,1],
		[1,0,1,0,1,0,1,0,1,1],
		[1,3,1,0,1,0,1,0,1,1],
		[1,0,1,0,0,0,1,0,1,1],
		[1,0,1,1,1,1,1,0,1,1],
		[1,0,0,0,0,0,0,0,1,1],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1]]    

e_map = [[1,1,1,2,3,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1]]

f_map = [[1,1,1,2,0,0,0,1,1,0],
		[1,1,1,1,1,1,0,1,1,0],
		[1,1,1,1,1,1,0,1,1,1],
		[1,1,1,1,1,1,0,1,1,1],
		[1,1,1,0,0,1,0,0,0,1],
		[1,1,1,0,1,1,0,1,1,1],
		[1,1,1,0,1,1,0,1,1,1],
		[1,1,1,0,1,1,0,1,1,1],
		[1,1,1,0,1,1,0,1,1,1],
		[1,1,0,0,0,0,0,1,1,1],
		[1,1,1,1,1,1,0,1,0,0],
		[1,1,1,1,1,1,0,1,0,3]]

g_map = [[0,0,0,0,2,0,0,0,0,0],
		[0,1,1,1,1,1,1,1,1,0],
		[0,1,0,0,0,0,0,0,0,0],
		[0,1,1,1,1,1,1,1,1,0],
		[0,0,0,0,0,0,0,1,1,0],
		[1,1,1,1,1,1,1,1,1,0],
		[0,1,1,0,0,0,0,0,1,0],
		[0,1,1,0,1,1,1,0,1,0],
		[0,1,1,0,1,3,1,0,1,0],
		[0,1,1,0,1,0,1,0,1,0],
		[0,1,1,0,0,0,1,0,1,0],
		[0,0,0,0,1,1,1,0,0,0]]



#print(bf_search(b_map))
def print_map(a_map):
        for i in range(0, len(a_map)):
                for j in range(0, len(a_map[0])):
                        print (a_map[i][j], end="")
                print ('\t')

'''
h = df_search(a_map)
print(h)
print_map(a_map)
j = df_search(ap_map)
print(j)
print_map(ap_map)
j = df_search(b_map)
print(j)
print_map(b_map)
'''

h = astar_search(a_map)
print(h)
print_map(a_map)

j = astar_search(ap_map)
print(j)
print_map(ap_map)

j = astar_search(b_map)
print(j)
print_map(b_map)

j = astar_search(c_map)
print(j)
print_map(c_map)

j = astar_search(d_map)
print(j)
print_map(d_map)

j = astar_search(e_map)
print(j)
print_map(e_map)

j = astar_search(f_map)
print(j)
print_map(f_map)

j = astar_search(g_map)
print(j)
print_map(g_map)
