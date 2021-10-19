# 테스트케이스 T 입력
T = int(input())

for tc in range(1, T+1):
    # 정수 개수, 더하는 개수 입력후 각각 할당
    NM = list(map(int, input().split()))
    N = NM[0]
    M = NM[1]
    # 숫자 리스트 입력
    aj = list(map(int, input().split()))

    # 숫자 리스트에서 M개씩 더한 값의 최대 최소값 비교
    # 비교를 위해 처음 M개 값의 합을 각 변수에 할당
    max_sum = 0
    min_sum = 0
    for i in range(M):
        max_sum += aj[i]
        min_sum += aj[i]

    # 각 테스트케이스에서 리스트의 처음 M개만큼의 합과 순차적으로 인덱스를 증가시키며 M개씩 더한 구간합을 비교
    for i in range(1, N-(M-1)):
        # 각 인덱스에서 M만큼의 구간합 계산
        partitial_sum = 0
        for j in range(i, M+i):
            partitial_sum += aj[j]
        # 구간합이 현재 할당한 최대값보다 크면 최대값으로 재할당
        if partitial_sum > max_sum:
            max_sum = partitial_sum
        # 구간합이 현재 할당한 최소값보다 작으면 최소값으로 재할당
        elif partitial_sum < min_sum:
            min_sum = partitial_sum

    difference_sum = max_sum - min_sum
    print('#{} {}'.format(tc, difference_sum))