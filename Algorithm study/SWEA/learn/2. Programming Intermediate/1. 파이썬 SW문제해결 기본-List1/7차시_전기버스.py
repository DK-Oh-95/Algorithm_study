# 최소 충전 횟수 계산 함수 생성
def charging_number(K, N, M_list):
    # 정류장 사이의 거리가 최대 이동거리보다 길면 0 출력
    for i in range(len(M_list) - 1):
        if M_list[i + 1] - M_list[i] > K:
            return 0

    # 처음 버스 위치
    first_position = 0
    # 현재 버스 위치
    current_position = 0
    # 충전횟수
    cnt = 0
    # 현재 버스위치가 종착역에서 최대 이동 가능 거리를 뺀만큼보다 큰 인덱스 정류장에 도착할때까지 반복한 횟수가 충전횟수
    while not current_position >= N - K:
        # 현재 위치에서 이동가능거리를 하나씩 늘려가며 충전소에 해당되면 현재위치 수정
        first_position = current_position
        for i in range(1, K + 1):
            if first_position + i in M_list:
                current_position = first_position + i
        # 충전소 위치가 정해지는 것이 곧 충전 횟수
        cnt += 1
    return cnt

# 테스트케이스 T 입력
T = int(input())

for tc in range(1, T+1):
    # K, N, M 띄어쓰기로 구분 입력해서 각각 할당
    KNM = list(map(int, input().split()))
    K = KNM[0]
    N = KNM[1]
    M = KNM[2]
    # M 정류장 번호 입력
    M_list = list(map(int, input().split()))

    print('#{} {}'.format(tc, charging_number(K, N, M_list)))