# 테스트케이스 입력
T = int(input())

for tc in range(1, T+1):
    # 정수 개수 n, 정수들 입력
    n = int(input())
    arr = list(map(int, input().split()))

    # 리스트 전체를 순회하면서 매번 가장 큰 값을 짝수 인덱스에, 가장 작은 값을 홀수 인덱스에 할당
    for i in range(n):
        # 인덱스가 짝수일 땐 큰 값 할당
        if not i % 2:
            for j in range(i, n):   # 앞자리부터 채워놓기 때문에 채워진 인덱스들은 조회할 필요 없다
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

        # 인덱스가 홀수일 땐 작은 값 할당
        if i % 2:
            for j in range(i, n):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

    print('#{}'.format(tc), end=' ')
    # 완성된 리스트에서 10번째까지만 출력하기 위해 반복문으로 하나씩 출력
    for i in range(9):
        print('{}'.format(arr[i]), end=' ')
    print(arr[9])