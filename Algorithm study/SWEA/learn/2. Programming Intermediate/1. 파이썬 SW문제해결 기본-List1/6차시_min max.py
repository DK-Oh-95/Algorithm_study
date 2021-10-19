# 테스트케이스 T 입력
T = int(input())
# 각각의 테스트케이스에서 숫자 개수와 숫자 리스트를 입력 받음
for tc in range(1, T+1):
    # 양수의 개수 N 입력
    N = int(input())
    # 숫자들 입력
    aj = list(map(int, input().split()))

    # 최대값, 최소값 변수에 리스트 첫번째 자리 수를 할당해 반복문으로 비교
    max_value = aj[0]
    min_value = aj[0]

    # 입력 받은 숫자 리스트의 인덱스를 참조해 최대, 최소값 구분
    for i in range(1, N):   # 첫번째 자리는 같은 값이므로 작업량 줄이기 위해 인덱스 1번부터 비교
        if aj[i] > max_value:
            max_value = aj[i]
        elif aj[i] < min_value:
            min_value = aj[i]
    # 최대, 최소값 차이 계산
    difference_value = max_value - min_value
    print('#{} {}'.format(tc, difference_value))