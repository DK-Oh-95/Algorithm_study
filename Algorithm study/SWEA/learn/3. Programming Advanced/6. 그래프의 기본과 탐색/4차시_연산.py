def calc(n, idx):
    # +1, -1, *2, -10
    if idx == 0: return n + 1
    elif idx == 1: return n - 1
    elif idx == 2: return n * 2
    else: return n - 10


def bfs():
    # 선형 큐 생성 (collections의 deque와 동일)
    Q = [0] * 1000000
    front = rear = -1

    rear += 1
    Q[rear] = N
    memo[N] = 0

    while front != rear:  # 큐가 공백상태가 될 때까지
        front += 1
        num = Q[front]

        if num == M:  # 지금 뽑은 값이 N과 같다면 해당 횟수를 반환한다
            return memo[num]

        for i in range(4):
            next_num = calc(num, i)
            # 중간 연산 결과는 100만 이하의 자연수
            if 0 < next_num <= 1000000 and memo[next_num] == -1:  # 새로 만든 숫자가 범위 안이고 아직 만든적이 없다면
                memo[next_num] = memo[num] + 1
                rear += 1
                Q[rear] = next_num
    return -1  # 만약에 M을 만들지 못한 경우


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    memo = [-1] * 1000001  # 중복된 숫자를 기록하기 위해 (중간 결과는 100만 이하)

    print('#{} {}'.format(tc, bfs()))
