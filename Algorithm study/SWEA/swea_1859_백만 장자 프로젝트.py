# 테스트케이스
T = int(input())

for tc in range(1, T+1):
    # 매매가 개수 N
    N = int(input())
    # 매매가
    prices = list(map(int, input().split()))

    # 크기 비교를 위한 현재 위치 변수
    current_idx = N - 1
    # 판매가를 더할 변수
    sum_v = 0
    # 거꾸로 탐색하며 자기보다 작은 값들을 더함
    for i in reversed(range(N)):
        if prices[current_idx] > prices[i]:
            sum_v += (prices[current_idx] - prices[i])
        # 현재 위치보다 더 큰 값을 가진 인덱스를 발견하면 위치 변경
        elif prices[current_idx] < prices[i]:
            current_idx = i

    print('#{} {}'.format(tc, sum_v))
