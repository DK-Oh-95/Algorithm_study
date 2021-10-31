def babygin(arr):
    # 카운트 배열을 입력받아 베이비진인지 판단하는 함수
    for d in range(8):
        # triplet
        if arr[d] >= 3:
            return 1
        # run
        if arr[d] >= 1 and arr[d+1] >= 1 and arr[d+2] >= 1:
            return 1


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))

    # 1 ~ 9까지 카드 개수를 셀 리스트
    p1 = [0] * 10
    p2 = [0] * 10

    ans = 0
    for i in range(12):
        # 플레이어 1에게 할당되는 카드
        if not i % 2:
            # 해당하는 숫자를 카운트
            p1[cards[i]] += 1
        # 플레이어 2에게 할당되는 카드
        else:
            p2[cards[i]] += 1

        if i > 2:  # 숫자가 3개 이상 들어감
            if babygin(p1):
                ans = 1
                break
            if babygin(p2):
                ans = 2
                break

    print('#{} {}'.format(tc, ans))
