# n-puzzle 1337 @ aallali

```
███╗   ██╗      ██████╗ ██╗   ██╗███████╗███████╗██╗     ███████╗
████╗  ██║      ██╔══██╗██║   ██║╚══███╔╝╚══███╔╝██║     ██╔════╝
██╔██╗ ██║█████╗██████╔╝██║   ██║  ███╔╝   ███╔╝ ██║     █████╗  
██║╚██╗██║╚════╝██╔═══╝ ██║   ██║ ███╔╝   ███╔╝  ██║     ██╔══╝  
██║ ╚████║      ██║     ╚██████╔╝███████╗███████╗███████╗███████╗
╚═╝  ╚═══╝      ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝
by : 
┌─┐┌┐ ┌┬┐┌─┐┬  ┬  ┌─┐┬ ┬  ┌─┐┬  ┬  ┌─┐┬  ┬
├─┤├┴┐ ││├┤ │  │  ├─┤├─┤  ├─┤│  │  ├─┤│  │
┴ ┴└─┘─┴┘└─┘┴─┘┴─┘┴ ┴┴ ┴  ┴ ┴┴─┘┴─┘┴ ┴┴─┘┴
```
```
usage: npuzzle.py [-h] 
                  [-g] [-u] 
                  [-f {hamming,gaschnig,manhattan,conflicts,euclidean,diagonal}]
                  [-s {zero_first,zero_last,snail}] 
                  [-v] 
                  [-t T] 
                  [--fast]
                  file

n-puzzle @ 42 aallali

positional arguments:
  file                  input file

optional arguments:
  -h, --help            show this help message and exit
  -g                    greedy search
  -u                    uniform-cost search
  -f {hamming,gaschnig,manhattan,conflicts,euclidean,diagonal}
                        heuristic function
  -s {zero_first,zero_last,snail}
                        snail
  -v                    gui visualizer
  -t T                  Solution replay on terminal, animation speed time value required
                        (Disabled default)
  --fast                fast search
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

`-f euclidean` euclidean distance heuristic (not good as manhattan)

`-f diagonal` euclidean distance heuristic (not good as manhattan)


#### miscellaneous:

`-g` greedy search: ignores the `g(n)` in **A*** formula `f(n) = g(n) + h(n)`, quickly finds a **suboptimal** solution

`-u` uniform cost search: discards the `h(n)` in **A*** formula (turns off heuristics and becomes dijkstra's, slow)

`-v` replay solution steps in graphical visualizer

`-t` replay solution steps in terminal with colorized outprint

`--fast` use a faster search alogrithm but add more moves to goal

#### Ready command for terminal (windows):
`py -2 .\generator.py -s -i 1000 3  > test && cls && py -3 .\npuzzle.py .\test -f conflicts -v `

#### View from GUI Visualation :
![gui](https://raw.githubusercontent.com/aallali/42-N-Puzzle/main/docs/gui.PNG?token=AKWFYDYMTX62IUOQIZBRXW3AZDN5O)

#### GIF from GUI Visualation :
![gui](https://raw.githubusercontent.com/aallali/42-N-Puzzle/main/docs/gui-gif.gif?token=AKWFYDYMDK73KJWOB625PYTAZDPCY)

#### View from Terminal :
![terminal](https://raw.githubusercontent.com/aallali/42-N-Puzzle/main/docs/terminal-replay.gif?token=AKWFYD4V6W6PYAYS3UOTKD3AZ4PH2)
