import numpy as np


def heuristic_aux(x, y, x_g, y_g, name):
    """Admissible heuristics
    Parameters
    ----------
    x, y: int
      state coordinate
    x_g, y_g: int
      goal coordinate
    name: str
      heuristic function name
    Return
    ------
    Float:
      Corresponding heuristic value for a single coordinate
    """
    if name == 'hamming':
        return x != x_g or y != y_g
    elif name == 'manhattan':
        return abs(x - x_g) + abs(y - y_g)
    elif name == 'euclidean':
        return np.sqrt((x - x_g) ** 2 + (y - y_g) ** 2)
    elif name == 'diagonal':
        return max(abs(x - x_g) , abs(y - y_g))
    elif name == 'uniform_cost':
        return 0


def heuristic(goal, state, name='euclidean'):
    """Heuristic function
    Parameters
    ----------
    goal: list
      Puzzle state we want to achieve
    state: list
      Current Puzzle state
    name: str (Default: 'euclidean')
      Name of heuristic function to use ∈ [ 'euclidean', 'manhattan',
                                            'gaschnig','hamming',
                                            'uniform-cost',]
    Returns
    -------
    One of
      'hamming': float
        Number of tiles in the wrong position
      'Manhattan': float
        Sum of the horizontal and vertical distances between,
        current position and desired position, i.e. ∑ |state - goal|
      'Gaschnig': Int
        total of white tile moves to put the puzzle in goal state, but without respecting order of tiles(check algo below)
      'Euclidean': float
        Sum of the distance between tiles
        ∑ √(x - x_g)² + (y - y_g)²
    """
    size = int(np.sqrt(len(goal)))

    if name == 'gaschnig':
        return gaschnig(goal, state, size)

    if name == 'uniform_cost':
        return 0

    coord_goal = np.zeros((size ** 2, 2))  # in index i coordinates of tile i in goal
    coord_state = np.zeros((size ** 2, 2))  # in index i coordinates of tile i in state
    for x in range(size):
        for y in range(size):
            coord_goal[goal[x * size + y]] = [x, y]
            coord_state[state[x * size + y]] = [x, y]
    h = 0
    if name == 'conflicts':
        h = np.sum([heuristic_aux(*coord_state[i], *coord_goal[i], 'manhattan') for i in range(size ** 2)])
        return 2 * linear_conflicts(goal, state, size) + h

    h = np.sum([heuristic_aux(*coord_state[i], *coord_goal[i], name) for i in range(size ** 2)])
    return h


def gaschnig(candidate, solved, size):
    """
    moves = 0
    while not in goal state:
        if blank in goal position:
            swap blank with any mismatch
        else
            swap blank with matched tile
        moves++
    return moves
    """
    res = 0
    candidate = list(candidate)
    solved = list(solved)
    while candidate != solved:
        zi = candidate.index(0)
        if solved[zi] != 0:
            sv = solved[zi]
            ci = candidate.index(sv)
            candidate[ci], candidate[zi] = candidate[zi], candidate[ci]
        else:
            for i in range(size * size):
                if solved[i] != candidate[i]:
                    candidate[i], candidate[zi] = candidate[zi], candidate[i]
                    break
        res += 1
    return res


def linear_conflicts(candidate, solved, size):
    def count_conflicts(candidate_row, solved_row, size, ans=0):
        counts = [0 for x in range(size)]
        for i, tile_1 in enumerate(candidate_row):
            if tile_1 in solved_row and tile_1 != 0:
                for j, tile_2 in enumerate(candidate_row):
                    if tile_2 in solved_row and tile_2 != 0:
                        if tile_1 != tile_2:
                            if (solved_row.index(tile_1) > solved_row.index(tile_2)) and i < j:
                                counts[i] += 1
                            if (solved_row.index(tile_1) < solved_row.index(tile_2)) and i > j:
                                counts[i] += 1
        if max(counts) == 0:
            return ans * 2
        else:
            i = counts.index(max(counts))
            candidate_row[i] = -1
            ans += 1
            return count_conflicts(candidate_row, solved_row, size, ans)

    res = 0
    candidate_rows = [[] for y in range(size)]
    candidate_columns = [[] for x in range(size)]
    solved_rows = [[] for y in range(size)]
    solved_columns = [[] for x in range(size)]
    for y in range(size):
        for x in range(size):
            idx = (y * size) + x
            candidate_rows[y].append(candidate[idx])
            candidate_columns[x].append(candidate[idx])
            solved_rows[y].append(solved[idx])
            solved_columns[x].append(solved[idx])

    for i in range(size):
        res += count_conflicts(candidate_rows[i], solved_rows[i], size)
    for i in range(size):
        res += count_conflicts(candidate_columns[i], solved_columns[i], size)
    return res


KV = {
    'hamming': True,
    'gaschnig': True,
    'manhattan': True,
    'conflicts': True,
    'euclidean': True,
    'diagonal': True
}
