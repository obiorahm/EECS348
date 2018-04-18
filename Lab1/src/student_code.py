import common
        

def df_search(map):
        found = False
        # PUT YOUR CODE HERE
        # access the map using "map[y][x]"
        # y between 0 and common.constants.MAP_HEIGHT-1
        # x between 0 and common.constants.MAP_WIDTH-1
        if find_start(map):
            x, y = find_start(map)
        else:
            return False
        path = []
        return dfs(map, y, x, path) and set_path(map, path)

def bf_search(map):
        found = False;
        # PUT YOUR CODE HERE
        # access the map using "map[y][x]"
        # y between 0 and common.constants.MAP_HEIGHT-1
        # x between 0 and common.constants.MAP_WIDTH-1
        if find_start(map):
            x, y = find_start(map)
        else:
            return False
        stack = []
        stack.append([y,x,-1,-1])
        path = []
        end = []
        return bfs(map, path, stack, end) and set_path_bfs(map, path, end)


#find the start state:
def find_start(map):
    for y in range(0, len(map) - 1):
        for x in range(0, len(map[0]) - 1):
            if (map[y][x] == 2):
                return x, y


def bfs(map, path, stack, end):
        if not stack:
                return False
        y = stack[0][0]
        x = stack[0][1]
        p_y = stack[0][2]
        p_x = stack[0][3]
        stack.pop(0)
        if((y < 0) or
                (y >= len(map)) or
                (x < 0) or 
                (x >= len(map[0]))):
                return bfs(map, path, stack, end)
        if (map[y][x] == 3):
                map[y][x] = 4
                path.append([y, x, p_y, p_x])
                end.append(y)
                end.append(x)
                return True        
        if (map[y][x] == 1 or map[y][x] == 4):
                return bfs(map,path, stack, end)  
        if (map[y][x] == 0 or map[y][x] == 2):
                path.append([y, x, p_y, p_x])
                map[y][x] = 4
                stack.append([y, x + 1, y, x])
                stack.append([y + 1, x, y, x])
                stack.append([y, x - 1, y, x])
                stack.append([y - 1, x, y, x])
                return bfs(map, path, stack, end)        
        

def dfs(map, y, x, path):
    if ((y < 0)
        or (x < 0)
        or (y >= len(map))
        or (x >= len(map[0]))
        or (map[y][x] == 4)):
        return False
    if (map[y][x] == 1):
        return False 
    if (map[y][x] == 3):
        path.append([y,x])
        return True
    if (map[y][x] == 0 or map[y][x] == 2):
        map[y][x] = 4
        v = (dfs(map, y, x + 1, path) or
         dfs(map, y + 1, x, path) or
         dfs(map, y, x - 1, path) or
         dfs(map, y - 1, x, path))
        if v:
                path.append([y,x])
                
        return v

def set_path(map, path):
        if path:
                for i in range(0, len(path)):
                        y = path[i][0]
                        x = path[i][1]
                        map[y][x] = 5
                return True
        else:
                return False

def set_path_bfs(map, path, end):
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



