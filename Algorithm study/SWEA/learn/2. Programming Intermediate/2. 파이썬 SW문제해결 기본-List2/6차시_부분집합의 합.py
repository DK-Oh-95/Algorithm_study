# 테스트케이스 입력
T = int(input())
# 1부터 12까지의 숫자를 지닌 집합 A
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for tc in range(1, T+1):
    # 원소 개수 N, 합 K 입력
    n, k = map(int, input().split())
    print(n, k)
    # 부분집합의 합이 0인 부분집합이 있으면 1, 없으면 0, 일단 없다고 가정
    result = 0
    # 비트 연산으로 집합 A의 부분집합 수만큼 반복
    for i in range(1<<len(A)):
        # 부분집합의 합을 할당할 변수 생성
        sum_v = 0
        # 몇개의 요소가 더해졌는지 확인할 변수 생성
        cnt = 0
        # i의 각 비트를 확인 (요소의 개수만큼 확인)
        for j in range(len(A)):
            if i & (1<<j):  # i의 j번째 비트는 1인지 확인
                # j번째 요소가 부분집합에 포함된다.
                sum_v += A[j]
                cnt += 1
        # 부분집합의 합이 0인 부분집합이 K이고 N개의 요소만 더했는지 확인
        if sum_v == k and cnt == n:
            # 해당하는 경우가 있다면 결과에 가짓수 하나씩 더함
            result += 1

    print('#{} {}'.format(tc, result))