T = int(input())
for tc in range(1, T+1):
    # 화덕 크기 N, 피자 개수 M
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    # 화덕 queue로 생성 후 처음 피자 넣음
    queue = []
    num = 0
    for i in range(N):
        num += 1
        queue.append([pizza.pop(0), num])  # 피자 번호

    # 피자 나오는 순서 변수
    sequence = []

    # 화덕에 남은 피자가 있으면 계속 돌림
    while True:
        # 화덕에 빈공간이 있고, 남은 피자가 있으면 피자 넣음
        for i in range(N):
            if 0 in queue[i] and pizza:
                num += 1
                queue[i] = [pizza.pop(0), num]

        # 치즈가 다 놓은 피자가 나올때까지 치즈 절반씩 녹음
        while True:
            # 치즈가 다 녹은 피자가 나오면 기록하고 중단
            tmp = 0
            for i in range(N):
                # 치즈가 절반씩 녹음
                queue[i][0] = queue[i][0] // 2
                if 0 in queue[i]:
                    tmp = i
                    # 중복을 없애고 나가는 순서대로 피자번호 기록
                    if queue[i][1] not in sequence:
                        sequence.append(queue[i][1])
            if 0 in queue[tmp]:
                break

        # 화덕 안이 비어있으면 전체 반복 중단
        cnt = 0
        for i in range(N):
            if 0 in queue[i]:
                cnt += 1
        if cnt == N:
            break

    print('#{} {}'.format(tc, sequence[-1]))
