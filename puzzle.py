
#input InitalState SearchMethod
import sys
from Queue import Queue, LifoQueue, PriorityQueue
from sets import Set
depth = 0
numCreated = 0
numExpanded = 0
maxFringe = 0
validPuzzle = Set(list('123456789ABCDEF '))
searches = ['BFS', 'DFS', 'GBFS', 'AStar','DLS']
option = ['h1', 'h2']

#prints the puzzle in a nice format
def printPuzzle(puzzle):
    print puzzle[0], puzzle[1], puzzle[2], puzzle[3]
    print puzzle[4], puzzle[5], puzzle[6], puzzle[7]
    print puzzle[8], puzzle[9], puzzle[10], puzzle[11]
    print puzzle[12], puzzle[13], puzzle[14], puzzle[15]

#does the space move right
def moveRight(puzzle):
    space = puzzle.index(' ')
    puzzleCopy = list(puzzle)
    if space % 4 != 3:
        puzzleCopy[space], puzzleCopy[space+1] = puzzleCopy[space+1], puzzleCopy[space]
        return puzzleCopy
    #print "cant move"
    return None
#does the space move left
def moveLeft(puzzle):
    space = puzzle.index(' ')
    puzzleCopy = list(puzzle)
    if space % 4 != 0:
        puzzleCopy[space], puzzleCopy[space-1] = puzzleCopy[space-1], puzzleCopy[space]
        return puzzleCopy
    #print "cant move"
    return None

#does the space move up
def moveUp(puzzle):
    space = puzzle.index(' ')
    puzzleCopy = list(puzzle)
    if space > 3:
        puzzleCopy[space], puzzleCopy[space-4] = puzzleCopy[space-4], puzzleCopy[space]
        return puzzleCopy
    #print "cant move"
    return None

#does the space move down
def moveDown(puzzle):
    space = puzzle.index(' ')
    puzzleCopy = list(puzzle)
    if space < 12:
        puzzleCopy[space], puzzleCopy[space+4] = puzzleCopy[space+4], puzzleCopy[space]
        return puzzleCopy
    #print "cant move"
    return None

#BFS search algorithm
def BFS(puzzle, solPuzzle, puzSol2):
    global depth
    global numCreated
    global numExpanded
    global maxFringe
    q = Queue()
    q.put((0, puzzle))
    visited = list(puzzle)
    while True:
        cp = q.get()
        current = cp[1]
        depth = cp[0]
        if current == solPuzzle or current == puzSol2:
            return current
        numExpanded += 1
        right = moveRight(current)
        down = moveDown(current)
        left = moveLeft(current)
        up = moveUp(current)
        if right != None and right not in visited:
            q.put((depth+1, right))
            visited.append(right)
            numCreated += 1
        if down != None and down not in visited:
            q.put((depth+1, down))
            visited.append(down)
            numCreated += 1
        if left != None and left not in visited:
            q.put((depth+1,left))
            visited.append(left)
            numCreated += 1
        if up != None and up not in visited:
            q.put((depth+1,up))
            visited.append(up)
            numCreated += 1
        if q.qsize() > maxFringe:
            maxFringe = q.qsize()
        
#DFS search algorithm
def DFS(puzzle, solPuzzle, puzSol2):
    global depth
    global numCreated
    global numExpanded
    global maxFringe
    q = LifoQueue()
    q.put((0, puzzle))
    visited = list(puzzle)
    while True:
        cp = q.get()
        current = cp[1]
        depth = cp[0]
        if current == solPuzzle or current == puzSol2:
            return current
        numExpanded += 1
        right = moveRight(current)
        down = moveDown(current)
        left = moveLeft(current)
        up = moveUp(current)
        if up != None and up not in visited:
            q.put((depth+1,up))
            visited.append(up)
            numCreated += 1
        if left != None and left not in visited:
            q.put((depth+1,left))
            visited.append(left)
            numCreated += 1
        if down != None and down not in visited:
            q.put((depth+1, down))
            visited.append(down)
            numCreated += 1
        if right != None and right not in visited:
            q.put((depth+1, right))
            visited.append(right)
            numCreated += 1
        if q.qsize() > maxFringe:
            maxFringe = q.qsize()

#heuristic for incorrect tiles
def h1(puzzle, solPuzzle):
    h1 = 0
    for i in range(16):
        if puzzle[i] != solPuzzle[i] and puzzle[i] != ' ':
            h1 += 1
    return h1

#heuristic for sum of Manhattan distance to solution
def h2(puzzle, solPuzzle):
    h2 = 0
    for i in range(16):
        if puzzle[i] != solPuzzle[i] and puzzle[i] != ' ':
            horizontal = abs(i%4 - solPuzzle.index(puzzle[i])%4)
            vertial = abs(i/4 - solPuzzle.index(puzzle[i])/4)
            h2 += horizontal + vertial
    return h2

# Greedy Best First Search Algorithm for heuristic 1
def GBFS_h1(puzzle, solPuzzle, puzSol2):
    global depth
    global numCreated
    global numExpanded
    global maxFringe
    q = PriorityQueue()
    q.put((h1(puzzle, solPuzzle),(0, puzzle)))
    visited = list(puzzle)
    while True:
        cp = q.get()
        current = cp[1][1]
        depth = cp[1][0]
        if current == solPuzzle or current == puzSol2:
            return current
        numExpanded += 1
        right = moveRight(current)
        down = moveDown(current)
        left = moveLeft(current)
        up = moveUp(current)
        if right != None and right not in visited:
            q.put((h1(right, solPuzzle), (depth+1, right)))
            visited.append(right)
            numCreated += 1
        if down != None and down not in visited:
            q.put((h1(down, solPuzzle), (depth+1, down)))
            visited.append(down)
            numCreated += 1
        if left != None and left not in visited:
            q.put((h1(left, solPuzzle), (depth+1, left)))
            visited.append(left)
            numCreated += 1
        if up != None and up not in visited:
            q.put((h1(up, solPuzzle), (depth+1, up)))
            visited.append(up)
            numCreated += 1
        if q.qsize() > maxFringe:
            maxFringe = q.qsize()
            
# Greedy Best First Search Algorithm for heuristic 2
def GBFS_h2(puzzle, solPuzzle, puzSol2):
    global depth
    global numCreated
    global numExpanded
    global maxFringe
    q = PriorityQueue()
    q.put((h2(puzzle, solPuzzle),(0, puzzle)))
    visited = list(puzzle)
    while True:
        cp = q.get()
        current = cp[1][1]
        depth = cp[1][0]
        if current == solPuzzle or current == puzSol2:
            return current
        numExpanded += 1
        right = moveRight(current)
        down = moveDown(current)
        left = moveLeft(current)
        up = moveUp(current)
        if right != None and right not in visited:
            q.put((h2(right, solPuzzle), (depth+1, right)))
            visited.append(right)
            numCreated += 1
        if down != None and down not in visited:
            q.put((h2(down, solPuzzle), (depth+1, down)))
            visited.append(down)
            numCreated += 1
        if left != None and left not in visited:
            q.put((h2(left, solPuzzle), (depth+1, left)))
            visited.append(left)
            numCreated += 1
        if up != None and up not in visited:
            q.put((h2(up, solPuzzle), (depth+1, up)))
            visited.append(up)
            numCreated += 1
        if q.qsize() > maxFringe:
            maxFringe = q.qsize()
            
# A Search Algorithm for heuristic 1
def AStar_h1(puzzle, solPuzzle, puzSol2):
    global depth
    global numCreated
    global numExpanded
    global maxFringe
    q = PriorityQueue()
    q.put((h1(puzzle, solPuzzle),(0, puzzle)))
    visited = list(puzzle)
    while True:
        cp = q.get()
        current = cp[1][1]
        depth = cp[1][0]
        if current == solPuzzle or current == puzSol2:
            return current
        numExpanded += 1
        right = moveRight(current)
        down = moveDown(current)
        left = moveLeft(current)
        up = moveUp(current)
        if right != None and right not in visited:
            q.put((h1(right, solPuzzle) + depth + 1, (depth+1, right)))
            visited.append(right)
            numCreated += 1
        if down != None and down not in visited:
            q.put((h1(down, solPuzzle) + depth + 1, (depth+1, down)))
            visited.append(down)
            numCreated += 1
        if left != None and left not in visited:
            q.put((h1(left, solPuzzle) + depth + 1, (depth+1, left)))
            visited.append(left)
            numCreated += 1
        if up != None and up not in visited:
            q.put((h1(up, solPuzzle) + depth + 1, (depth+1, up)))
            visited.append(up)
            numCreated += 1
        if q.qsize() > maxFringe:
            maxFringe = q.qsize()

# AStar Search Algorithm for heuristic 2
def AStar_h2(puzzle, solPuzzle, puzSol2):
    global depth
    global numCreated
    global numExpanded
    global maxFringe
    q = PriorityQueue()
    q.put((h2(puzzle, solPuzzle),(0, puzzle)))
    visited = list(puzzle)
    while True:
        cp = q.get()
        current = cp[1][1]
        depth = cp[1][0]
        if current == solPuzzle or current == puzSol2:
            return current
        numExpanded += 1
        right = moveRight(current)
        down = moveDown(current)
        left = moveLeft(current)
        up = moveUp(current)
        if right != None and right not in visited:
            q.put((h2(right, solPuzzle) + depth + 1, (depth+1, right)))
            visited.append(right)
            numCreated += 1
        if down != None and down not in visited:
            q.put((h2(down, solPuzzle) + depth + 1, (depth+1, down)))
            visited.append(down)
            numCreated += 1
        if left != None and left not in visited:
            q.put((h2(left, solPuzzle) + depth + 1, (depth+1, left)))
            visited.append(left)
            numCreated += 1
        if up != None and up not in visited:
            q.put((h2(up, solPuzzle) + depth + 1, (depth+1, up)))
            visited.append(up)
            numCreated += 1
        if q.qsize() > maxFringe:
            maxFringe = q.qsize()

#Depth limited search algorithm
def DLS(puzzle, solPuzzle, puzSol2, limit):
    global depth
    global numCreated
    global numExpanded
    global maxFringe
    q = LifoQueue()
    q.put((0, puzzle))
    visited = list(puzzle)
    while True:
        if q.empty():
            print "Could not find the solution in the limited search."
            sys.exit()
        cp = q.get()
        current = cp[1]
        depth = cp[0]
        if current == solPuzzle or current == puzSol2:
            return current
        if depth == limit:
            continue
        numExpanded += 1
        right = moveRight(current)
        down = moveDown(current)
        left = moveLeft(current)
        up = moveUp(current)
        if up != None and up not in visited:
            q.put((depth+1,up))
#            visited.append(up)
            numCreated += 1
        if left != None and left not in visited:
            q.put((depth+1,left))
#            visited.append(left)
            numCreated += 1
        if down != None and down not in visited:
            q.put((depth+1, down))
#            visited.append(down)
            numCreated += 1
        if right != None and right not in visited:
            q.put((depth+1, right))
#            visited.append(right)
            numCreated += 1
        if q.qsize() > maxFringe:
            maxFringe = q.qsize()
            
            
solution1 = "123456789ABCDEF "
solution2 = "123456789ABCDFE "


def main(argv):

    options = None
    if len(sys.argv) > 2:
        if Set(sys.argv[1]) != validPuzzle or len(list(sys.argv[1])) > 16:
            print "Invalid puzzle please input the correct format."
            sys.exit()
        else: initialstate = list(sys.argv[1])
        
        if sys.argv[2] not in searches:
            print "Please enter a valid search method and options if necessary."
            sys.exit()
        else: searchmethod = sys.argv[2]
        
        if len(sys.argv) > 3:
            if sys.argv[3] not in option and not sys.argv[3].isdigit():
                    print 'Please enter a correct option or limit.'
                    sys.exit()
            else: options = sys.argv[3]
            
    else:
        print 'Please enter at least an initial state and a search method.'
        
    puzzle = list(initialstate)
    puzSol = list(solution1)
    puzSol2 = list(solution2)
    
    if searchmethod == "BFS":
        searchAns = BFS(puzzle, puzSol, puzSol2)
    elif searchmethod == "DFS":
        searchAns = DFS(puzzle, puzSol, puzSol2)
    elif searchmethod == "GBFS" and options == "h1":
        searchAns = GBFS_h1(puzzle, puzSol, puzSol2)
    elif searchmethod == "GBFS" and options == "h2":
        searchAns = GBFS_h2(puzzle, puzSol, puzSol2)
    elif searchmethod == "AStar" and options == "h1":
        searchAns = AStar_h1(puzzle, puzSol, puzSol2)
    elif searchmethod == "AStar" and options == "h2":
        searchAns = AStar_h1(puzzle, puzSol, puzSol2)
    elif searchmethod == "DLS":
        searchAns = DLS(puzzle, puzSol, puzSol2, int(options))
    else:
        print """
Please follow this format for entering a puzzle, a search method,
and options for the search method if there are any: 

python puzzle.py "initialState" searchmethod options

GBFS and AStar options are h1 or h2

DLS option is any number for the depth limit."""
        sys.exit()
    '''
    print 'Initialstate is:'
    printPuzzle(puzzle)
    print 'Searchmethod is', searchmethod
    if options != None:
        print 'Options are ', options
        
    print "Puzzle Soultion is:"
    printPuzzle(searchAns)
    '''
    print str(depth) +  ', ' + str(numCreated) + ', ' + str(numExpanded) + ', ' + str(maxFringe)    
    #printPuzzle(puzSol)
if __name__ == "__main__":
    main(sys.argv[1:])

