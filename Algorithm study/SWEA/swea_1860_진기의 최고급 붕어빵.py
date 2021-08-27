# 1000개 중에 993개 맞음

T = int(input())

for tc in range(1, T+1):
    # 사람 수 N, M초의 시간, K개의 붕어
    N, M, K = list(map(int, input().split()))
    # 사람들 도착하는 시간 초
    seconds = list(map(int, input().split()))
    seconds.sort()

    # 같은 시간에 오는 사람 수
    num_s = [0] * 11112
    for i in seconds:
        num_s[i] += 1

    # 시간마다 만들어진 붕어빵 개수
    fish = [0] * 11112
    result = 'Possible'
    for i in range(1, 11112):
        fish[i] = fish[i - 1]
        if i % M == 0:
            fish[i] += K

        fish[i] -= num_s[i]
        if fish[i] < 0:
            result = 'Impossible'
            break

    print('#{} {}'.format(tc, result))
