import sys
sys.stdin = open("input (1).txt", "r")


def code_num(r, c):
    result = []
    # 숫자 8개 생성
    for d in range(8):
        pattern = []
        # 7자리 코드를 숫자로 변환
        for k in range(c - (7*d), c - (7*d) - 7, -1):
            pattern.append(codes[r][k])
        result.insert(0, patterns[''.join(pattern)])
    return result


def decode(code):
    # 7자리 암호를 홀수번쨰합*3, 짝수번째합이 10의 배수인지 판별
    odd = 0
    even = 0
    for m in range(8):
        # 홀수
        if m+1 & 1:
            odd += code[m]
        # 짝수(검증코드 포함)
        else:
            even += code[m]
    if not (odd * 3 + even) % 10:
        return odd + even
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    codes = [input() for _ in range(N)]

    # 뒤에서부터 수를 참조
    patterns = {
        '1011000': 0,
        '1001100': 1,
        '1100100': 2,
        '1011110': 3,
        '1100010': 4,
        '1000110': 5,
        '1111010': 6,
        '1101110': 7,
        '1110110': 8,
        '1101000': 9,
    }
    password = []
    ans = 0
    for i in range(N):
        if '1' in codes[i]:
            for j in range(M-1, -1, -1):
                if codes[i][j] == '1':
                    password = code_num(i, j)
                    ans = decode(password)
                    break
            if password:
                break

    print('#{} {}'.format(tc, ans))
