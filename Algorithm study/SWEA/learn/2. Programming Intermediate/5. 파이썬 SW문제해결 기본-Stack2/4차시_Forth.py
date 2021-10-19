# 테스트케이스
T = int(input())

for tc in range(1, T+1):
    # 계산식 입력
    formula = list(input().split())
    n = len(formula)
    # 계산식을 순회하면서 숫자 만나면 스택에 push하고
    # 연산 만나면 스택에 있는 숫자 2개 pop해서 계산한 다음 결과 push
    # 빈 스택에서 pop하면 error 출력
    # .로 계산이 끝났는데 스택에 값이 2개 이상이면 error 출력
    stack = []
    try:
        for i in range(n-1):
            if formula[i] == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif formula[i] == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif formula[i] == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif formula[i] == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 // num2)
            # 사칙연산이 아닌경우 >> 숫자
            else:
                stack.append(int(formula[i]))
        # 계산 결과가 하나가 아니면 error 출력
        if len(stack) == 1:
            result = stack.pop()
        else:
            result = 'error'
    # 빈 스택에서 pop 한 경우
    except IndexError:
        result = 'error'

    print('#{} {}'.format(tc, result))
