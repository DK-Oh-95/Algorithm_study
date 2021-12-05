# 테스트케이스는 10개로 지정
for _ in range(10):
    tc = int(input())   # 테스트케이스 입력
    # 100개의 값을 입력받아 리스트로 만드는 작업 100번 반복
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 합들을 비교해 최종 출력할 변수 생성
    max_sum = 0

    # row 우선 순회
    max_row_sum = 0 # 각 행의 합의 최대값을 할당하기 위한 변수
    for r in range(len(arr)):
        arr_sum = 0 # 각 행의 합을 기억할 변수
        for c in range(len(arr[r])):
            arr_sum += arr[r][c]
        # 각 행의 합을 구하고 현재 저장된 최대값과 비교
        if arr_sum > max_row_sum:
            max_row_sum = arr_sum

    # column 우선 순회
    max_column_sum = 0
    for c in range(len(arr[0])):
        arr_sum = 0
        for r in range(len(arr)):
            arr_sum += arr[r][c]
        if arr_sum > max_column_sum:
            max_column_sum = arr_sum

    # 대각선 합 계산
    # 오른쪽 아래로 향하는 대각선 변수
    arr_sum1 = 0
    # 왼쪽 위로 향하는 대각선 변수
    arr_sum2 = 0
    for r in range(len(arr)):
        for c in range(len(arr)):
            if r == c:  #행, 열의 인덱스가 같을 때 값 더하기
                arr_sum1 += arr[r][c]
            if r+c == len(arr)-1:   #행, 열의 인덱스의 합이 N-1일 때 값 더하기
                arr_sum2 += arr[r][c]

    # 행 우선, 열 우선 대각선 2개 중 최대인 값 할당
    sum_list = [max_row_sum, max_column_sum, arr_sum1, arr_sum2]
    for i in range(4):
        if max_sum < sum_list[i]:
            max_sum = sum_list[i]

    print('#{} {}'.format(tc, max_sum))