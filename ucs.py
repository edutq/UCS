import heapq
import itertools
import copy
import fileinput

class Node:
	def __init__ (self, state) :
		self.state = state

	def getState(self):
		return self.state


def toMatrix(string) :
	matrix = []
	for var in string.split(';'):
		var = var.replace(' ', '')
		var = var.replace(')', '')
		var = var.replace('(', '')
		list = []
		for var2 in var.split(','):
			if var2 == '':
				continue
			else:
				list.append(var2)

		matrix.append(list)
	#print(matrix)
	return matrix



def areequal(current, goal):
	count = 0
	for index, item in enumerate(goal):
		if item != ['X']:
			if current[index] == goal[index]:
				count += 1
	if count == len(goal) - goal.count(['X']):
		return True
	return False

def children(cost, current_state, possible_movements, path, maxheight) :
	arrayofchildren = []
	for action in possible_movements:
		#print(action)

		auxpath = copy.deepcopy(path)
		nextstate = copy.deepcopy(current_state)
		auxcost = cost + 1 + abs(action[0] - action[1])
		if not nextstate[action[0]]:
			continue
		if len(nextstate[action[1]]) >= maxheight:
			continue

		value = (nextstate[action[0]]).pop()
		
		nextstate[action[1]].append(value)
		auxpath.append(action)
		
	
		arrayofchildren.append((auxcost, auxpath, nextstate))
	return arrayofchildren

def ucs (maxheight, current, goal) :
	#initialize the goal found in false
	foundGoal = False
	#parse the string of the current state to a matrix
	current_matrix = toMatrix(current)
	#parse the string of the goal state to a matrix
	goal_matrix = toMatrix(goal)

	#list of seen items
	seen = []
	#priority queue
	cost = 0
	path = []

	q = [(cost, path, current_matrix)]
	#validate that the input is not messed up
		
	while q:

		cost, path, state= heapq.heappop(q)
		
		if areequal(state, goal_matrix):
			print(cost)
			for action in path:
				if action != path[-1]:
					print(action, end="")
					print("; ", end="")
				else:
					print(action)
			return path
		else:
			#find all posible movements in the current state
			possible_movements = list(itertools.permutations(range(0, len(state)), 2))
			#remove the movements from the empty stack
			
			#possible_movements = cleanmovements(possible_movements, state.getState())

			if state not in seen:
				child = children(cost, state, possible_movements, path, maxheight)
				for var in child:
					heapq.heappush(q, var)

				seen.append(state)
	print("No solution found")

if __name__ == "__main__":

	h = int(input())
	current = input()
	goal = input()

	ucs(h, current, goal)