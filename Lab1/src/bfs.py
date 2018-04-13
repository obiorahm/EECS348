def bfs(map, path, parent, curr_parent, stack, start, end):
	if not stack:
		return False:
	y = stack[0][0]
	x = stack[0][1]
	stack.pop(0)
	if (map[y][x] == 3):
		map[y][x] = 4
		parent.append(curr_parent)
		path.append([y,x])
		end.append([y,x])
		return True
	if((y < 0) or
		(y >= len(map)) or
		(x < 0) or 
		(x >= len(map))):
		return bfs(map, path, parent, [y,x],stack, start, end)
	if(map[y][x] == 4):
		parent.append(curr_parent);
		path.append([y][x])
		return bfs(map, path, parent, [y,x], stack, start, end)
	if(map[y][x] == 0 or map[y][x] == 2)
		path.append([y,x])
		parent.append(curr_parent)
		stack.append(y, x + 1)
		stack.append(y + 1, x)
		stack.append(y, x - 1)
		stack.append(y - 1, x)
		return bfs(map, path, parent, [y,x], stack, start, end)