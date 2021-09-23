def post_order(v):
    # v : 현재 정점의 번호
    if v == 0:
        return
    # 후위 계산식 생성
    post_order(left_child[v])
    post_order(right_child[v])
    stack.append(tree[v])


for tc in range(1, 11):
    N = int(input())
    formula = [list(input().split()) for _ in range(N)]

    # 이진트리 생성
    left_child = [0] * (N + 1)
    right_child = [0] * (N + 1)
    tree = [0] * (N + 1)

    # 왼쪽자식노드, 오른쪽자식노드, 트리 생성
    for i in range(N):
        try:
            tree[i+1] = int(formula[i][1])  # int 자료형 변환 안되면 사칙연산
        except ValueError:
            left_child[i+1] = int(formula[i][2])
            right_child[i+1] = int(formula[i][3])
            tree[i+1] = formula[i][1]

    stack = []
    post_order(1)
    # 생성된 후위계산식 계산
    while stack:
        for i in range(len(stack)):
            if type(stack[i]) != int:
                if stack[i] == '+':
                    result = stack.pop(i - 2) + stack.pop(i - 2)
                    stack.pop(i - 2)
                    stack.insert(i - 2, result)
                    break
                elif stack[i] == '-':
                    result = stack.pop(i - 2) - stack.pop(i - 2)
                    stack.pop(i - 2)
                    stack.insert(i - 2, result)
                    break
                elif stack[i] == '*':
                    result = stack.pop(i - 2) * stack.pop(i - 2)
                    stack.pop(i - 2)
                    stack.insert(i - 2, result)
                    break
                elif stack[i] == '/':
                    result = stack.pop(i - 2) / stack.pop(i - 2)
                    stack.pop(i - 2)
                    stack.insert(i - 2, result)
                    break
        if len(stack) == 1:
            break

    result = stack.pop()
    print('#{} {}'.format(tc, int(result)))
