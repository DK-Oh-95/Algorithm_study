# 테스트케이스 입력
T = int(input())

for tc in range(1, T+1):
    # 퍼즐 크기 N, 단어 길이 K 입력
    n, k = map(int, input().split())
    # 퍼즐 모양 입력
    puzzle = [list(map(int, input().split())) for _ in range(n)]

    # 행, 열을 순회하면서 글자가 들어갈 수 있는 공간의 길이가
    # 넣으려고 하는 단어의 길이와 같으면 결과에 1씩 더한다
    result = 0
    for i in range(n):
        cnt = 0
        # 행 순회
        for j in range(n):
            if puzzle[i][j] == 1:
                cnt += 1
            # 0이나 퍼즐의 끝에 도달했을 때
            if puzzle[i][j] == 0 or j == n-1:
                # 글자가 들어갈 수 있는 길이가 단어 길이와 같으면 결과에 추가
                if cnt == k:
                    result += 1
                cnt = 0

        # 열 순회
        for j in range(n):
            if puzzle[j][i] == 1:
                cnt += 1
            # 0이나 퍼즐의 끝에 도달했을 때
            if puzzle[j][i] == 0 or j == n - 1:
                # 글자가 들어갈 수 있는 길이가 단어 길이와 같으면 결과에 추가
                if cnt == k:
                    result += 1
                cnt = 0

    print('#{} {}'.format(tc, result))
