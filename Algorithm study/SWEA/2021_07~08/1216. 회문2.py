def palindrome(arr):
    # 글자판 크기
    N = len(arr)

    # 회문 길이 비교할 변수
    result_r = 0
    result_c = 0

    # 행 우선 순회
    for i in range(N):
        # 찾을 패턴의 길이(최대길이부터 하나씩 줄임)
        for M in range(100, 1, -1):
            for j in range(N - M + 1):
                # 회문인지 검사하기 위한 변수
                is_pal = True
                # 찾고자 하는 회문 길이의 절반만큼 반대쪽과 같은지 판별
                for d in range(M//2):
                    # 회문 아님
                    if arr[i][j + d] != arr[i][j + M - d - 1]:
                        is_pal = False
                        break
                # 반복문을 모두 마치고 회문임이 판별되면 그때의 찾는 패턴길이 M이 회문 길이
                if is_pal == True:
                    if result_r < M:
                        result_r = M
                    break

    # 열 우선 순회
    for i in range(N):
        # 찾을 패턴의 길이(최대길이부터 하나씩 줄임)
        for M in range(100, 1, -1):
            for j in range(N - M + 1):
                # 회문인지 검사하기 위한 변수
                is_pal = True
                # 찾고자 하는 회문 길이의 절반만큼 반대쪽과 같은지 판별
                for d in range(M // 2):
                    # 회문 아님
                    if arr[j + d][i] != arr[j + M - d - 1][i]:
                        is_pal = False
                        break
                # 반복문을 모두 마치고 회문임이 판별되면 그때의 찾는 패턴길이 M이 회문 길이
                if is_pal == True:
                    if result_c < M:
                        result_c = M
                    break

    # row, column 중 더 큰 값 반환
    if result_r > result_c:
        return result_r
    else:
        return result_c

# 테스트케이스는 총 10개
for _ in range(10):
    tc = int(input())
    # 각 테스트케이스의 글자판
    words = [input() for _ in range(100)]

    print('#{} {}'.format(tc, palindrome(words)))