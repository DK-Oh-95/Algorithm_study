import sys
sys.stdin = open("sample_input.txt", "r")


def passcode(r, c):
    result = []
    # 비율을 구하고 그것을 토대로 8자리 암호 생성
    idx = c
    for k in range(8):
        # 각 코드들의 너비를 저장할 변수들
        w1 = w2 = w3 = w4 = 0
        while bin_codes[r][idx] == '1':
            w4 += 1
            idx -= 1
        while bin_codes[r][idx] == '0':
            w3 += 1
            idx -= 1
        while bin_codes[r][idx] == '1':
            w2 += 1
            idx -= 1
        # 비율
        min_w = min(w2, w3, w4)
        result.insert(0, patterns[(w2/min_w, w3/min_w, w4/min_w)])
        idx = c - (7 * (k+1) * min_w)

    # 같은 줄에 암호 시작이 또 있는 경우
    tmp = 0
    for k in range(idx, 0, -1):
        if bin_codes[r][k] == '1' and bin_codes[r-1][k] == '0':
            tmp = passcode(r, k)
            break

    # 홀수*3 + 짝수가 10의 배수인지 확인
    odd = 0
    even = 0
    for m in range(8):
        # 홀수
        if (m + 1) % 2:
            odd += result[m]
        # 짝수(검증코드 포함)
        else:
            even += result[m]
    if not (odd * 3 + even) % 10:
        return tmp + odd + even
    else:
        return tmp + 0


patterns = {
    # 1  0  1
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}

hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    codes = [list(input()) for _ in range(N)]

    # 배열을 순회하며 16진수 > 2진수로 변환
    for i in range(1, N):
        for j in range(1, M):
            codes[i-1][j] = hex_to_bin[codes[i-1][j]]
    bin_codes = []
    for i in range(N):
        bin_codes.append(''.join(codes[i]))

    # 배열을 뒤에서부터 참조하며 값이 1이고 위가 0인 인덱스 확인
    # 암호코드 판독
    ans = 0
    len_bin = len(bin_codes[0]) -1
    for i in range(1, N):
        if '1' in bin_codes[i]:
            for j in range(len_bin, 0, -1):
                if bin_codes[i][j] == '1' and bin_codes[i-1][j] == '0':
                    ans += passcode(i, j)
                    break

    print('#{} {}'.format(tc, ans))
