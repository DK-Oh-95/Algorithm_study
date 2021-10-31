from collections import deque


def bfs():
    Q = [0] * 100000
    front = rear = -1

    rear += 1
    Q[rear] = (0, 0)  # 행과 열의 좌표를 넣는다
    dist[0][0] = 0

    while front != rear:
        front += 1
        r, c = Q[front]

        # 4방향 탐색
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                power = heights[nr][nc] - heights[r][c] if heights[nr][nc] > heights[r][c] else 0

                if dist[nr][nc] > dist[r][c] + power + 1:
                    rear += 1
                    Q[rear] = (nr, nc)
                    dist[nr][nc] = dist[r][c] + power + 1


def bfs2():
    q = deque()
    q.append((0, 0))
    dist[0][0] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                power = heights[nr][nc] - heights[r][c] if heights[nr][nc] > heights[r][c] else 0
                if dist[nr][nc] > dist[r][c] + power + 1:
                    q.append((nr, nc))
                    dist[nr][nc] = dist[r][c] + power + 1


for tc in range(1, int(input())+1):
    N = int(input())
    heights = [list(map(int, input().split())) for _ in range(N)]

    INF = 0xffffff
    dist = [[INF] * N for _ in range(N)]
    # bfs()
    bfs2()

    print('#{} {}'.format(tc, dist[N-1][N-1]))

"""
3
3
0 2 1
0 1 1
1 1 1
5
0 0 0 0 0
0 1 2 3 0
0 2 3 4 0
0 3 4 5 0
0 0 0 0 0
5
0 1 1 1 0
1 1 0 1 0
0 1 0 1 0
1 0 0 1 1
1 1 1 1 1
"""