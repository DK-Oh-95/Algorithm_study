# 행, 열, 사각형으로 순회하면서 기록하고.
# 기록이 1이 아니면 스도쿠 아님 >> 0 반환
def sudoku(arr):
    # 퍼즐 크기
    N = len(arr)

    # 행 검사
    for i in range(N):
        # 확인한 숫자 기록
        visited = [0] * (N + 1)
        for j in range(N):
            visited[arr[i][j]] += 1
        # 1~9번 인덱스 값이 1이 아니면 0 반환
        for d in range(1, N+1):
            if visited[d] != 1:
                return 0
    # 열 검사
    for i in range(N):
        # 확인한 숫자 기록
        visited = [0] * (N + 1)
        for j in range(N):
            visited[arr[j][i]] += 1
        # 1~9번 인덱스 값이 1이 아니면 0 반환
        for d in range(1, N+1):
            if visited[d] != 1:
                return 0

    # 사각형 검사 (행렬을 3씩 구간을 나눠서 반복한다
    for k in range(0, N, 3):
        for m in range(0, N, 3):
            # 확인한 숫자 기록
            visited = [0] * (N + 1)
            for i in range(k, k+3):
                for j in range(m, m+3):
                    visited[arr[i][j]] += 1
            # 1~9번 인덱스 값이 1이 아니면 0 반환
            for d in range(1, N+1):
                if visited[d] != 1:
                    return 0
    # 모든 검사에서 이상 없으면 1 반환
    return 1

# 테스트케이스
T = int(input())

for tc in range(1, T+1):
    # 스도쿠 퍼즐 입력
    puzzle = [list(map(int, input().split())) for _ in range(9)]

    print('#{} {}'.format(tc, sudoku(puzzle)))