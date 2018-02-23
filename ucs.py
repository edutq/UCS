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

def children(node, cost, current_state, possible_movements, path) :
	arrayofchildren = []
	for action in possible_movements:
		#print(action)

		auxpath = copy.deepcopy(path)
		nextstate = copy.deepcopy(current_state)
		auxcost = cost + 1 + abs(action[0] - action[1])
		if not nextstate[action[0]]:
			continue
		value = (nextstate[action[0]]).pop()
		
		nextstate[action[1]].append(value)
		auxpath.append(action)
		child = Node(nextstate)
	
		arrayofchildren.append((auxcost, auxpath, child))
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

	q = [(cost, path, Node(current_matrix))]
	#validate that the input is not messed up
	if all(len(var) <= maxheight for var in goal_matrix) and len(current_matrix) == len(goal_matrix):
		
		while q:

			cost, path, state= heapq.heappop(q)
			
			if areequal(state.getState(), goal_matrix):
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
				possible_movements = list(itertools.permutations(range(0, len(state.getState())), 2))
				#remove the movements from the empty stack
				
				#possible_movements = cleanmovements(possible_movements, state.getState())

				if state not in seen:
					child = children(state, cost, state.getState(), possible_movements, path)
					for var in child:
						heapq.heappush(q, var)

					seen.append(state)
	else:
		print("No solution found")

if __name__ == "__main__":

	lines = []
	for line in fileinput.input():
    	lines.append(line)
	h = lines[0]
	current = lines[1]
	goal = lines[2]

	ucs(h, current, goal)