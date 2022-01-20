def solution(id_list, report, k):
    n = len(id_list)
    answer = [0] * n

    cnt_list = [[] for _ in range(n)]

    for i in range(len(report)):
        reporter, reported = report[i].split()
        for j in range(n):
            if reported == id_list[j] and reporter not in cnt_list[j]:
                cnt_list[j].append(reporter)
                break

    for i in range(n):
        if len(cnt_list[i]) >= k:
            for j in range(len(cnt_list[i])):
                for k in range(n):
                    if cnt_list[i][j] == id_list[k]:
                        answer[k] += 1
                        break

    return answer


# print(solution(["muzi", "frodo", "apeach", "neo"], 	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
