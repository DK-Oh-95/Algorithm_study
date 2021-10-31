def load(idx, cnt):
    global max_cnt

    # 마지막 인덱스 도달하면 화물 수 비교
    if idx + 1 == N:
        if max_cnt < cnt:
            max_cnt = cnt
        return

    # 다음 작업 가능한 시간 있으면 수행하고 없다면 return
    for d in range(idx + 1, N):
        if time[idx][1] <= time[d][0]:
            load(d, cnt + 1)
    # 더 이상 사용 가능한 도크가 없을 때 작업한 화물수와 최대 작업 수 비교
    if max_cnt < cnt:
        max_cnt = cnt
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]

    s = [0] * N  # 시작시각
    e = [0] * N  # 종료시각

    # 시작시각의 오름차순으로 정렬
    for i in range(N-1):
        min_idx = i
        for j in range(i, N):
            if time[min_idx][0] > time[j][0]:
                min_idx = j
        time[i], time[min_idx] = time[min_idx], time[i]

    max_cnt = 0
    for i in range(N):
        load(i, 1)

    print('#{} {}'.format(tc, max_cnt))
