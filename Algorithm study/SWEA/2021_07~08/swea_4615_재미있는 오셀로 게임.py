# 테스트케이스
T = int(input())

for tc in range(1, T+1):
    # 보드 길이 N, 돌 놓는 횟수 M
    N, M = map(int, input().split())

    # N x N 오셀로판 생성
    othello = list([0] * N for _ in range(N))
    # 처음 돌 배치 / 1: 흑돌, 2: 백돌
    othello[N//2 - 1][N//2 - 1] = 2
    othello[N//2 - 1][N//2] = 1
    othello[N//2][N//2 - 1] = 1
    othello[N//2][N//2] = 2

    # 8방향 탐색을 위한 dr, dc
    # 0~7 인덱스 : 위부터 시계방향
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    # M회 만큼 돌 놓음
    for _ in range(M):
        # 문제의 좌표는 일반적인 행열과 반대
        c, r, s_color = map(int, input().split())

        othello[r-1][c-1] = s_color

        # 돌을 놓은 곳 기준으로 8방향 탐색하여 규칙에 해당하는지 확인
        for i in range(8):
            # 현재 위치 기록
            current_r = r - 1
            current_c = c - 1
            # 돌 위치를 기록할 리스트
            location = []

            # 흑돌일 때
            if s_color == 1:
                # 놓은 돌 주변에 백돌을 발견하면
                if 0 <= current_r + dr[i] < N and 0 <= current_c + dc[i] < N and othello[current_r + dr[i]][current_c + dc[i]] == 2:
                    # 해당 방향으로 흑돌을 만날때까지 계속 참조
                    try:
                        while othello[current_r + dr[i]][current_c + dc[i]] != 1:
                            # 백돌들의 위치 기록
                            current_r += dr[i]
                            current_c += dc[i]
                            location += [[current_r, current_c]]
                        # 파이썬 특성 상 음수도 인덱스 참조가 되므로 그 때도 고려해준다
                        if current_r + dr[i] < 0 or current_c + dc[i] < 0:
                            continue
                    # 다른 색 돌을 만나지 못하고 인덱스 에러가 나면 다른방향 참조
                    except IndexError:
                        continue
                    # 흑돌을 만났을 때 사이에 기록한 위치들이 모두 백돌이면 색 바꿈 (빈공간이 없으면)
                    location_v = []
                    for m in range(len(location)):
                        location_v += [othello[location[m][0]][location[m][1]]]
                    if 0 not in location_v:
                        for j in range(len(location)):
                            othello[location[j][0]][location[j][1]] = 1

            # 백돌일 때
            elif s_color == 2:
                # 놓은 돌 주변에 흑돌을 발견하면
                if 0 <= current_r + dr[i] < N and 0 <= current_c + dc[i] < N and othello[current_r + dr[i]][current_c + dc[i]] == 1:
                    # 해당 방향으로 백돌을 만날때까지 계속 참조
                    try:
                        while othello[current_r + dr[i]][current_c + dc[i]] != 2:
                            # 흑돌들의 위치 기록
                            current_r += dr[i]
                            current_c += dc[i]
                            location += [[current_r, current_c]]
                        # 파이썬 특성 상 음수도 인덱스 참조가 되므로 그 때도 고려해준다
                        if current_r + dr[i] < 0 or current_c + dc[i] < 0:
                            continue
                    # 다른 색 돌을 만나지 못하고 인덱스 에러가 나면 다른방향 참조
                    except IndexError:
                        continue
                    # 백돌을 만났을 때 사이에 기록한 위치들이 모두 흑돌이면 색 바꿈 (빈공간이 없으면)
                    location_v = []
                    for m in range(len(location)):
                        location_v += [othello[location[m][0]][location[m][1]]]
                    if 0 not in location_v:
                        for j in range(len(location)):
                            othello[location[j][0]][location[j][1]] = 2

    # 모든 돌 두기가 끝나면 개수 확인 후 출력
    black = 0
    white = 0
    for d in range(N):
        for k in range(N):
            if othello[d][k] == 1:
                black += 1
            elif othello[d][k] == 2:
                white += 1

    print('#{} {} {}'.format(tc, black, white))