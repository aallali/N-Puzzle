# n-puzzle @ 42 aallali

```
usage: solver.py [-h] [-g] [-u]
                 [-f {hamming,gaschnig,manhattan,conflicts}]
                 [-s {zero_first,zero_last,snail}] [-v]
                 file

n-puzzle @ 42 aallali

positional arguments:
  file                  input file

optional arguments:
  -h, --help            show this help message and exit
  -g                    greedy search
  -u                    uniform-cost search
  -f {hamming,gaschnig,manhattan,conflicts}
                        heuristic function
  -s {zero_first,zero_last,snail}
                        solved state
  -v                    gui visualizer
```

#### search:

default search is **A***
- fast and efficient
- memory heavy


#### input puzzle configurations:
`-s zero_first` (blank tile first)

```
3
0  1  2
3  4  5
6  7  8
```


`-s zero_last` (blank tile last)
```
3
1  2  3
4  5  6
7  8  0
```

`-s snail` (default, spiral pattern)
```
3
1  2  3
8  0  4
7  6  5
```

#### heuristics:
`-f hamming` hamming distance aka "tiles out of place"

`-f gaschnig` performs better than hamming distance

`-f manhattan` manhattan distance heuristic (default)

`-f conflicts` linear conflicts usually more informed than manhattan distance


#### miscellaneous:
`-g` greedy search: ignores the `g(n)` in **A*** formula `f(n) = g(n) + h(n)`, quickly finds a **suboptimal** solution

`-u` uniform cost search: discards the `h(n)` in **A*** formula (turns off heuristics and becomes dijkstra's, slow)

`-v` replay solution steps in graphical visualizer

#### Ready command for terminal :
`py -2 .\generator.py -s -i 1000 3  > test && cls && py -3 npuzzle.py .\test -f conflicts -v `

#### View from GUI Visualation :

![gui](https://github.com/aallali/42-N-Puzzle/blob/main/docs/gui.PNG)
#### View from Terminal :
![terminal](https://raw.githubusercontent.com/aallali/42-N-Puzzle/main/docs/terminal.PNG?token=AKWFYD6GOMASIDHHVVW5ZCLAY52ZC)
