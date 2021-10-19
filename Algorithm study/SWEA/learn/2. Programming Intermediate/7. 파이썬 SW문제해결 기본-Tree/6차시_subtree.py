def pre_order(v):
    global cnt
    # v : 현재 정점의 번호
    if v == 0:
        return
    # 자식이 있는 노드이므로
    cnt += 1
    pre_order(left_child[v])
    pre_order(right_child[v])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    V = E + 1  # 노드 개수는 간선 + 1
    edges = list(map(int, input().split()))

    # 이진트리 생성하고 순회하여 자식 노드 수 게산하면 됨
    left_child = [0] * (V + 1)
    right_child = [0] * (V + 1)

    for i in range(0, E * 2, 2):
        # edges[i] : 부모노드
        # edges[i+1] : 자식노드
        if not left_child[edges[i]]:  # 왼쪽 자식이 없으면 왼쪽에 넣음
            left_child[edges[i]] = edges[i + 1]
        else:
            right_child[edges[i]] = edges[i + 1]
    cnt = 0
    pre_order(N)

    print('#{} {}'.format(tc, cnt))
