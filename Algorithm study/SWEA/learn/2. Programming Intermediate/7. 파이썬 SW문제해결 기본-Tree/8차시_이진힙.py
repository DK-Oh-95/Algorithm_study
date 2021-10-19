T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    tree = [0] * (N+1)

    sum_p = 0
    for i in range(1, N+1):
        # 트리에 입력값을 하나씩 넣고
        # 부모노드보다 값이 작으면 위치 변경
        tree[i] = numbers[i-1]
        num = i
        while num // 2:
            if tree[num] < tree[num//2]:
                tree[num], tree[num//2] = tree[num//2], tree[num]
            num //= 2

        if i == N:
            num = i
            while num//2:
                num //= 2
                sum_p += tree[num]

    print('#{} {}'.format(tc, sum_p))
