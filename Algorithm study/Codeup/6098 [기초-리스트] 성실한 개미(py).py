def find_feed(r, c):
    global maze

    if maze[r][c] == '2':
        maze[r][c] = '9'
        return

    maze[r][c] = '9'

    if c+1 < 10 and maze[r][c+1] == '0' or maze[r][c+1] == '2':
        c += 1
    elif not maze[r+1][c] == '1' or maze[r+1][c] == '2':
        r += 1
    else:
        return
    find_feed(r, c)


maze = [list(input().split()) for _ in range(10)]
find_feed(1, 1)

for i in range(10):
    for j in range(10):
        print(int(maze[i][j]), end=' ')
    print()