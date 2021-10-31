from collections import deque


def bfs():
    Q = deque()
    Q.append(N)
    memo[N] = True

    ans = 0
    while Q:  # 큐가 공백상태가 될 때까지
        size = len(Q)

        for i in range(size):
            num = Q.popleft()
            if num == M: return ans

            for j in (num+1, num-1, num*2, num-10):
                if 0 < j <= 1000000 and not memo[j]:
                    memo[j] = True
                    Q.append(j)
        ans += 1
    return -1  # 만약에 M을 만들지 못한 경우


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    memo = [False] * 1000001  # 중복된 숫자를 기록하기 위해 (중간 결과는 100만 이하)

    print('#{} {}'.format(tc, bfs()))
