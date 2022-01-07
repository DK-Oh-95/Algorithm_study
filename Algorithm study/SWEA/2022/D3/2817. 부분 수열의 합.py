def powerset(idx):
    global total
    # 중단 조건
    result = 0
    if idx == N:
        for i in range(N):
            if used[i]:
                result += nums[i]
            if result > K:
                return
        if result == K:
            total += 1
        return

    # 예외처리
    for i in range(N):
        if used[i]:
            result += nums[i]
        if result > K:
            return

    # 인덱스 사용하는 경우
    used[idx] = 1
    powerset(idx + 1)

    # 인덱스 사용하지 않는 경우
    used[idx] = 0
    powerset(idx + 1)


for tc in range(int(input())):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))

    used = [0] * N
    total = 0
    powerset(0)

    print('#{} {}'.format(tc+1, total))
