def b_tree(n):
    global cnt

    # 왼쪽 자식부터 탐색하여 값 넣고, 부모노드에 입력 후 오른쪽 자식에 값 입력
    if n <= N:
        # 왼쪽 자식 노드부터 값 넣기 위해 현재 노드의 2배
        b_tree(n * 2)
        # 범위를 넘지 않는 가장 왼쪽 노드에 값 입력 후 값 증가
        tree[n] = cnt
        cnt += 1
        # 오른쪽 자식 노드는 현재노드의 2배 + 1
        b_tree(n * 2 + 1)

    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)

    # 1부터 트리에 입력
    cnt = 1
    b_tree(1)

    print('#{} {} {}'.format(tc, tree[1], tree[N // 2]))
