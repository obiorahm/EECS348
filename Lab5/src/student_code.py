import common

def drone_flight_planner (map,policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle):
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# access the policies using "policies[y][x]"
	# access the values using "values[y][x]"
	# y between 0 and 5
	# x between 0 and 5
	# function must return the value of the cell corresponding to the starting position of the drone
	# 
	return planner (map,policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, 1 - discount_per_cycle)
	

def planner (map,policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle):
	copy_values = copy_list(values)
	for i in range (len (map)):
		for j in range (len (map[0])):
			if map[i][j] == 2:
				values[i][j] = delivery_fee
				policies[i][j] =common.constants.EXIT
			elif map[i][j] == 3:
				values[i][j] = -1 * dronerepair_cost
				policies[i][j] =common.constants.EXIT
			else:
				sum_rewards = sum_of_rewards(map, copy_values, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle, i, j)
				maximum = max(sum_rewards)
				values[i][j] = maximum
				policy = [common.constants.SOFF, common.constants.NOFF, common.constants.EOFF, common.constants.WOFF,
							common.constants.SON, common.constants.NON, common.constants.EON, common.constants.WON]
				index = sum_rewards.index(maximum)
				policies[i][j] = policy[index]
	if difference(values, copy_values):
		return get_start_value(map,values)
	else:
		return planner (map, policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle)

def get_start_value(map,values):
	for i in range(len(map)):
		for j in range(len(map)):
			if map[i][j] == 1:
				return values[i][j]





def print_values (values):
	for i in range(len(values)):
		for j in range(len(values[0])):
			print values[i][j], 
        print '\n'


def sum_of_rewards (map, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle, i, j):
	bd = -1 * battery_drop_cost
	death = -1 * (dronerepair_cost + battery_drop_cost)
	win = delivery_fee - battery_drop_cost
	reward = [ bd, bd, win, death, 0]


	east_off = ((0.15 * (reward[bounce(map, i - 1, j, 4)] + (discount_per_cycle * bounce(values, i - 1,j,0))))
				+ (0.15 * (reward[bounce(map, i + 1, j,4)] + discount_per_cycle * bounce(values, i + 1, j,0)))
				+ (0.70 * (reward[bounce(map, i, j + 1, 4)] + discount_per_cycle * bounce(values, i, j + 1, 0))))


	west_off = ((0.15 * (reward[bounce(map, i - 1, j, 4)] + discount_per_cycle * bounce(values, i - 1, j, 0)))
				+ (0.15 * (reward[bounce(map, i + 1, j, 4)] + discount_per_cycle * bounce(values, i + 1, j, 0)))
				+ (0.70 * (reward[bounce(map, i, j - 1, 4)] + discount_per_cycle * bounce(values, i, j - 1, 0))))

	south_off 	= ((0.15 * (reward[bounce(map, i, j - 1, 4)] + discount_per_cycle * bounce(values, i, j - 1, 0)))
				+ (0.15 * (reward[bounce(map, i, j + 1, 4)] + discount_per_cycle * bounce(values, i, j + 1, 0)))
				+ (0.70 * (reward[bounce(map, i + 1, j, 4)] + discount_per_cycle * bounce(values, i + 1, j, 0))))

	north_off  = ((0.15 * (reward[bounce(map, i, j - 1, 4)] + discount_per_cycle * bounce(values, i, j - 1, 0))) 
				+ (0.15 * (reward[bounce(map, i, j + 1, 4)] + discount_per_cycle * bounce(values, i, j + 1, 0)))
				+ (0.70 * (reward[bounce(map, i - 1, j, 4)] + discount_per_cycle * bounce(values, i - 1, j, 0))))

	bd1 = -2 * battery_drop_cost
	death1 = -dronerepair_cost + (-2 * battery_drop_cost)
	win1 = delivery_fee + (-2 * battery_drop_cost)
	reward1 = [bd1, bd1, win1, death1, 0]
				

	east_on = ((0.10 * (reward1[bounce(map, i - 1, j, 4)] + discount_per_cycle * bounce(values, i - 1,j, 0))) 
			 + (0.10 * (reward1[bounce(map, i + 1, j, 4)] + discount_per_cycle * bounce(values, i + 1, j, 0)))
			 + (0.80 * (reward1[bounce(map, i, j + 1, 4)] + discount_per_cycle * bounce(values, i, j + 1, 0))))

	west_on = ((0.10 * (reward1[bounce(map, i - 1, j, 4)] + discount_per_cycle * bounce(values, i - 1, j, 0)))
			+  (0.10 * (reward1[bounce(map, i + 1, j, 4)] + discount_per_cycle * bounce(values, i + 1, j, 0)))
			+  (0.80 * (reward1[bounce(map, i, j - 1, 4)] + discount_per_cycle * bounce(values, i, j - 1, 0))))

	south_on = ((0.10 * (reward1[bounce(map, i, j - 1, 4)] + discount_per_cycle * bounce(values, i, j - 1, 0)))
			  + (0.10 * (reward1[bounce(map, i, j + 1, 4)] + discount_per_cycle * bounce(values, i, j + 1, 0)))
			  + (0.80 * (reward1[bounce(map, i + 1, j, 4)] + discount_per_cycle * bounce(values, i + 1, j, 0))))

	north_on  = ((0.10 * (reward1[bounce(map, i, j - 1, 4)] + discount_per_cycle * bounce(values, i, j - 1, 0))) 
			   + (0.10 * (reward1[bounce(map, i, j + 1, 4)] + discount_per_cycle * bounce(values, i, j + 1, 0)))
			   + (0.80 * (reward1[bounce(map, i - 1, j, 4)] + discount_per_cycle * bounce(values, i - 1, j, 0))))

	return [south_off, north_off, east_off, west_off, south_on, north_on, east_on, west_on]


def difference(values, copy_values):
	sum_values = 0
	sum_copy_values = 0
	for i in range(len (values)):
		for j in range(len (values[0])):
			sum_values += values[i][j]
			sum_copy_values += copy_values[i][j]
	diff = abs(sum_copy_values - sum_values)/36.0
	#print diff
	return (diff > 0 and diff < 0.001)


def bounce(map, i, j, default):
	if (i < 0 or j < 0 or i > 5 or j > 5):
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

mapx = [[0002]
[0]]
drone_flight_planner(mapx,policiesx, valuesx, delivery_feex, battery_drop_costx, dronerepair_costx, discount_per_cyclex)



