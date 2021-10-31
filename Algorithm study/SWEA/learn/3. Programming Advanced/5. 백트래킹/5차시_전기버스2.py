def battery_change(charge, cur, cnt):
    """
    :param charge: 잔여 배터리량
    :param cur: 현재 지점
    :param cnt: 배터리 교환 횟수
    """
    global min_cnt
    # 마지막 정류장 도달할 때까지 반복
    if cur == N - 1:
        if min_cnt > cnt:
            min_cnt = cnt
        return

    # 현재 교환 횟수가 이미 최소 횟수를 넘으면 중단
    if min_cnt < cnt:
        return

    # 배터리 한 칸 사용해서 한 정거장 이동
    charge -= 1
    cur += 1

    # 배터리 잔여량으론 도달할 수 없고, 교체 시 마지막 정류장 갈 수 있으면 교체
    if cur + charge < N-1 and cur + battery[cur] >= N - 1:
        cnt += 1
        if min_cnt > cnt:
            min_cnt = cnt
        return

    # 배터리 다 쓰면 교체
    if charge == 0:
        charge = battery[cur]
        cnt += 1

    # 교체하지 않는 경우
    battery_change(charge, cur, cnt)
    # 교체하는 경우
    charge = battery[cur]
    cnt += 1
    battery_change(charge, cur, cnt)
    return


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    battery = arr[1:]

    min_cnt = 99  # 최소 교체 횟수
    battery_change(battery[0], 0, 0)

    print('#{} {}'.format(tc, min_cnt))
