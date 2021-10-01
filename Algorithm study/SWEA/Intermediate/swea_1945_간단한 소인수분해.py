# 테스트케이스 입력
T = int(input())

for tc in range(1, T+1):
    # 소인수분해 대상 숫자 입력
    N = int(input())

    # 2, 3, 5, 7, 11의 계수 설정
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    # N을 나눠 1이 될 때까지 반복
    while not N == 1:
        if N % 2 == 0:
            N /= 2
            a += 1
        elif N % 3 == 0:
            N /= 3
            b += 1
        elif N % 5 == 0:
            N /= 5
            c += 1
        elif N % 7 == 0:
            N /= 7
            d += 1
        elif N % 11 == 0:
            N /= 11
            e += 1

    print('#{} {} {} {} {} {}'.format(tc, a, b, c, d, e))
