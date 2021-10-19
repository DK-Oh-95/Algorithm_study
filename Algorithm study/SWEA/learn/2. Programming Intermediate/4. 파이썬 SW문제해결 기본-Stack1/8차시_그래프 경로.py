# 인접배열을 탐색하면서 S로 시작해 E에 도달하면 1 반환
def dfs(graph, start, goal):
    N = len(graph)
    stack = []
    stack.append(start)
    # 탐색한 경로 순서
    path = []
    path.append(start)
    # 왔던 길 표시
    visited = [0] * N
    visited[start] = 1

    while stack:
        # top : 현재 노드 번호
        top = stack[-1]
        for i in range(1, N):
            # top에서 갈 수 있는 길 확인
            if graph[top][i] and not visited[i]:
                # i를 경로에 추가
                stack.append(i)
                visited[i] = 1
                path.append(i)
                break
        # 갈 수 있는 길이 없으면 경로에서 pop
        else:
            stack.pop()
    if goal in path:
        return 1
    else:
        return 0

# 테스트케이스
T = int(input())

for tc in range(1, T+1):
    # 노드 개수 V, 간선 개수 E
    V, E = map(int, input().split())
    # 간선 정보(연결된 노드 정보)
    nodes = [list(map(int, input().split())) for _ in range(E)]
    # 출발, 도착 노드
    S, G = map(int, input().split())

    # 노드 개수만큼 크기를 가지는 인접행렬 생성
    adj = [[0] * (V+1) for _ in range(V+1)]
    # 생성한 인접행렬의 연결된 노드 정보 입력
    for i in range(E):
        adj[nodes[i][0]][nodes[i][1]] = 1

    print('#{} {}'.format(tc, dfs(adj, S, G)))