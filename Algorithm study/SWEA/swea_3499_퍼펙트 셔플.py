T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(input().split())

    front = []
    back = []
    result = []

    for i in range((N+1)//2):
        front.append(cards[i])
    for i in range((N+1)//2, N):
        back.append(cards[i])

    while front or back:
        if front:
            result.append(front.pop(0))
        if back:
            result.append(back.pop(0))

    print('#{}'.format(tc), *result)