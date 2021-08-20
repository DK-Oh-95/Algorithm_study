def dfs(graph):
    N = len(graph)
    # 스택의 줄발지점은 0
    stack = []
    stack.append(0)
    # 방문 기록
    visited = [0] * N
    visited[0] = 1
    # 지나간 경로
    path = []
    path.append(0)

    # 스택이 비어 있는 상태까지 반복 >> 더이상 참조할 곳이 없다
    while stack:
        # 현재 노드 위치
        top = stack[-1]
        for i in range(N):
            # 갈 곳이 있고 방문하지 않았을 때
            if graph[top][i] and not visited[i]:
                # i를 경로에 추가
                stack.append(i)
                visited[i] = 1
                path.append(i)
                break   # 먼저 찾았으면 더이상 찾을 필요 없이 다음 노드로 이동
        # 갈 수 있는 곳 없으면 stack에서 뺀다
        else:
            stack.pop()
    # 최종 목적지 노드는 99
    if 99 in path:
        return 1
    else:
        return 0

# 테스트케이스는 10개
T = 10

for _ in range(T):
    # 테스트케이스. 길의 총 개수
    tc, N = map(int, input().split())

    # 노드 연결 정보 입력
    nodes = list(map(int, input().split()))
    # 출발점과 도착점 따로 구분
    nodes_s = []
    nodes_e = []
    for i in range(len(nodes)):
        if not i % 2:   # 인덱스가 짝수(출발점)
            nodes_s.append(nodes[i])
        else:   # 인덱스가 홀수(도착점)
            nodes_e.append(nodes[i])

    # 100 * 100 인접행렬 생성
    adj = [[0] * 100 for _ in range(100)]
    # 노드 간 출발, 도착 정보 입력
    for i in range(N):
        adj[nodes_s[i]][nodes_e[i]] = 1

    print('#{} {}'.format(tc, dfs(adj)))