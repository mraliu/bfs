file = open("maze.csv", "r")
maze = []
[maze.append(row.split(",")) for row in file.read().splitlines()]
    

# print(maze)