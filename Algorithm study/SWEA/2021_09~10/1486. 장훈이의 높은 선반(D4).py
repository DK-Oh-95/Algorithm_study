def tower(idx, sub_height):
    global height

    # 탑을 쌓는 도중 현재 높이보다 높아지면 중단
    if height < sub_height:
        return
    # 선반 높이보다 높아지면 값 저장하고 중단
    if B <= sub_height:
        height = sub_height
        return
    # 마지막 인덱스까지 조회했으면 반환
    if idx == N:
        return

    # 해당 인덱스 값 사용
    tower(idx + 1, sub_height + Hi[idx])
    # 해당 인덱스 값 미사용
    tower(idx + 1, sub_height)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    Hi = list(map(int, input().split()))

    height = 200000
    used = [0] * len(Hi)
    tower(0, 0)

    print('#{} {}'.format(tc, height - B))
