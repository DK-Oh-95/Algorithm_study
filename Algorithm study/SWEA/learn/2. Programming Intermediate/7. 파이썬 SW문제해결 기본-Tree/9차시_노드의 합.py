T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    leaf = [list(map(int, input().split())) for _ in range(M)]

    # leaf의 값들 입력
    nodes = [0] * (N+1)
    for i in range(len(leaf)):
        nodes[leaf[i][0]] = leaf[i][1]

    # 부모노드에 자식노드들의 합 입력
    for j in reversed(range(N+1)):
        nodes[j//2] += nodes[j]

    print('#{} {}'.format(tc, nodes[L]))