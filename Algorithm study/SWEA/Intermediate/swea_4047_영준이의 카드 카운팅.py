def count_card(arr):
    n = len(arr)

    # 같은 카드 있으면 오류
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                return ['ERROR']

    # 오류가 없다면 각 종류별 카드 수를 새고 13에서 뺀다
    cnt_s = 0
    cnt_d = 0
    cnt_h = 0
    cnt_c = 0
    result = []
    for i in range(n):
        if arr[i][0] == 'S':
            cnt_s += 1
        if arr[i][0] == 'D':
            cnt_d += 1
        if arr[i][0] == 'H':
            cnt_h += 1
        if arr[i][0] == 'C':
            cnt_c += 1
    result.append(13 - cnt_s)
    result.append(13 - cnt_d)
    result.append(13 - cnt_h)
    result.append(13 - cnt_c)

    return result


T = int(input())
for tc in range(1, T+1):
    # 카드 무늬 (S, D, H, C)
    S = input()

    cards = []
    for r in range(0, len(S), 3):
        tmp = ''
        for c in range(r, r+3):
            tmp += S[c]
        cards.append(tmp)

    print('#{}'.format(tc), *count_card(cards))
