def money_cnt(n):
    for d in range(8):
        if n >= money_list[d]:
            tmp = n // money_list[d]
            money_cnt_list[d] += tmp
            n -= tmp * money_list[d]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money_cnt_list = [0] * 8

    money_cnt(N)
    print('#{}\n{}'.format(tc, ' '.join(map(str, money_cnt_list))))
