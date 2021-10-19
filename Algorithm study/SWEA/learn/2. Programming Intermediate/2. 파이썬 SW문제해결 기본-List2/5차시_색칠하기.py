# 테스트케이스 입력
T = int(input())

for tc in range(1, T+1):
    # 처음 10 x 10 격자 생성(곱셈을 할 것이기 때문에 1로 값 지정)
    # 현재 문제엔 해당 안되지만 덧셈으로 구별할 시 red 상자가 여러번 겹치면 판단이 안되므로 곱셈으로 계산
    Box = [[1] * 10 for _ in range(10)]

    # 영역 개수 N, 인덱스 r/c, 색 color 입력
    N = int(input())
    RC = [list(map(int, input().split())) for _ in range(N)]
    # r1 = RC[i][0]
    # c1 = RC[i][1]
    # r2 = RC[i][2]
    # c2 = RC[i][3]

    for e in range(N):
        # color가 red라면 해당 영역에 2를 곱함
        if RC[e][4] == 1:
            # 입력받은 값에서 r1~r2, c1~c2만큼만 범위 반복
            for i in range(RC[e][0], RC[e][2]+1):
                for j in range(RC[e][1], RC[e][3]+1):
                    Box[i][j] *= 2
        # color가 red라면 해당 영역에 3을 곱함
        elif RC[e][4] == 2:
            # 입력받은 값에서 r1~r2, c1~c2만큼만 범위 반복
            for i in range(RC[e][0], RC[e][2] + 1):
                for j in range(RC[e][1], RC[e][3] + 1):
                    Box[i][j] *= 3

    # 전체 격자를 참조하면서 겹친 부분은 6으로 나누어 떨어진다
    # 값이 3 이상인 구역의 개수를 카운트하면 그 값이 넓이
    cnt = 0
    for i in range(10):
        for j in range(10):
            if Box[i][j] % 6 == 0:
                cnt += 1

    print('#{} {}'.format(tc, cnt))