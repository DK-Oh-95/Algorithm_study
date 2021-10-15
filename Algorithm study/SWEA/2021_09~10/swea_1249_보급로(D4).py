from collections import deque


def bfs(r, c):
    q = deque()
    q.append((r, c))  # 출발지 입력
    dist[0][0] = 0
    while q:  # q 다 쓸때까지(모든지점 확인)
        cr, cc = q.popleft()
        for dr, dc in [[-1,0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = cr + dr, cc + dc
            # 이동할 수 있는 노드의 값이 현재 지점에 도달할 수 있는 최소시간과
            # 다음 지역에서 써야할 소비시간의 합보다 크면 더 작은 값으로 갱신
            if 0 <= nr < N and 0 <= nc < N:
                if dist[nr][nc] > dist[cr][cc] + arr[nr][nc]:
                    q.append((nr, nc))
                    dist[nr][nc] = dist[cr][cc] + arr[nr][nc]


for tc in range(int(input())):
    N = int(input())  # 지도크기
    arr = [list(input()) for _ in range(N)]  # 지도 정보
    # 정수로 변환
    for i in range(N):
        for j in range(N):
            arr[i][j] = int(arr[i][j])
    INF = 0xffffff
    dist = [[INF] * N for _ in range(N)]  # 출발지로부터 각 노드로 가는 최소시간을 저장할 리스트
    bfs(0, 0)

    print('#{} {}'.format(tc+1, dist[N - 1][N - 1]))
