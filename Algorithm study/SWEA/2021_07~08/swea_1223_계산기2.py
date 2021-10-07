# 테스트케이스 10개
T = 10

for tc in range(1, T+1):
    # 테스트케이스 길이
    N = int(input())
    # 계산식
    formula = input()

    # 계산식을 순회하면서 숫자 만나면 바로 출력 (후위계산식에 넣음)
    # 사칙연산 만나면 우선순위가 높으면 바로 스택에 넣고
    # 우선순위가 낮으면 더 낮은 연산 만날때까지 pop
    # 우선 순위 : +,- >> 1, *,/ >> 2
    stack = []
    top = 0
    post_formula = []
    for i in range(N):
        # 숫자 만나면(+, * 아니면) 추후 계산을 위해 정수형으로 변환
        if formula[i] != '+' and formula[i] != '*':
            post_formula += [int(formula[i])]
        # 연산 만났을 때 스택 비어있으면 push
        elif not stack:
            stack.append(formula[i])
            top = stack[-1]
        # 연산 만났을 때 우선순위 높으면 push
        elif formula[i] == '*' and top == '+':
            stack.append(formula[i])
            top = stack[-1]
        # 나머지 경우는 (*,* / +,+ / +,*) 우선순위가 높지 않으므로 pop
        else:
            # *일 때 스택의 top이 +나 빌 때까지
            if formula[i] == '*':
                while top != '+':
                    if not stack:
                        break
                    post_formula += stack.pop()
                    if not stack:
                        continue
                    top = stack[-1]
                stack.append(formula[i])
                top = stack[-1]
            # +일 떈 스택이 빌 때까지
            elif formula[i] == '+':
                while stack:
                    post_formula += stack.pop()
                    if not stack:
                        continue
                    top = stack[-1]
                stack.append(formula[i])
                top = stack[-1]
    # 작업이 끝난 후 스택이 남아있으면 빌때까지 pop
    while stack:
        post_formula += stack.pop()
        top = 0

    # 생성한 후위 표현식 계산
    stack_result = []
    for j in range(N):
        if post_formula[j] != '+' and post_formula[j] != '*':
            stack_result.append(post_formula[j])
        # + 만나면 push한 값들 중 2개 더해서 다시 push
        elif post_formula[j] == '+':
            tmp = stack_result.pop() + stack_result.pop()
            stack_result.append(tmp)
        # * 만나면 push한 값들 중 2개 곱해서 다시 push
        elif post_formula[j] == '*':
            tmp = stack_result.pop() * stack_result.pop()
            stack_result.append(tmp)

    print('#{} {}'.format(tc, stack_result.pop()))
