def queen(cr, cc):
    global cnt

    # 8방향 탐색하여 1이 없으면 해당 자리 1로 바꾸고 다음 행 이동
    tmp = 0
    for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, 1),
                   (1, 1), (1, 0), (1, -1), (0, -1)]:
        nr, nc = cr, cc
        while 0 <= nr < N and 0 <= nc < N:
            nr, nc = nr + dr, nc + dc
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc]:
                tmp += 1
                break
        if not tmp:
            # for x in range(N):
            #     print(board[x])
            # print('tmp:', tmp)
            # print('cnt:', cnt)
            # 마지막 행까지 채우면 가능한 경우 추가
            if cr == N-1:
                cnt += 1
                return

            board[cr][cc] = 1
            for ne in range(N):
                queen(cr+1, ne)
            board[cr][cc] = 0


for tc in range(int(input())):
    N = int(input())
    board = list([0] * N for _ in range(N))

    cnt = 0
    for e in range(N):
        queen(0, e)

    print('#{} {}'.format(tc+1, cnt))