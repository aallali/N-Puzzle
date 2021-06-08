import sys
from tools.parser import get_input
from tools.is_solvable import is_solvable
from tools.Puzzle import Puzzle
from tools.colors import color
from tools.solved_state import KV as states
from tools.heuristics import KV

if __name__ == "__main__":

    g, u                = None, None
    goal_state          = []
    puzzle, size, args  = get_input()
    max_num             = size ** 2 - 1
    tmp                 = []
    remastered_puzzled  = []
    heuristic           = 'conflicts'
    allHeuristics       = list(KV.keys())
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
        heuristic = 'manhattan'

    elif args.f == 'conflicts':
        heuristic = 'conflicts'

    elif args.f == 'gaschnig':
        heuristic = 'gaschnig'

    elif args.f == 'hamming':
        heuristic = 'hamming'

    elif args.f == 'euclidean':
        heuristic = 'euclidean'

    if args.g == True:  # greedy Search
        g = 0

    if args.u == True:  # uniform Search
        u = 0

    # _is = [j for i in [[l for l in el] for el in init_state] for j in i]
    # print(_is)
    # _gs = [j for i in [[l for l in el] for el in goal_state] for j in i]

    print("- Puzzle given :")
    for i in range(size ** 2):
        t = " " + str(init_state[i]) if init_state[i] > 9 else ("  " + str(init_state[i]))
        print(color('yellow', t), end='')
        if (i + 1) % size == 0 or i == size ** 2:
            print()

    print("\n- Puzzle wanted :")
    for i in range(size ** 2):
        t = " " + str(goal_state[i]) if goal_state[i] > 9 else ("  " + str(goal_state[i]))
        print(color('yellow', t), end='')
        if (i + 1) % size == 0 or i == size ** 2:
            print()

    if init_state == goal_state:
        print(color('red', "- The puzzle is already solved !"))
        sys.exit(0)

    if not is_solvable(init_state, goal_state, size):
        print(color('red', "\n[ Unsolvable Puzzle ]\n"))
        sys.exit(0)

    puzzle = Puzzle(init_state, goal_state, size, g, u, heuristic)
    print(color('red', '<=========================================================>'))
    print("- Solving using :")
    print(f'     algorithm      : {color("blue2", "A*")}')
    print(f'     heuristic      : {color("blue2", args.f)}')
    print(f'     greedy  Search : {color("blue2", "Enabled" if args.g is True else "Disabled")}')
    print(f'     uniform Search : {color("blue2", "Enabled" if args.u is True else "Disabled")}')

    print("\n- Other Heuristics you can try :")
    print(f'                    - {color("blue2", str(", ".join(allHeuristics[0:2])))}')
    print(f'                    - {color("blue2", str(", ".join(allHeuristics[2:4])))}')
    print(f'                    - {color("blue2", str(", ".join(allHeuristics[4:6])))}')
    actions, states, count, cspace, maxopen, time = puzzle.solve_A_STAR()
    print(color('red', '<=========================================================>'))
    print(color('green2', "- Puzzle Solved :)"))
    # print(color('red', '<=========================================================>'))
    print(f"- Total Nodes Opened {color('yellow', '(Complexity in time)')}     : {color('blue2', str(count))}")
    print(f"- Max opened in RAM {color('yellow', '(Complexity in size)')}      : {color('blue2', str(maxopen))}")
    print(f"- Number of moves required                    : {color('blue2', str(len(states)))}")
    print(f"- Time needed to solve                        : {color('blue2', str(format(time, '.4f')))} s")
    print(color('red', '<=========================================================>'))

    open('moves.txt', 'w').close()
    open('states.txt', 'w').close()

    with open('moves.txt', 'a') as f:
        for answer in actions:
            f.write(answer + '\n')
    with open('states.txt', 'a') as f:
        for answer in states:
            f.write(str(answer) + '\n')
    """
        Visualtion if activated by flag -v
    """
    if args.v:
        from tools.visualization import visualize

        states = [[j for i in [[l for l in el] for el in tile] for j in i] for tile in states]
        states.insert(0, init_state)
        visualize(states, size)
