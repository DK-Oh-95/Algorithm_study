# 테스트케이스
T = int(input())

for tc in range(1, T+1):
    # 행렬크기 N
    N = int(input())
    # 행렬 정보
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 배열을 90도 회전시켜 새로운 배열 생성
    arr_90 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_90[i][j] = arr[N-1-j][i]
    # 90도 회전 시킨 배열을 다시 회전
    arr_180 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_180[i][j] = arr_90[N - 1 - j][i]
    # 180도 회전 시킨 배열을 다시 회전
    arr_270 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_270[i][j] = arr_180[N - 1 - j][i]

    # 출력 조건에 맞춤
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print('{}'.format(arr_90[i][j]), end='')
        print(end=' ')
        for j in range(N):
            print('{}'.format(arr_180[i][j]), end='')
        print(end=' ')
        for j in range(N):
            print('{}'.format(arr_270[i][j]), end='')
        print()