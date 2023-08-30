def print_maze(maze, player_pos):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if (row, col) == player_pos:
                print('P', end=' ')
            else:
                print(maze[row][col], end=' ')
        print()

def move_player(player_pos, direction):
    row, col = player_pos
    if direction == 'w':
        row -= 1
    elif direction == 's':
        row += 1
    elif direction == 'a':
        col -= 1
    elif direction == 'd':
        col += 1
    return row, col

maze = [
    ['#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#']
]

player_pos = (1, 1)

print("Welcome to the Maze Game!")
print_maze(maze, player_pos)

while True:
    move = input("Enter a direction (w/a/s/d): ")
    
    new_player_pos = move_player(player_pos, move)
    
    if maze[new_player_pos[0]][new_player_pos[1]] == ' ':
        player_pos = new_player_pos
    else:
        print("You can't move there!")

    print_maze(maze, player_pos)

