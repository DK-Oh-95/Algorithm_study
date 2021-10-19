def paper(number):
    n = number // 10
    memo = [0] * n
    memo[0] = 1
    memo[1] = 3

    # 원하는 크기의 경우의 수는 이전 크기의 경우의 수 더하기,
    # 2단계 전 경우의 수의 2배
    # 이유 : 전 단계에서 크기 10짜리를 추가하는 경우는 똑같고
    #       2단계 전 경우는 크기 20짜리를 추가하는 경우 2가지이기 때문
    for i in range(2, n):
        memo[i] = memo[i-1] + memo[i-2] * 2

    return memo[n-1]

# 테스트케이스
T = int(input())

for tc in range(1, T+1):
    # 가로 길이 N 입력
    N = int(input())

    print('#{} {}'.format(tc, paper(N)))

