def in_order(num):
    # num : 참조 시작하려는 현재 노드의 번호
    # 정상 노드인지 확인
    if num == 0:
        return

    # 왼쪽 가장 깊은 번호까지 가서 출력한 뒤
    # 돌아오면서 가운데 출력, 오른쪽  자식 출력
    in_order(left_child[num])
    print(word[num], end='')
    in_order(right_child[num])


T = 10
for tc in range(1, T+1):
    # 정점의 수 N
    N = int(input())
    # 간선 개수
    E = N - 1
    # 정점정보(번호, 알파벳, 왼쪽자식, 오른쪽자식)
    node = [list(input().split()) for _ in range(N)]
    # 간선 정보 리스트 생성
    edge = []
    # 글자정보 리스트 생성
    word = [0] * (N + 1)

    for i in range(N):
        if len(node[i]) == 2:  # 길이가 2면 자식노드 없다는 뜻
            word[i + 1] = node[i][1]
        elif len(node[i]) == 3:  # 자식 노드 1개
            edge.append(int(node[i][0]))
            edge.append(int(node[i][2]))
            word[i + 1] = node[i][1]
        elif len(node[i]) == 4:  # 자식 노드 2개
            edge.append(int(node[i][0]))
            edge.append(int(node[i][2]))
            edge.append(int(node[i][0]))
            edge.append(int(node[i][3]))
            word[i + 1] = node[i][1]

    # 왼쪽 자식 노드(인덱스가 부모 노드 번호)
    left_child = [0] * (N + 1)
    # 오른쪽 자식 노드(인덱스가 부모 노드 번호)
    right_child = [0] * (N + 1)

    # 부모노드와 자식노드 쌍으로 있으므로 범위는 E의 두배까지
    for i in range(0, E*2, 2):
        # 간선 정보 리스트를 순회하면서 우선 왼쪽 자식노드 없으면 채움
        if not left_child[edge[i]]:  # edge[i] : 부모노드 번호 >> 인덱스가 곧 부모노드
            left_child[edge[i]] = edge[i + 1]
        # 왼쪽 자식 있으면 오른쪽 채움
        else:
            right_child[edge[i]] = edge[i + 1]

    print('#{}'.format(tc), end=' ')
    in_order(1)
    print()