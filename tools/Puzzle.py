from collections import deque
import copy
import heapq
import time
from .Node import Node


class Puzzle(object):

	def __init__(self, init_state, goal_state, size, g, u, heuristic, fast_search=False):

		self.init_state = []
		self.goal_state = []
		self.actions = deque()
		self.states = deque()
		self.heuristic = heuristic
		self.g = g # greedy search : f = 0 + h(n)
		self.u = u # uniform search : f = g + 0
		self.augment_heuristic = 1 if fast_search is False else 4
		tmp = []
		for i in range(len(init_state)):
			tmp.append(init_state[i])
			if (i + 1) % size == 0:
				self.init_state.append(tmp)
				tmp = []

		tmp = []
		for i in range(len(goal_state)):
			tmp.append(goal_state[i])
			if (i + 1) % size == 0:
				self.goal_state.append(tmp)
				tmp = []

		for i, v in enumerate(self.init_state):
			for j, k in enumerate(v):
				if k == 0:
					self.start_pos = (i, j)
					break

		self.start_node = Node(self.init_state, None, None, self.start_pos, self.goal_state, self.g, self.u, heuristic, self.augment_heuristic)

	def swap(self, curr_state, pos, direction):
		temp = curr_state[pos[0]][pos[1]]
		curr_state[pos[0]][pos[1]] = curr_state[pos[0] + direction[0]][pos[1] + direction[1]]
		curr_state[pos[0] + direction[0]][pos[1] + direction[1]] = temp
		return curr_state

	def move(self, curr_state, pos, visited, direction):
		if pos[0] + direction[0] >= len(curr_state) or pos[0] + direction[0] < 0 or pos[1] + direction[1] >= len(
				curr_state[0]) or pos[1] + direction[1] < 0:
			return None, pos
		if str(self.swap(curr_state, pos, direction)) in visited:
			curr_state = self.swap(curr_state, pos, direction)
			return None, pos

		next_state = copy.deepcopy(curr_state)
		curr_state = self.swap(curr_state, pos, direction)
		return next_state, (pos[0] + direction[0], pos[1] + direction[1])

	def solve_A_STAR(self):
		move_directions = {
			(0, 1): 'RIGHT',
			(1, 0): 'DOWN',
			(-1, 0): 'UP',
			(0, -1): 'LEFT'
		}
		visited = set()
		pq = []
		heapq.heappush(pq, self.start_node)
		count = 0
		timestamp1 = time.time()
		maxOpenSet = 0
		while pq:
			maxOpenSet = max(maxOpenSet, len(pq))
			curr_node = heapq.heappop(pq)
			if curr_node.state == self.goal_state:
				break
			if str(curr_node.state) in visited or str(curr_node.state) in pq:
				continue

			"""
			visited == closed set == to register all visited states to avoid infinity loop
			"""
			visited.add(str(curr_node.state))

			for direction in move_directions.keys():
				next_state, next_pos = self.move(curr_node.state,
				                                 curr_node.pos,
				                                 visited,
				                                 direction)
				if next_state:
					node = Node(next_state,
					            curr_node,
					            move_directions[direction],
					            next_pos,
					            self.goal_state,
					            self.g,
					            self.u,
					            self.heuristic,
					            self.augment_heuristic)
					"""
					push to Queue
					"""
					heapq.heappush(pq, node)
					count += 1

		timestamp2 = time.time() # get the time diff from the start till we foud the solution

		"""
		loop through the last solution node parent tree to retreive states, and actions (moves)
		"""
		while curr_node:
			if curr_node.action:
				self.actions.appendleft(curr_node.action)
				self.states.appendleft(curr_node.state)
			curr_node = curr_node.parent

		"""
		return @params
		actions 				= 'all moves taken to find the solution path'
		states  				= 'all the puzzle states in the solution path'
		maxOpenSet 				= 'or Complexity in size : the number of nodes that was opened in same time in RAM'
		timestamp2 - timestamp1 = 'time diff from the start till we foud the solution'
		"""
		return self.actions, self.states, count, len(self.actions), maxOpenSet, timestamp2 - timestamp1
