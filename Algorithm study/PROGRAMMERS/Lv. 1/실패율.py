def solution(N, stages):
    answer = []
    tmp_list = []
    tmp_num = 0
    n = len(stages)
    for i in range(1, N+1):
        a = stages.count(i)
        tmp_list.append(a/(n-tmp_num))
        tmp_num += a
    tmp_list2 = sorted(tmp_list)
    tmp_list2.reverse()
    used = [0] * N

    for i in range(N):
        for j in range(N):
            if not used[j] and tmp_list2[i] == tmp_list[j]:
                used[j] = 1
                answer.append(j+1)

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
