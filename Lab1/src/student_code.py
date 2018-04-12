from collections import deque
import common
        

def df_search(map):
	found = False
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	x, y = find_start(map)
	print ("x: ", x)
	print ("y: ", y)
	pathx = []
	pathy = []
	p = push_nodes(map, y, x, pathx, pathy)
	print (p)
	return p and set_path(map, pathx, pathy)

def bf_search(map):
	found = False;
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	return bfs_helper(map)


#find the start state:
def find_start(map):
    for y in range(0, common.constants.MAP_HEIGHT - 1):
        for x in range(0, common.constants.MAP_WIDTH - 1):
            if (map[y][x] == 2):
                return x, y

def bfs_helper(map):
    x, y = find_start(map)
    start = [x,y]
    stack = []
    stack.append([y,x])
    path = []
    path.append([y,x])
    parent = []
    parent.append([-1,-1])
    end = []
    return bfs(map, path, parent,stack,start, end) and set_path_bfs(map, path, parent, start, end)
        
        
def bfs(map, path, parent, stack, start, end):
    if not stack:
        return False
    y = stack[0][0]
    x = stack [0][1]   
    stack.pop(0)
    if (map[y][x] == 3):
        map[y][x] = 4
        return True    
    if(map[y][x] == 4):
        return bfs(map, path, parent,stack, start, end)
        
    if (map[y][x] == 0 or map[y][x] == 2):
        map[y][x] = 4
        v = stack_append(map, stack, path, parent, end, [y,x], y,x + 1)
        w = stack_append(map, stack, path, parent, end, [y,x], y + 1, x)
        r = stack_append(map, stack, path, parent, end, [y,x], y, x - 1)
        s = stack_append(map, stack, path, parent, end, [y,x], y - 1, x)

        return bfs(map, path, parent, stack, start, end)

def deep_pop(stack, path, x,y):
        while (path and stack and ([x,y]!= path[0])):
                path.pop(0)
                
def stack_append(map, stack,path, parent, end, curr_parent, y,x):
    if((y >= 0 ) and
        (y < len(map)) and
        (x >= 0) and
        (x < len(map[0])) and
        ((map[y][x] == 0 or map[y][x] == 3))):
            if (map[y][x] == 0):
                parent.append(curr_parent)
                path.append([y,x])            
                stack.append([y,x])
            elif(map[y][x] == 4):
                parent.append(curr_parent)
                path.append([y,x])
            elif(map[y][x] == 3):
                parent.append(curr_parent)
                path.append([y,x])
                stack.append([y,x])
                end.append([y,x])



def push_nodes(map, y, x, pathx, pathy):
    if ((y < 0)
        or (x < 0)
        or (y >= len(map))
        or (x >= len(map[0]))
        or (map[y][x] == 4)
        or (map[y][x] == 5)):
        return False
    if (map[y][x] == 1):
        return False 
    if (map[y][x] == 3):
        pathx.append(x)
        pathy.append(y)
        return True
    if (map[y][x] == 0 or map[y][x] == 2):
        map[y][x] = 4
        v = (push_nodes(map, y, x + 1, pathx, pathy) or
         push_nodes(map, y + 1, x, pathx, pathy) or
         push_nodes(map, y, x - 1, pathx, pathy) or
         push_nodes(map, y - 1, x, pathx, pathy))
        if v:
                pathx.append(x)
                pathy.append(y)
        return v

def set_path(map, pathx,pathy):
        if pathx:
                for i in range(0, len(pathx)):
                        x = pathx[i]
                        y = pathy[i]
                        map[y][x] = 5
                return True
        else:
                return False

def set_path_bfs(map, path, parent, start, end):
        getDest = False
        j = []
        for i in range(len(path) - 1,-1, -1):
                #print(parent[i])
                if (getDest == False):
                    if (path[i] == end[0]):
                        getDest = True
                        y = end[0][0]
                        x = end[0][1]                         
                        map[y][x] = 5
                        j = parent[i]
                else:
                    if path[i] == j:
                            y = path[i][0]
                            x = path[i][1] 
                            j = parent[i]
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

#print(bf_search(b_map))
#def print_map(a_map):
#        for i in range(0, len(a_map)):
#                for j in range(0, len(a_map[0])):
#                        print (a_map[i][j], end="")
#                print ('\t')

#h = bf_search(a_map)
#print(h)
#print_map(a_map)

#j = bf_search(ap_map)
#print(j)
#print_map(ap_map)

#j = bf_search(b_map)
#print(j)
#print_map(b_map)




        
