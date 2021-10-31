def lr_count(num):
    # 찾는 숫자가 N 리스트에 없으면 0 리턴
    if num not in arr_n:
        return 0
    # 찾는 숫자 있으면 조건에 만족 안하는지 확인
    else:
        s = 0  # 시작 인덱스
        e = len(arr_n) - 1  # 종료 인덱스

        tmp = ''  # 찾는 값이 전에 왼쪽이었는지 오른쪽이었는지 기록
        while 1:
            m = (s + e) // 2  # 중간 인덱스
            # 조건에 이상없이 찾는 값 조회하면 1 리턴
            if num == arr_n[m]:
                return 1
            # 찾는 값이 m보다 작은데 이전에도 왼쪽이었으면 0 리턴
            elif num < arr_n[m]:
                if tmp == 'L':
                    return 0
                e = m - 1
                tmp = 'L'
            # 찾는 값이 m보다 큰데 이전에도 오른쪽이었으면 0 리턴
            elif num > arr_n[m]:
                if tmp == 'R':
                    return 0
                s = m + 1
                tmp = 'R'


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr_n = sorted(list(map(int, input().split())))
    arr_m = list(map(int, input().split()))

    result = 0
    for i in range(M):
        result += lr_count(arr_m[i])

    print('#{} {}'.format(tc, result))
