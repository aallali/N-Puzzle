from .heuristics import heuristic


class Node(object):
	def __init__(self, curr_state, parent, action, pos, solved, g, u, h, ah):
		self.state = curr_state
		self.parent = parent
		self.action = action
		self.pos = pos
		self.path_cost = g if g is not None else ((parent.path_cost + 1 if parent != None else 0))

		self.candidate = [j for i in [[l for l in el] for el in curr_state] for j in i]
		self.solved = [j for i in [[l for l in el] for el in solved] for j in i]
		if u is not None:
			self.heuristic = 0
		else:
			self.heuristic = heuristic(self.candidate, self.solved, h) * ah

	# compare function <
	def __lt__(self, other):
		# it's straightforward to see why this heuristic dominates manhattan distance, because for all n where n represents a state,
		# manhattanDistance(n) <= manhattanDistance(n) + linearConflict(n), where linearConflict(n) is an integer >= 0.
		return self.path_cost + self.heuristic < other.path_cost + other.heuristic
	#
	# # compare function <=
	# def __le__(self, other):
	# 	return self.path_cost + self.heuristic <= other.path_cost + other.heuristic
	#
	# # compare function >=
	# def __ge__(self, other):
	# 	return self.path_cost + self.heuristic >= other.path_cost + other.heuristic
	#
	# # compare function >
	# def __gt__(self, other):
	# 	return self.path_cost + self.heuristic > other.path_cost + other.heuristic
	#
