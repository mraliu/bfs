maze = [
    ['#', 'E', '#', '#', '#', '#', '#', '#', '#', '#'], #0
    ['#', ' ', ' ', '#', '#', '#', '#', ' ', '#', '#'], #1
    ['#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#'], #2
    ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'], #3
    ['#', '#', ' ', '#', '#', ' ', '#', '#', '#', '#'], #4
    ['#', '#', ' ', '#', '#', ' ', '#', '#', '#', '#'], #5
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'], #6
    ['#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#'], #7
    ['#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#'], #8
    ['#', '#', '#', '#', '#', '#', '#', '#', 'S', '#']  #9
    # 0,   1,   2,   3,   4,   5,   6,   7,   8,   9   ###
]

def printmaze():
    for row in maze:
        print(row)
    print("\n\n")

def searchnode(key)
    for row in maze:
        for col in row.split(","):
            if maze[row][col] == key:
                return (row, col)
queue = [] 
visited = []
currentnode = [9, 8] # y, x
completed = False


i = 0
while completed == False and maze[currentnode[1]][currentnode[0]] != "E":
    visited.append(currentnode)
    y, x = currentnode
    if y > 0: #  North (UP)
        if maze[y-1][x] == " " and [y-1, x] not in visited:
            queue.append([y-1, x])
            maze[y-1][x] = "o"
        elif maze[y-1][x] == "E":
            print("Exit found at: ", y-1,x)
            break
    if y < len(maze) -1: # South (DOWN)
        if maze[y+1][x] == " " and [y+1, x] not in visited: 
            queue.append([y+1, x])
            maze[y+1][x] = "o"
        elif maze[y+1][x] == "E":
            print("Exit found at: ", y+1,x)
            break
    if x > 0: # West (RIGHT)
        if maze[y][x-1] == " " and [y, x-1] not in visited:
            queue.append([y, x-1])
            maze[y][x-1] = "o"
        elif maze[y][x-1] == "E":
            print("Exit found at: ", y,x-1)
            break
    if x < len(maze[0]) -1: # East (LEFT)
        if maze[y][x+1] == " " and [y, x+1] not in visited:
            queue.append([y, x+1])
            maze[y][x+1] = "o"
        elif maze[y][x+1] == "E":
            print("Exit found at: ", y, x+1)
            break
    # print("S:", i, "Currentnode: ", currentnode, "Queue: ", queue, "Visited: ", visited)
    if len(queue) != 0:
        currentnode = queue.pop(0)
    else:
        print("Cannot find exit")
        completed = True
    i+=1
    printmaze()