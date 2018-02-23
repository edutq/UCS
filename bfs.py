import heapq
import itertools

class Node:
	def __init__ (self, cost, parent, path, state) :
		self.cost = cost
		self.parent = parent
		self.path = path

def move(maxheight, current, goal) :
	foundGoal = False
	current_matrix = toMatrix(current)
	goal_matrix = toMatrix(goal)


def toMatrix(string) :
	matrix = []
	for var in string.split(';'):
		var = var.replace(' ', '')
		var = var.replace(')', '')
		var = var.replace('(', '')
		list = []
		for var2 in var.split(','):

			list.append(var2)

		matrix.append(list)
	return matrix

def cleanmovements(possible_movements, current_matrix) : 
	print(possible_movements)
	newlist = []
	for i in range(len(current_matrix)):
		if current_matrix[i][0] == '':
			newlist.append(i)
	print(newlist)
	for t, i in zip(possible_movements, range(0,len(possible_movements))):
		for item in newlist:
			if t[0] == item:
				del(possible_movements[i:i+len(current_matrix)-1])
	print(possible_movements)
	return possible_movements

def ucs (maxheight, current, goal) :
	#initialize the goal found in false
	foundGoal = False
	#parse the string of the current state to a matrix
	current_matrix = toMatrix(current)
	#parse the string of the goal state to a matrix
	goal_matrix = toMatrix(goal)
	#find all posible movements in the current state
	possible_movements = list(itertools.permutations(range(0, len(current_matrix)), 2))
	#remove the movements from the empty stack
	possible_movements = cleanmovements(possible_movements, current_matrix)
	#list of seen items
	seen = {}
	#priority queue
	q = [Node(0, [], [], current_matrix)]


ucs(3, "(A); (B); (C); ()", "(); (A); (B); (C)")