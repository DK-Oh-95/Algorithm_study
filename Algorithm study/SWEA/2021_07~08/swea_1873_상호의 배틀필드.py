T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    # .: 평지, *: 벽돌벽, #: 강철벽, -: 물
    # ^, v, <, >
    field = ['!'.join(input()).split('!') for _ in range(H)]
    N = int(input())
    # U, D, L, R, S
    behavior = input()

    # 현재 전차 위치 파악
    cr = 0
    cc = 0
    for i in range(H):
        for j in range(W):
            if field[i][j] == '^' or field[i][j] == 'v' or field[i][j] == '<' or field[i][j] == '>':
                cr, cc = i, j

    for k in range(N):
        if behavior[k] == 'U':
            if cr == 0:
                field[cr][cc] = '^'
            elif 0 <= cr - 1 and field[cr - 1][cc] == '.':
                field[cr][cc] = '.'
                cr -= 1
                field[cr][cc] = '^'
            else:
                field[cr][cc] = '^'
        elif behavior[k] == 'D':
            if cr == H - 1:
                field[cr][cc] = 'v'
            elif cr + 1 < H and field[cr + 1][cc] == '.':
                field[cr][cc] = '.'
                cr += 1
                field[cr][cc] = 'v'
            else:
                field[cr][cc] = 'v'
        elif behavior[k] == 'L':
            if cc == 0:
                field[cr][cc] = '<'
            elif 0 <= cc - 1 and field[cr][cc - 1] == '.':
                field[cr][cc] = '.'
                cc -= 1
                field[cr][cc] = '<'
            else:
                field[cr][cc] = '<'
        elif behavior[k] == 'R':
            if cc == W - 1:
                field[cr][cc] = '>'
            elif cc + 1 < W and field[cr][cc + 1] == '.':
                field[cr][cc] = '.'
                cc += 1
                field[cr][cc] = '>'
            else:
                field[cr][cc] = '>'
        else:  # S일 경우
            nr = 0
            nc = 0
            # 바라보는 방향으로 참조하여 * 있으면 .으로 변경
            if field[cr][cc] == '^':
                nr = cr - 1
                while nr != -1:
                    if field[nr][cc] == '#':
                        break
                    elif field[nr][cc] == '*':
                        field[nr][cc] = '.'
                        break
                    nr = nr - 1
            elif field[cr][cc] == 'v':
                nr = cr + 1
                while nr != H:
                    if field[nr][cc] == '#':
                        break
                    elif field[nr][cc] == '*':
                        field[nr][cc] = '.'
                        break
                    nr = nr + 1
            elif field[cr][cc] == '<':
                nc = cc - 1
                while nc != -1:
                    if field[cr][nc] == '#':
                        break
                    elif field[cr][nc] == '*':
                        field[cr][nc] = '.'
                        break
                    nc = nc - 1
            elif field[cr][cc] == '>':
                nc = cc + 1
                while nc != W:
                    if field[cr][nc] == '#':
                        break
                    elif field[cr][nc] == '*':
                        field[cr][nc] = '.'
                        break
                    nc = nc + 1

    print('#{}'.format(tc), end=' ')
    for d in range(H):
        for m in range(W):
            print(field[d][m], end='')
        print()
