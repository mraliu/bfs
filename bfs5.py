# Create your maze
# text box to create size of grid
# LMB to make gap
# RMB to make wall
# Button to start BFS

import pygame, sys

file = open("maze.csv", "r")
maze = []
[maze.append(row.split(",")) for row in file.read().splitlines()]

MAP_SIZE = len(maze)
TILE_SIZE = 50
HEIGHT = MAP_SIZE * TILE_SIZE
WIDTH = HEIGHT * 2

def draw_map():
    #iterate over map
    for r in range(MAP_SIZE):
        for c in range(MAP_SIZE):
            
            square = maze[r][c]
            if square == "S":
                pygame.draw.rect(screen, (0, 255, 0), (c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1))
            elif square == "E":
                pygame.draw.rect(screen, (255, 0, 0), (c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1))
            elif square == "#":
                pygame.draw.rect(screen, (0, 0, 0), (c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1))
            else:   
                pygame.draw.rect(screen, (211, 211, 211), (c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1))
            
def printmaze():
    for row in maze:
        print(row)
    print("\n\n")

def searchnode(key): # Returns coords of key
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == key:
                return (row, col)
            
def save():
    with open("maze.csv", "w") as file:
        for row in maze:
            file.write(",".join(row) + "\n")






def bfs():
    queue = [] 
    currentnode = searchnode("S") # y, x
    visited = []
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
                # break
        if y < len(maze) -1: # South (DOWN)
            if maze[y+1][x] == " " and [y+1, x] not in visited: 
                queue.append([y+1, x])
                maze[y+1][x] = "o"
            elif maze[y+1][x] == "E":
                print("Exit found at: ", y+1,x)
                # break
        if x > 0: # West (RIGHT)
            if maze[y][x-1] == " " and [y, x-1] not in visited:
                queue.append([y, x-1])
                maze[y][x-1] = "o"
            elif maze[y][x-1] == "E":
                print("Exit found at: ", y,x-1)
                # break
        if x < len(maze[0]) -1: # East (LEFT)
            if maze[y][x+1] == " " and [y, x+1] not in visited:
                queue.append([y, x+1])
                maze[y][x+1] = "o"
            elif maze[y][x+1] == "E":
                print("Exit found at: ", y, x+1)
                # break
        # print("S:", i, "Currentnode: ", currentnode, "Queue: ", queue, "Visited: ", visited)
        if len(queue) != 0:
            currentnode = queue.pop(0)
        else:
            print("Cannot find exit")
            completed = True
        i+=1
    printmaze()
   

# bfs()


######################################################################

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        
        if x>=0 and x <= MAP_SIZE * TILE_SIZE and y>=0 and y <= MAP_SIZE * TILE_SIZE:
            print(int(x/TILE_SIZE % 10), int(y/TILE_SIZE % 10))
            if event.button == 1:
                maze[int(y/TILE_SIZE % 10)][int(x/TILE_SIZE % 10)] = "#"
            elif event.button == 3:
                maze[int(y/TILE_SIZE % 10)][int(x/TILE_SIZE % 10)] = " "

    screen.fill((255, 255, 255))

    draw_map()

    butt_bfs = pygame.draw.rect(screen, (189, 195, 199), (WIDTH - 400, 50, 100, 50))
    butt_save = pygame.draw.rect(screen, (95, 106, 106), (WIDTH - 400, 125, 100, 50))

    if butt_bfs.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            bfs()

    if butt_save.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            save()

        

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit(0)