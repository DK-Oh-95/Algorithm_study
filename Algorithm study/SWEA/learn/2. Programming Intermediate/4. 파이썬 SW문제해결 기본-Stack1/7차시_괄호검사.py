def bracket(string):
    # 문자열을 순회하면서 여는 괄호 나오면 push, 닫는 괄호 나오면 pop 해서 비교
    # 1. 여는 괄호와 닫는 괄호의 개수가 같아야 한다
    # 2. 여는괄호가 닫는 괄호보다 먼저 나와야한다
    # 3. 괄호 사이에는 포함 관계만 존재한다
    stack = []
    try:
        for i in range(len(string)):
            # 여는 괄호 만나면 push
            if string[i] == '(' or string[i] == '{' or string[i] == '[':
                stack.append(string[i])
            # 닫는 괄호 만나면 pop하고 짝 맞는지 확인
            elif string[i] == ')':
                if stack.pop() != '(':
                    return 0
            elif string[i] == '}':
                if stack.pop() != '{':
                    return 0
            elif string[i] == ']':
                if stack.pop() != '[':
                    return 0

    # 닫는 괄호 만났는데 스택 비어있으면 오류 >> 0 반환
    except IndexError:
        return 0

    if stack:
        return 0
    else:
        return 1


# 테스트케이스
T = int(input())

for tc in range(1, T+1):
    # 입력받은 문자열 리스트로 변환
    string_input = ('!'.join(input())).split('!')

    print('#{} {}'.format(tc, bracket(string_input)))
