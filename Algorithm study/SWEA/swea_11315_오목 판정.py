def find_gomoku(arr):
    # 배열 순회하면서 우, 우하, 하, 좌하 방향으로 o가 연속 5개면 YES 반환
    for i in range(N):
        for j in range(N):
            # o를 만났을 때 각 방향 탐색 시 o가 있다면 연속으로 몇 개 인지 확인
            if arr[i][j] == 'o':
                for dr, dc in [(0, 1), (1, 1), (1, 0), (1, -1)]:
                    cnt = 0
                    for d in range(1, 5):
                        nr, nc = i + dr*d, j + dc*d
                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'o':
                            cnt += 1
                        else:
                            break
                    # 4개가 되기 전에 빈칸 만나면 중지
                    if cnt == 4:
                        return 'YES'
    return 'NO'

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 오목판 입력
    gomoku = [input() for _ in range(N)]

    print('#{} {}'.format(tc, find_gomoku(gomoku)))
