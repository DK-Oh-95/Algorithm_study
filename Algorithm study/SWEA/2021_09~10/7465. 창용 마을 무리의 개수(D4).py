def find_set(x):
    # 선택한 노드의 대표가 본인이면 그대로 반환
    if x == p[x]:
        return x
    # 대표가 다른 노드면 해당 노드 다시 탐색
    return find_set(p[x])


def union(x, y):
    # 두 노드의 대표가 같으면 반환
    if find_set(x) == find_set(y):
        return
    # 다르면 대표를 찾아서 수정
    p[find_set(y)] = find_set(x)


for tc in range(int(input())):
    N, M = map(int, input().split())  # N: 사람수, M: 관계수
    # p = [x for x in range(N+1)]
    p = list(range(N+1))
    # 대표자 설정
    for i in range(M):
        n1, n2 = map(int, input().split())
        union(n1, n2)

    # 그룹으로 묶어줌
    group = set()
    for i in range(1, N+1):
        group.add(find_set(p[i]))
    print('#{} {}'.format(tc+1, len(group)))

"""
2
6 5
1 2
2 5
5 1
3 4
4 6
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
"""