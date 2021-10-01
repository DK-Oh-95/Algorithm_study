# 좌,우,하를 탐색하기 위한 dr, dc 생성
dr = [0, 0, 1]
dc = [-1, 1, 0]

# 테스트케이스는 10개
for _ in range(10):
    tc = int(input())

    # 사다리 입력
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 첫번째 행을 탐색하면서 1을 만나면 아래로 이동
    for j in range(100):
        if ladder[0][j] == 1:
            current_r = 0
            current_c = j

            # 이전상태 변수 생성
            tmp = 2  # 좌 : 0, 우 : 1, 하 : 2
            # 사다리 따라 내려가며 2 만날때까지 시행
            # 마지막이 1인 사다리는 row 인덱스 범위까지 반복
            while current_r < 99:
                # 주변 1의 개수 변수 생성
                cnt = 0
                # 현재 위치에서 좌,우,하를 탐색하고 1이 하나면 아래로, 두개 이상이면 이전 상태를 토대로 이동
                for d in range(3):
                    check_r, check_c = current_r+dr[d], current_c+dc[d]
                    # current_r, current_c 정상범위이면서 값이 1일 때 cnt를 하나씩 올림
                    if 0 <= check_r < 100 and 0 <= check_c < 100 and ladder[check_r][check_c] == 1:
                        cnt += 1

                # 주변에 1이 2개 이상이고 tmp가 2일 때(아래로 이동중일 때) 좌우를 탐색해서 1인곳으로 이동
                if cnt > 1 and tmp == 2:
                    if current_c-1 >= 0 and ladder[current_r][current_c-1] == 1:
                        current_c -= 1
                        tmp = 0
                    elif current_c+1 < 100 and ladder[current_r][current_c+1] == 1:
                        current_c += 1
                        tmp = 1
                # 주변에 1이 2개 이상이고 아래에 1이 없을 때 tmp를 확인해서 그대로 이동
                elif cnt > 1 and ladder[current_r+1][current_c] == 0:
                    # 왼쪽으로 가던중
                    if tmp == 0:
                        current_c -= 1
                    # 오른쪽으로 가던중
                    elif tmp == 1:
                        current_c += 1
                # 주변에 1이 2개 이상이고 좌or우로 이동 중 아래에 1이 있을 때 아래로 이동
                elif cnt > 1 and tmp != 2 and ladder[current_r+1][current_c] ==1:
                    current_r += 1
                    tmp = 2
                # 주변에 1이 하나뿐이면 아래로 이동
                else:
                    current_r += 1
                    tmp = 2

                # 현재 값이 2면 그때의 j 값 출력
                if ladder[current_r][current_c] == 2:
                    result = j

    print('#{} {}'.format(tc, result))