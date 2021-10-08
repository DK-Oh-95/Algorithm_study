def change_decimal(num, notation):
    n = len(num)
    tmp = 0
    for d in range(n):
        if num[n - d - 1] != 0:
            tmp += num[n - d - 1] * (notation ** d)
    return tmp


T = int(input())
for tc in range(1, T+1):
    binary = list(map(int, input()))
    trinary = list(map(int, input()))
    b_list = []  # 2진수 변환으로 가능한 경우
    t_list = []  # 3진수 변환으로 가능한 경우

    # 2진수에서 한 자리씩 바꾸면서 가능한 경우 확인
    for i in range(len(binary)):
        binary[i] ^= 1  # 한자리씩 토글
        b_list.append(change_decimal(binary, 2))
        binary[i] ^= 1  # 초기화

    # 3진수에서 한 자리씩 바꾸면서 가능한 경우 확인
    for i in range(len(trinary)):
        for _ in range(2):
            trinary[i] = (trinary[i] + 1) % 3
            t_list.append(change_decimal(trinary, 3))
        trinary[i] = (trinary[i] + 1) % 3  # 초기화

    # 생성한 2진수 경우와 3진수 경우 중 겹치는 값 확인
    result = 0
    for i in range(len(b_list)):
        if b_list[i] in t_list:
            result = b_list[i]

    print('#{} {}'.format(tc, result))
