def solution(n, lost, reserve):
    student = [1] * n
    for i in range(len(lost)):
        student[lost[i] - 1] -= 1
    for i in range(len(reserve)):
        student[reserve[i] - 1] += 1
    for i in range(n):
        if not student[i]:
            if i != 0 and student[i-1] == 2:
                student[i] += 1
                student[i - 1] -= 1
            elif i != n-1 and student[i+1] == 2:
                student[i] += 1
                student[i + 1] -= 1
    return student.count(1) + student.count(2)


print(solution(5, [2, 4], [1, 3, 5]))
