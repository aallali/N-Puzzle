import sys
from tools.parser import get_input
from tools.is_solvable import is_solvable
from tools.Puzzle import Puzzle
from tools.colors import color
from tools.solved_state import KV as states
from tools.heuristics import KV
import time
from reprint import output
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def print_hello():
	head = """
███╗   ██╗      ██████╗ ██╗   ██╗███████╗███████╗██╗     ███████╗
████╗  ██║      ██╔══██╗██║   ██║╚══███╔╝╚══███╔╝██║     ██╔════╝
██╔██╗ ██║█████╗██████╔╝██║   ██║  ███╔╝   ███╔╝ ██║     █████╗  
██║╚██╗██║╚════╝██╔═══╝ ██║   ██║ ███╔╝   ███╔╝  ██║     ██╔══╝  
██║ ╚████║      ██║     ╚██████╔╝███████╗███████╗███████╗███████╗
╚═╝  ╚═══╝      ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝
	"""
	msg = f"""{color('magenta2', head)}
by: {color('cyan2', 'Abdellah Allali')} && {color('cyan2', 'Hamza Elamri')}
	"""
	print(msg)
	return 
if __name__ == "__main__":
	clearConsole()
	print_hello()	
	g, u                = None, None
	goal_state          = []
	puzzle, size, args  = get_input()
	max_num             = size ** 2 - 1
	tmp                 = []
	remastered_puzzled  = []
	heuristic           = 'conflicts'
	allHeuristics       = list(KV.keys())
	init_state          = puzzle
	fast_search         = args.fast

	print(color('red', '<=========================================================>'))
	print(f"- Size of the puzzle : {color('blue2', str(size))} * {color('blue2', str(size))}\n")

	goal_state = states[args.s](size)
	heuristic = args.f

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

	puzzle = Puzzle(init_state, goal_state, size, g, u, heuristic, fast_search)

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

	actions, states, count, cspace, maxopen, timeTaken = puzzle.solve_A_STAR()
	actionsRemastered = "".join([(color('blue2', '↑') if l == 'UP'
	                               else ( color('red2', '↓') if l == 'DOWN'
	                                      else ( color('yellow', '→') if l == 'RIGHT' else color('green2', '←'))))
	                              for l in actions])
	print(color('red', '<=========================================================>'))

	print(color('green2', "- Puzzle Solved :)"))
	print(f"- Total Nodes Opened {color('yellow', '(Complexity in time)')}     : {color('blue2', str(count))}")
	print(f"- Max opened in RAM {color('yellow', '(Complexity in size)')}      : {color('blue2', str(maxopen))}")
	print(f"- Number of moves required                    : {color('blue2', str(len(actions)))}")
	print(f"- Time needed to solve                        : {color('blue2', str(format(timeTaken, '.4f')))} s")
	print(f"- Moves taken to solve                        : {actionsRemastered}")
	print(color('red', '<=========================================================>'))

	open('moves.txt', 'w').close()
	open('states.txt', 'w').close()

	with open('moves.txt', 'a') as f:
		for answer in actions:
			f.write(answer + '\n')
	with open('states.txt', 'a') as f:
		for answer in states:
			f.write(str(answer) + '\n')

	states = [[j for i in [[l for l in el] for el in tile] for j in i] for tile in states]

	if args.v is False and args.t != '0':
		alphabetic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
		print('- Moves replay :\n')
		with output(output_type='dict', sort_key=lambda x: 1) as output_lines:
			for i in range(len(states)):
				move =  ''
				if actions[i] == 'UP':
					move = color('blue2', '↑ ' + actions[i])
				if actions[i] == 'DOWN':
					move = color('red2', '↓ ' + actions[i])
				if actions[i] == 'RIGHT':
					move = color('yellow', '→ '+ actions[i])
				if actions[i] == 'LEFT':
					move = color('green2', '← ' + actions[i])

				output_lines['Move   '] = '       ' + move + ' '
				output_lines['Move N°'] = '       ' + f"{i + 1}/{len(actions)}\n"
				tmp = []
				row = []
				for j in range(len(states[i])):
					t = states[i][j]
					t = '_' if t == 0 else t
					if t == '_':
						n = '  █'
					else:
						n = (' ' + str(t)) if t > 9 else ('  '+ str(t))
						n = color('yellow', n)
					tmp.append(n)
					if (j + 1) % size == 0:
						row.append("".join(tmp))
						tmp = []
				for x in range(len(row)):
					output_lines[alphabetic[x]] = '         ' + str(row[x])

				time.sleep(float(args.t))
	
			# print(states[i])
	"""
		Visualtion if activated by flag -v
	"""
	if args.v:
		from tools.visualization import visualize
		states.insert(0, init_state)
		visualize(states, size)
