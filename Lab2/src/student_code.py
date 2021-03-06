import common
def astar_search(map):
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	start_y, start_x, end_y, end_x = find_start_stop(map)
	if ((start_y == -1) or (end_y == -1)):
		return False 
	end = [end_y, end_x]
	frontier = []
	path = []
	path.append([start_y, start_x, -1, -1])
	frontier.append([start_y, start_x, -1, -1, 0])
	return astar(map, path, frontier, end) and set_path(map, path, end)

def find_start_stop(map):
	found_start = False
	found_end = False
	start_x = -1
	start_y = -1
	end_x = -1
	end_y = -1
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
	return start_y, start_x, end_y, end_x



def astar(map, path, frontier, end):
	if(not frontier):
		return False
	curr_node = min_frontier(frontier, end)
	y = curr_node[0]
	x = curr_node[1]
	p_y = curr_node[2]
	p_x = curr_node[3]
	dist = curr_node[4]	
	if (map[y][x] == 4 or map[y][x] == 1):
		return astar(map, path, frontier, end)
	if (map[y][x] == 3):
		return True
	if (map[y][x] == 0 or map[y][x] == 2):
		map[y][x] = 4
		new_dist = dist + 1
		frontier_append(map, path, frontier, y, x + 1, y, x, new_dist)
		frontier_append(map, path, frontier, y + 1, x, y, x, new_dist)
		frontier_append(map, path, frontier, y, x - 1, y, x, new_dist)
		frontier_append(map, path, frontier, y - 1, x, y, x, new_dist)
		return astar(map, path, frontier, end)


def frontier_append(map, path, frontier, y, x, p_y, p_x, new_dist):
	if ((y < len(map)) and
		(x < len(map[0])) and
		(y >= 0) and
		(x >= 0)):
		path.append([y, x, p_y, p_x])
		frontier.append([y, x, p_y, p_x, new_dist])


def min_frontier(frontier, end):
	if frontier:
		m_frontier = frontier[0]
		j = 0
		for i in range(0, len(frontier)):
			c_frontier = frontier[i]
			min_fn = m_frontier[4] + abs(end[0] - m_frontier[0]) + abs(end[1] - m_frontier[1])
			curr_fn = c_frontier[4] + abs(end[0] - c_frontier[0]) + abs(end[1] - c_frontier[1])
			if(min_fn > curr_fn):
				m_frontier = c_frontier
				j = i
			elif (min_fn == curr_fn):
				if(c_frontier[1] < m_frontier[1]):
					m_frontier = c_frontier
					j = i
				elif(c_frontier[0] < m_frontier[0]):
					m_frontier = c_frontier
					j = i
		frontier.pop(j)
		return m_frontier


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
                        j = [path[i][2], path[i][3]]
                        map[y][x] = 5
                else:
                    if currPath == j:
                            y = path[i][0]
                            x = path[i][1] 
                            j = [path[i][2], path[i][3]]
                            map[y][x] = 5
        return True

ap_map = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,0,1,1,1,1,1,1,1],
        [0,1,0,0,0,0,0,0,0,0],
        [0,1,0,1,1,1,1,1,1,1],
        [0,1,1,1,0,0,0,0,0,1],
        [0,1,0,1,0,1,0,1,1,2],
        [0,1,0,1,0,1,0,0,0,0],
        [0,1,0,0,0,1,1,1,1,0],
        [0,0,1,1,1,1,1,1,1,0],
        [1,0,1,1,1,1,1,1,1,0],
        [1,0,1,1,1,1,1,1,1,0],
        [1,0,0,0,0,0,0,0,0,3]]
b_map = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,1,1,1,1,1,1],
        [0,2,1,0,1,0,0,0,0,2],
        [1,0,1,0,1,0,1,1,1,0],
        [0,0,0,0,1,0,1,0,1,0],
        [0,0,1,0,1,0,1,0,1,0],
        [0,0,1,0,0,0,1,0,1,0],
        [0,0,1,1,1,1,1,0,1,0],
        [0,0,0,0,0,0,0,0,1,0],
        [0,0,1,1,1,1,1,1,1,0],
        [0,0,1,0,0,0,1,0,3,1],
        [1,0,0,0,1,0,1,0,0,1]]

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

map1 =[[3,2,0,0,0,0,0,0,0,0],
       [1,1,1,1,1,1,1,1,1,0],
       [0,0,0,0,0,0,0,0,1,0],
       [0,1,1,1,1,1,1,0,1,0],
       [0,1,0,0,0,0,1,0,1,0],
       [0,1,0,1,1,0,1,0,1,0],
       [0,1,0,1,1,0,1,0,1,0],
       [0,1,0,1,0,0,1,0,1,0],
       [0,1,0,1,1,1,1,0,1,0],
       [0,1,0,0,0,0,0,0,1,0],
       [0,1,1,1,1,1,1,1,1,0],
       [0,0,0,0,0,0,0,0,0,0]]

map2 = [[3,0,0,0],
        [1,1,1,0],
        [0,0,0,0],
        [2,1,1,0]]

map3 = [[2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

map4=[[2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
      [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


map5 =[[2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
       [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
       [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
       [0,1,1,1,1,1,1,1,1,1,1,1,0,1,0],
       [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
       [0,1,1,1,1,1,1,1,1,1,1,1,0,1,0],
       [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
       [0,1,1,1,1,1,1,1,1,1,1,1,0,1,0],
       [3,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]



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

j = astar_search(ap_map)
print(j)
print_map(ap_map)

h = astar_search(a_map)
print(h)
print_map(a_map)

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

j = astar_search(map1)
print(j)
print_map(map1)

j = astar_search(map2)
print(j)
print_map(map2)

j = astar_search(map3)
print(j)
print_map(map3)

j = astar_search(map4)
print(j)
print_map(map4)

j = astar_search(map5)
print(j)
print_map(map5)

