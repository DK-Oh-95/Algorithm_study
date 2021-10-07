T = 10
for tc in range(1, T+1):
    # 한 변 길이
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 테이블 순회하면서 N극 밑에 S극이 있는 쌍의 개수가 교착상태 수
    # N극: 1, S극: 2
    cnt = 0  # 교착상태 수
    for i in range(n):
        stack = []
        for j in range(n):
            # 열 우선순회 중 N극을 만났을 때 스택의 top이 1이면 pop하고 push
            if arr[j][i] == 1 and stack and stack[-1] == 1:
                stack.pop()
                stack.append(1)
            # 열 우선순회 중 N극을 만나고 스택 비어있으면 push
            elif arr[j][i] == 1 and not stack:
                stack.append(1)
            # S극 만났을 때 스택의 top이 1이면 pop하고 카운트
            elif arr[j][i] == 2 and stack and stack[-1] == 1:
                stack.pop()
                cnt += 1
    print('#{} {}'.format(tc, cnt))
