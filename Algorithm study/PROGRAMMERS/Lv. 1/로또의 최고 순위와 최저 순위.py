# 1등: 6개 / 2등: 5개 / 3등: 4개
# 4등: 3개 / 5등: 2개 / 6등: 1개 이하

def solution(lottos, win_nums):
    answer = []

    rank = [6, 6, 5, 4, 3, 2, 1]

    # lottos에 있는 숫자들 중 win_nums에 있는 개수 확인
    cnt = 0
    cnt_zero = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt += 1
        # lottos에 있는 0 개수 확인
        if lottos[i] == 0:
            cnt_zero += 1

    answer.extend([rank[cnt_zero + cnt], rank[cnt]])

    return answer
