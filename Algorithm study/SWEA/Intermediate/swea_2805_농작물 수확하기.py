T = int(input())
for tc in range(1, T+1):
    # 농장크기 N
    N = int(input())
    # 농장
    farm = [input() for _ in range(N)]

    # 열의 인덱스 값과 N의 중앙값의 차이만큼 행을 참조한다
    sum_v = 0
    for i in range(N):
        for j in range(abs(i - N//2), N - abs(i - N//2)):
            sum_v += int(farm[i][j])

    print('#{} {}'.format(tc, sum_v))