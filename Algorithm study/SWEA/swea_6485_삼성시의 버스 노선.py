# 테스트케이스
T = int(input())

for tc in range(1, T+1):
    # 버스 노선 개수
    N = int(input())

    # Ai, Bi 버스정류장
    AB = [list(map(int, input().split())) for _ in range(N)]

    P = int(input())
    Cj = [int(input()) for _ in range(P)]

    # N회 반복하며 정류장을 지나는 노선 체크
    # 확인하려는 정류장 수만큼 배열 생성
    bus_stops = [0] * 5000
    for i in range(N):
        # Ai 부터 Bi까지 버스 정류장들에 1 더함
        for j in range(AB[i][0]-1, AB[i][1]):
            bus_stops[j] += 1

    # 각 정류소를 지나는 노선 개수 입력
    result = []
    for i in Cj:
        result += [bus_stops[i-1]]

    print('#{}'.format(tc), *result)
