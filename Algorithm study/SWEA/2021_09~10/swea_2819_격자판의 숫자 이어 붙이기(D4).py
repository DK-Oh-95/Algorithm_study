def make_number(r, c, number):
    if len(number) == 7:
        num_list.add(number)
        return

    # 현재 지점 기준 네 방향 이동
    for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            make_number(nr, nc, number + grid[nr][nc])


T = int(input())
for tc in range(1, T + 1):
    grid = [list(input().split()) for _ in range(4)]

    num_list = set()
    for i in range(4):
        for j in range(4):
            make_number(i, j, grid[i][j])

    print('#{} {}'.format(tc, len(num_list)))
