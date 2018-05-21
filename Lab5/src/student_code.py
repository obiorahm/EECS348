import common

def drone_flight_planner (map,policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle):
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# access the policies using "policies[y][x]"
	# access the values using "values[y][x]"
	# y between 0 and 5
	# x between 0 and 5
	# function must return the value of the cell corresponding to the starting position of the drone
	y, x = get_reward_pos(map)
	if x is None or y is None:
		return 0 
	return planner (map,policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, 1 - discount_per_cycle, 0, x, y)



policy = [common.constants.SOFF, common.constants.NOFF, common.constants.EOFF, common.constants.WOFF,
			common.constants.SON, common.constants.NON, common.constants.EON, common.constants.WON]

	

def planner (map,policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle, k, x, y):
	#for k in range(20):
	copy_values = copy_list(values)
	for i in range (len (map)):
		for j in range (len (map[0])):
			if map[i][j] == 2:
				values[i][j] = delivery_fee
				policies[i][j] = common.constants.EXIT
			elif map[i][j] == 3:
				values[i][j] = -1 * dronerepair_cost
				policies[i][j] = common.constants.EXIT
			else:
				if k > (abs(y - i) + abs(x - j)) - 1 :
					sum_rewards = sum_of_rewards(map, copy_values, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle, i, j)
					maximum = max(sum_rewards)
					values[i][j] = maximum
					index = sum_rewards.index(maximum)
					policies[i][j] = policy[index]
			
	if difference(values, copy_values):
		return get_start_value(map,values)
	else:
		return planner (map, policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle, k + 1, x, y)


def get_start_value(map,values):
	for i in range(len(map)):
		for j in range(len(map[0])):
			if map[i][j] == 1:
				return values[i][j]

def get_reward_pos(map):
	for i in range(len(map)):
		for j in range(len(map[0])):
			if map[i][j] == 2:
				return i, j


def print_values (values):
	for i in range(len(values)):
		for j in range(len(values[0])):
			print values[i][j], 
        print '\n'


def sum_of_rewards (map, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle, i, j):
	bd = -battery_drop_cost
	death = -dronerepair_cost
	win = delivery_fee 
	reward = [ bd, bd, win, death, 0]
	Rsas = reward[bounce(map, i, j, 4)]
	bounce_val = values[i][j]


	east_off = ((0.15 * (Rsas + (discount_per_cycle * bounce(values, i - 1,j, bounce_val))))
				+ (0.15 * (Rsas + (discount_per_cycle * bounce(values, i + 1, j,bounce_val))))
				+ (0.70 * (Rsas + (discount_per_cycle * bounce(values, i, j + 1, bounce_val)))))


	west_off = ((0.15 * (Rsas + (discount_per_cycle * bounce(values, i - 1, j, bounce_val))))
				+ (0.15 * (Rsas + (discount_per_cycle * bounce(values, i + 1, j, bounce_val))))
				+ (0.70 * (Rsas + (discount_per_cycle * bounce(values, i, j - 1, bounce_val)))))

	south_off 	= ((0.15 * (Rsas + (discount_per_cycle * bounce(values, i, j - 1, bounce_val))))
				+ (0.15 * (Rsas + (discount_per_cycle * bounce(values, i, j + 1, bounce_val))))
				+ (0.70 * (Rsas + (discount_per_cycle * bounce(values, i + 1, j, bounce_val)))))

	north_off  = ((0.15 * (Rsas + (discount_per_cycle * bounce(values, i, j - 1, bounce_val))))
				+ (0.15 * (Rsas + (discount_per_cycle * bounce(values, i, j + 1, bounce_val))))
				+ (0.70 * (Rsas + (discount_per_cycle * bounce(values, i - 1, j, bounce_val)))))
	#return [south_off,north_off, east_off, west_off ]


	bd1 = -2 * battery_drop_cost
	reward1 = [bd1, bd1, win, death, 0]
	Rsas1 = reward1[bounce(map, i, j, 4)]
				

	east_on = ((0.10 * (Rsas1 + discount_per_cycle * bounce(values, i - 1,j, bounce_val))) 
			 + (0.10 * (Rsas1 + discount_per_cycle * bounce(values, i + 1, j, bounce_val)))
			 + (0.80 * (Rsas1 + discount_per_cycle * bounce(values, i, j + 1, bounce_val))))

	west_on = ((0.10 * (Rsas1 + discount_per_cycle * bounce(values, i - 1, j, bounce_val)))
			+  (0.10 * (Rsas1 + discount_per_cycle * bounce(values, i + 1, j, bounce_val)))
			+  (0.80 * (Rsas1 + discount_per_cycle * bounce(values, i, j - 1, bounce_val))))

	south_on = ((0.10 * (Rsas1 + discount_per_cycle * bounce(values, i, j - 1, bounce_val)))
			  + (0.10 * (Rsas1 + discount_per_cycle * bounce(values, i, j + 1, bounce_val)))
			  + (0.80 * (Rsas1 + discount_per_cycle * bounce(values, i + 1, j, bounce_val))))

	north_on  = ((0.10 * (Rsas1 + discount_per_cycle * bounce(values, i, j - 1, bounce_val))) 
			   + (0.10 * (Rsas1 + discount_per_cycle * bounce(values, i, j + 1, bounce_val)))
			   + (0.80 * (Rsas1 + discount_per_cycle * bounce(values, i - 1, j, bounce_val))))

	return [south_off, north_off, east_off, west_off, south_on, north_on, east_on, west_on]



def difference(values, copy_values):
	sum_values = 0
	sum_copy_values = 0
	for i in range(len (values)):
		for j in range(len (values[0])):
			sum_values += values[i][j]
			sum_copy_values += copy_values[i][j]
	diff = abs(sum_copy_values - sum_values)/len(values[0]) * len(values[0])
	return (diff > 0 and diff < 0.001)


def bounce(map, i, j, default):
	leny = len(map) - 1
	lenx = len(map[0]) - 1
	if (i < 0 or j < 0 or i > leny or j > lenx):
		return default
	return map[i][j]


def copy_list(my_list):
	new_list  = []
	for l in my_list:
		if (isinstance(l,list)):
			new_list.append(copy_list(l))			
		else:
			new_list.append(l)
	return new_list


mapx = [[0,0,0,2],
[0,0,0,3],
[0,0,0,0]]

valuesx = [[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]

policiesx = [['e','e','e','X'],
['n','X','n','X'],
['n','e','n','w']]

delivery_feex = 1
battery_drop_costx = 0
dronerepair_costx = 1
discount_per_cyclex = 0.1

v = drone_flight_planner(mapx,policiesx, valuesx, delivery_feex, battery_drop_costx, dronerepair_costx, discount_per_cyclex)
print(v)

print_values(valuesx)
print_values(policiesx)

delivery_feex = 1000
battery_drop_costx = 100
dronerepair_costx = 500
discount_per_cyclex = 0.1

data4 = [[0,0,0,0,0,0],
			[0,0,0,0,0,0],
			[0,0,0,0,0,0],
			[0,0,0,0,0,0],  
			[0,0,0,0,0,2],
			[0,0,0,0,0,0]]
			   
p_gold4 = [['e','e','e','e','s','S'],
			['e','e','e','e','s','S'],
			['e','e','E','e','s','S'],
			['s','S','X','E','E','S'],
			['E','E','E','E','E','X'],
			['n','N','X','e','e','N']]

valuesx = [[0,0,0,0,0,0],
			[0,0,0,0,0,0],
			[0,0,0,0,0,0],
			[0,0,3,0,0,0],  
			[0,0,0,0,0,2],
			[0,0,3,0,0,0]]


v = drone_flight_planner(data4,p_gold4, valuesx, delivery_feex, battery_drop_costx, dronerepair_costx, discount_per_cyclex)

print "the v, ", v

print_values(valuesx)
print_values(policiesx)			

