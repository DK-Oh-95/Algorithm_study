def calc(pay, month):
    global min_pay
    if month > 11:
        if min_pay > pay:
            min_pay = pay
        return

    if fees[0] * plans[month] < fees[1]:
        # 1일
        calc(pay + (fees[0] * plans[month]), month + 1)
    else:
        # 1달
        calc(pay + fees[1], month + 1)
    # 3달
    calc(pay + fees[2], month + 3)


T = int(input())
for tc in range(1, T+1):
    # 1일, 1달, 3달, 1년
    fees = list(map(int, input().split()))
    plans = list(map(int, input().split()))

    min_pay = fees[3]
    calc(0, 0)

    print('#{} {}'.format(tc, min_pay))
