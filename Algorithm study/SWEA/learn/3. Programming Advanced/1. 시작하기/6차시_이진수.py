def hex_to_decimal(c):
    # 문자열이기 때문에 쉽게 변환하기 위해 아스키코드 사용
    # 숫자인 경우
    n = ord(c)
    if '0' <= c <= '9':
        return n - ord('0')
    # 문자인 경우
    else:
        return n - ord('A') + 10


def decimal_to_bin(n):
    # 16미만의 자연수가 들어오므로 2진수 4자리로 표현 가능
    binary = [0] * 4
    idx = 3
    # 2로 나눈 나머지를 뒤에서부터 채움
    while n > 0:
        binary[idx] = n % 2
        idx -= 1
        n //= 2
    return binary


T = int(input())
for tc in range(1, T+1):
    N, hex_num = list(input().split())

    tmp = []
    for i in range(int(N)):
        # print(hex_to_decimal(hex_num[i]))
        tmp += map(str, decimal_to_bin(hex_to_decimal(hex_num[i])))
    result = ''.join(tmp)
    print('#{} {}'.format(tc, result))
