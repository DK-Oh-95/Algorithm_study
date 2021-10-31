T = int(input())
for tc in range(1, T+1):
    N = float(input())

    n = 1
    binary_idx = []
    result = ''
    while N:
        # 1/2의 n승 보다 크면 인덱스 값 저장
        if N >= (1/2)**n:
            N -= (1/2)**n
            binary_idx.append(n)
        n += 1
        # 소수점 이하 13자리가 되면 중단
        if n == 13:
            result = 'overflow'
            break

    # 오버플로우면 그대로 진행
    if result:
        pass
    else:
        result = []
        i = 1
        # 해당하는 인덱스가 있으면 1추가, 없으면 0추가
        while binary_idx:
            if i in binary_idx:
                result.append('1')
                binary_idx.pop(0)
            else:
                result.append('0')
            i += 1
        result = ''.join(result)
    print('#{} {}'.format(tc, result))
