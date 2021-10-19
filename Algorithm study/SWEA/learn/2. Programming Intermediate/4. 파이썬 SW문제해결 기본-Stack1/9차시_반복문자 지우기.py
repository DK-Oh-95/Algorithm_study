# 테스트케이스
T = int(input())

for tc in range(1, T+1):
    # 문자열 입력
    string = input()

    # 문자열을 순회하면서 하나씩 push하고,
    # 현재 스택의 top과 동일하다면 pop
    # 스택에 남아있는 문자열 출력
    stack = []
    top = ''
    for i in range(len(string)):
        if top == string[i]:
            stack.pop()
            # 스택이 비어 있는 경우는 top을 빈 문자열로 지정
            if not stack:
                top = ''
            else:
                top = stack[-1]
        else:
            stack.append(string[i])
            top = stack[-1]

    print('#{} {}'.format(tc, len(stack)))