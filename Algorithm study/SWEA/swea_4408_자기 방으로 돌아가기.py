# 테스트케이스
T = int(input())

for tc in range(1, T+1):
    # N : 돌아가야 할 학생들의 수
    N = int(input())

    # 돌아가야할 학생들의 현재 방과 돌아갈 방
    rooms = [list(map(int, input().split())) for _ in range(N)]

    # 방들의 길이는 200
    arr = [0] * 200
    # 사람이 지나가면 1씩 추가
    for i in range(N):
        # 출발 위치가 도착 위치보다 앞일 경우
        if rooms[i][0] <= rooms[i][1]:
            # 인덱스로 참조할 것이기 때문에 방번호에서 1씩 빼서 2로 나눔
            start = (rooms[i][0] - 1) // 2
            end = (rooms[i][1] - 1) // 2
        # 출발 위치가 도착 위치보다 뒤일 경우
        else:
            start = (rooms[i][1] - 1) // 2
            end = (rooms[i][0] - 1) // 2
        # 지나간 경로에 1씩 추가
        for j in range(start, end + 1):
            arr[j] += 1

    # 겹친 구간의 최대값 구함
    max_v = 0
    for i in range(200):
        if max_v < arr[i]:
            max_v = arr[i]

    print('#{} {}'.format(tc, max_v))