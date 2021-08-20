# 테스트케이스
T = int(input())

for tc in range(1, T+1):
    # 쇠막대기, 레이저 괄호 입력
    stick = input()
    n = len(stick)

    # 여는 괄호 만나면 스택에 push, 닫는괄호 만나면 pop
    stack = []
    cnt = 0
    for i in range(n):
        if stick[i] == '(':
            stack.append(stick[i])
        # 닫는 괄호가 여는괄호 바로 뒤에 있다면(레이저인 경우)
        # pop할 때 스택에 남아있는 요소 개수 더함
        elif stick[i] == ')' and stick[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        # 막대기가 끝나는 지점에선 해당 막대기 마지막 조각 추가하고 pop
        elif stick[i] == ')':
            cnt += 1
            stack.pop()

    print('#{} {}'.format(tc, cnt))