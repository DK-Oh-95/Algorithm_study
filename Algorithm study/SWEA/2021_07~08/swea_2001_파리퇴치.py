# 테스트케이스
T = int(input())

for tc in range(1, T+1):
    # 배열크기 N, 파리채크기 M 입력
    n, m = map(int, input().split())
    # 배열 입력
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 합들의 최대값 변수 생성
    max_sum = 0
    # 전체 배열을 순회하면서 범위 m인 값들만 더함
    for e in range(0, n-(m-1)):
        for k in range(0, n-(m-1)):
            # 부분합 변수 생성
            sum_v = 0
            for i in range(e, e+m):
                for j in range(k, k+m):
                    sum_v += arr[i][j]
            # 최대값보다 크면 할당
            if sum_v > max_sum:
                max_sum = sum_v

    print('#{} {}'.format(tc, max_sum))