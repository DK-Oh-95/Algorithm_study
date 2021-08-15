# 테스트케이스 입력
T = int(input())

for tc in range(1, T+1):
    # 퍼즐 크기 N, 단어 길이 K 입력
    n, k = map(int, input().split())
    # 퍼즐 모양 입력
    puzzle = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            # 행
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == n-1:
                if cnt == k:
                    result += 1
                cnt = 0

            # 열
        for j in range(n):
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == n - 1:
                if cnt == k:
                    result += 1
                cnt = 0

    print('#{} {}'.format(tc, result))
