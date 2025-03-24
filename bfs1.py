maze = [
    ['#', 'E', '#', '#', '#', '#', '#', '#', '#', '#'], #0
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], #1
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], #2
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], #3
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], #4
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], #5
    ['#', ' ', ' ', ' ', 'E', '#', '#', '#', '#', '#'], #6
    ['#', '#', ' ', '#', '#', '#', '#', '#', '#', '#'], #7
    ['#', '#', ' ', '#', '#', '#', '#', '#', '#', ' '], #8
    ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S']  #9
    # 0,   1,   2,   3,   4,   5,   6,   7,   8,   9   ###
]

queue = [] 
visited = []
currentnode = [9, 9] # y, x
completed = False

i = 0

while completed == False and maze[currentnode[1]][currentnode[0]] != "E":

    visited.append(currentnode)

    y, x = currentnode

    # North (UP)
    if y > 0 and maze[y-1][x] == " " and [y-1, x] not in visited:
        queue.append([y-1, x])

    # South (DOWN)
    if y < len(maze) -1 and maze[y+1][x] == " " and [y+1, x] not in visited: 
        queue.append([y+1, x])  

    # West (RIGHT)
    if x > 0 and maze[y][x-1] == " " and [y, x-1] not in visited:
        queue.append([y, x-1])

    # East (LEFT)
    if x < len(maze[0]) -1 and maze[y][x+1] == " " and [y, x+1] not in visited:
        queue.append([y, x+1])

    print("S:", i, "Currentnode: ", currentnode, "Queue: ", queue, "Visited: ", visited)

    if len(queue) != 0:
        currentnode = queue.pop(0)
    elif maze[currentnode[1]][currentnode[0]] == "E":
        print("Found path")
    else:
        print("Cannot find exit")
        completed = True
    i+=1