def find_set(x):
    if x == p[x]:
        return x
    return find_set(p[x])


def union(x, y):
    px = find_set(x)
    py = find_set(y)
    if px == py:
        return
    else:
        p[py] = px


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    p = [x for x in range(N + 1)]

    # 그룹으로 묶어줌
    for i in range(M):
        union(nums[i*2], nums[i*2+1])

    # 그룹수 계산
    group = set()
    for i in range(1, N+1):
        if p[i] and p[i] not in group:
            group.add(find_set(p[i]))
    print('#{} {}'.format(tc, len(group)))

"""
3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4
"""