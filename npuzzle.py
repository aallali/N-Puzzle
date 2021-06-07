# CS3243 Introduction to Artificial Intelligence
# Project 1: k-Puzzle

import sys
from tools.parser import get_input
from tools.is_solvable import is_solvable
from tools.Puzzle import Puzzle
from tools.colors import color
from tools.heuristics.manhattanDistance import Node as Node_manhatten
from tools.heuristics.linearConflict import Node as Node_linearConflict
from tools.heuristics.gaschnig import Node as Node_Gasching
from tools.heuristics.hamming import Node as Node_Hamming

from tools.solved_state import KV as states

if __name__ == "__main__":

    Node                = None
    g, u                = None, None
    goal_state          = []
    init_state          = []
    puzzle, size, args  = get_input()
    max_num             = size ** 2 - 1
    tmp                 = []
    remastered_puzzled  = []
    allHeuristics       = ", ".join(['hamming', 'gaschnig', 'manhattan', 'conflicts'])
    init_state          = puzzle
   
    print(color('red', '<=========================================================>'))
    print(f"- Size of the puzzle : {color('blue2', str(size))} * {color('blue2', str(size))}\n")



    if args.s == 'snail':
        goal_state = states['snail'](size)

    elif args.s == 'zero_first':
        goal_state = states['zero_first'](size)

    elif args.s == 'zero_last':
        goal_state = states['zero_last'](size)


    if args.f == 'manhattan':
        Node = Node_manhatten

    elif args.f == 'conflicts':
        Node = Node_linearConflict

    elif args.f == 'gaschnig':
        Node = Node_Gasching

    elif args.f == 'hamming':
        Node = Node_Hamming

    
    if args.g == True: # greedy Search
        g = 0

    if args.u == True: # uniform Search
        u = 0


    """
        Serialize  puzzle from [[t,t,t],[t,t,t],[t,t,t]] => [t,t,t,t,t,t,t,t,t]
    """
    # print(puzzle)
    # for i in range(len(puzzle)):
    #     tmp.append(int(puzzle[i]))
    #     if len(tmp) == size:
    #         init_state.append(tmp)
    #         tmp = []
    # print(init_state)
    # print(goal_state)
    """
        Serialize  puzzle from [[t,t,t],[t,t,t],[t,t,t]] => [t,t,t,t,t,t,t,t,t]
    """

    # for i in range(len(goal_state)):
    #     tmp.append(int(goal_state[i]))
    #     if len(tmp) == size:
    #         remastered_puzzled.append(tmp)
    #         tmp = []
    # goal_state = remastered_puzzled
    # remastered_puzzled = []

    # _is = [j for i in [[l for l in el] for el in init_state] for j in i]
    # print(_is)
    # _gs = [j for i in [[l for l in el] for el in goal_state] for j in i]


    print("- Puzzle given :")
    for i in range(size ** 2):
        t = " "+ str(init_state[i]) if init_state[i] > 9 else ("  " + str(init_state[i]))
        print(color('yellow', t), end='')
        if (i + 1) % size == 0 or i == size ** 2:
            print()

    print("- Puzzle wanted :")
    for i in range(size ** 2):
        t = " "+ str(goal_state[i]) if goal_state[i] > 9 else ("  " + str(goal_state[i]))
        print(color('yellow', t), end='')
        if (i + 1) % size == 0 or i == size ** 2:
            print()

    if init_state == goal_state:
        print("- The puzzle is already solved !")
        sys.exit(0)

    if not is_solvable(init_state, goal_state, size):
        print('Unsolvable Puzzle')
        sys.exit(0)


    puzzle            = Puzzle(Node, init_state, goal_state, size, g, u)
    print(color('red', '<=========================================================>'))
    print("- Solving using :")
    print(f'     algorithm      : {color("blue2", "A*")}')
    print(f'     heuristic      : {color("blue2", args.f)}')
    print(f'     greedy  Search : {color("blue2", "Enabled" if args.g is True else "Disabled")}')
    print(f'     uniform Search : {color("blue2", "Enabled" if args.u is True else "Disabled")}')

    print("\n- Other ways you can try :")
    print(f'     heuristics : {color("blue2", str(allHeuristics))}')

    actions, states, count, cspace, maxopen, time = puzzle.solve_A_STAR()
    print(color('red', '<=========================================================>'))
    print("- Puzzle Solved :")
    for i in range(size):
        print(color('green2', "  " + " ".join([str(j) if j > 9 else (" " + str(j)) for j in states[-1][i]])))
        if (i + 1) % size == 0 and i + 1 != size:
            print()
    print(color('red', '<=========================================================>'))
    print(f"- Total Nodes Opened {color('yellow', '(Complexity in time)')}     : {color('blue2', str(count))}")
    print(f"- Max opened at same time {color('yellow', '(Complexity in size)')}: {color('blue2', str(maxopen))}")
    print(f"- Number of moves required                    : {color('blue2', str(len(states)))}")
    print(f"- Time needed to solve                        : {color('blue2', str(format(time, '.4f')))} s")
    print(color('red', '<=========================================================>'))

    with open('moves.txt', 'a') as f:
        for answer in actions:
            f.write(answer + '\n')

    if args.v:
        from tools.visualization import visualize
      
        states =   [[j for i in [[l for l in el] for el in tile] for j in i] for tile in states]
        states.insert (0, init_state) 
          
        visualize(states, size)
