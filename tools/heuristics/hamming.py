
from .heuristics import *

class Node(object):
    def __init__(self, curr_state, parent, action, pos, solved, g, u):
        self.state = curr_state
        self.parent = parent
        self.action = action
        self.pos = pos
        self.path_cost = g if g is not None else ((parent.path_cost + 1 if parent != None else 0))
        self.candidate = [j for i in [[l for l in el] for el in curr_state] for j in i]
        self.solved = [j for i in [[l for l in el] for el in solved] for j in i]

        if u is not None:
            self.heuristic = u
        else:
            self.heuristic = hamming(self.candidate, self.solved, len(curr_state[0])) * 2


    def __lt__(self, other):
        return self.path_cost + self.heuristic < other.path_cost + other.heuristic

