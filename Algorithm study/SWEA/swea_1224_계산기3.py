# 테스트케이스 10개
T = 10

for tc in range(1, T+1):
    # 테스트케이스 길이
    n = int(input())
    # 계산식
    formula = input()

    # 계산식 순회하면서 숫자면 바로 담고
    # 연산은 스택에 쌓는다 (우선순위 높으면 바로 답고 낮으면 pop하면서 더 낮은거 나올때 push)
    # +,- : 1, *,/ : 2
    # 여는괄호는 icp는 3 isp는 0, 닫는 괄호 만나면 여는괄호 나올때까지 pop
    stack = []
    postfix = []
    for i in range(n):
        # 여는괄호 만나면 스택에 push (우선순위 가장 높음)
        if formula[i] == '(':
            stack.append(formula[i])
        # 닫는괄호 만나면 여는괄호 만날때까지 pop하고 여는괄호 지움
        elif formula[i] == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        elif formula[i] == '*':
            # 스택의 top이 같은 우선순위인 연산이면 pop
            if stack[-1] == '*':
                postfix.append(stack.pop())
                stack.append(formula[i])
            # +, ( 인 경우는 우선순위 낮으므로 push
            else:
                stack.append(formula[i])
        elif formula[i] == '+':
            # +일 때 스택의 top의 우선순위가 더 높으면 낮은 연산 나올때까지 pop
            # 문제에선 (, +, * 밖에 없으므로 ( 나올때까지 pop
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.append(formula[i])
        # 숫자는 바로 후위 표현식에 담는다 (연산 아닐때)
        else:
            postfix.append(int(formula[i]))
    # 문제에선 괄호가 정상적으로 작성되어 있으므로 스택에 남아있는 연산을 비울 필요 없다

    # 생성한 후위 표현식 계산
    result = []
    for j in range(len(postfix)):
        # 숫자면 바로 push
        if postfix[j] != '+' and postfix[j] != '*':
            result.append(postfix[j])
        # + 만나면 push한 값들 중 2개 더해서 다시 push
        elif postfix[j] == '+':
            tmp = result.pop() + result.pop()
            result.append(tmp)
        # * 만나면 push한 값들 중 2개 곱해서 다시 push
        elif postfix[j] == '*':
            tmp = result.pop() * result.pop()
            result.append(tmp)

    print('#{} {}'.format(tc, *result))
