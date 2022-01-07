# 다시풀자
#            0  1  2  3  4  5  6  7  8  9
# 1번 수포자 : 1, 2, 3, 4, 5
# 2번 수포자 : 2, 1, 2, 3, 2, 4, 2, 5
# 3번 수포자 : 3, 3, 1, 1, 2, 2, 4, 4, 5, 5

def solution(answers):
    answer = []

    first = 0
    second = 0
    third = 0
    for i in range(len(answers)):
        # 1번 수포자
        if i % 5 == 0 and answers[i] == 1:
            first += 1
        elif i % 5 == 1 and answers[i] == 2:
            first += 1
        elif i % 5 == 2 and answers[i] == 3:
            first += 1
        elif i % 5 == 3 and answers[i] == 4:
            first += 1
        elif i % 5 == 4 and answers[i] == 5:
            first += 1

        # 2번 수포자
        if i % 2 == 0 and answers[i] == 2:
            second += 1
        elif i % 8 == 1 and answers[i] == 1:
            second += 1
        elif i % 8 == 3 and answers[i] == 3:
            second += 1
        elif i % 8 == 5 and answers[i] == 4:
            second += 1
        elif i % 8 == 7 and answers[i] == 5:
            second += 1

        # 3번 수포자
        if (i // 2) % 5 == 0 and answers[i] == 3:
            third += 1
        elif (i // 2) % 5 == 1 and answers[i] == 1:
            third += 1
        elif (i // 2) % 5 == 2 and answers[i] == 2:
            third += 1
        elif (i // 2) % 5 == 3 and answers[i] == 4:
            third += 1
        elif (i // 2) % 5 == 4 and answers[i] == 5:
            third += 1

    # 1, 2, 3번 정답 개수 비교
    if first > second:
        if first > third:
            answer.append(1)
        elif first == third:
            answer.extend([1, 3])
        else:
            answer.append(3)
    elif first == second:
        if first > third:
            answer.extend([1, 2])
        elif first == third:
            answer.extend([1, 2, 3])
        else:
            answer.append(3)
    else:
        if second > third:
            answer.append(2)
        elif second == third:
            answer.extend([2, 3])
        else:
            answer.append(3)

    return answer


print(solution([1, 2, 3, 4, 5]))
