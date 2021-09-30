T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    result = ''
    # 짝수면 마지막 비트 0
    if not M % 2:
        result = 'OFF'
    else:
        cnt = 0
        # N회 동안 2로 나눠서 모두 나머지 1이면 ON
        for i in range(N):
            if M % 2:
                cnt += 1
                M //= 2
        if cnt == N :
            result = 'ON'
        else:
            result = 'OFF'

    print('#{} {}'.format(tc, result))
