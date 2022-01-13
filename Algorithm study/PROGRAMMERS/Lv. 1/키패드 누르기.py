def solution(numbers, hand):
    answer = ''

    l_position = [3, 0]
    r_position = [3, 2]

    for i in range(len(numbers)):
        if numbers[i] in [1, 4, 7]:
            answer += 'L'
            if numbers[i] == 1:
                l_position = [0, 0]
            elif numbers[i] == 4:
                l_position = [1, 0]
            elif numbers[i] == 7:
                l_position = [2, 0]
        elif numbers[i] in [3, 6, 9]:
            answer += 'R'
            if numbers[i] == 3:
                r_position = [0, 2]
            elif numbers[i] == 6:
                r_position = [1, 2]
            elif numbers[i] == 9:
                r_position = [2, 2]
        else:
            if numbers[i] == 2:
                if length(0, 1, l_position[0], l_position[1], r_position[0], r_position[1], hand) == 'L':
                    l_position = [0, 1]
                    answer += 'L'
                else:
                    r_position = [0, 1]
                    answer += 'R'
            elif numbers[i] == 5:
                if length(1, 1, l_position[0], l_position[1], r_position[0], r_position[1], hand) == 'L':
                    l_position = [1, 1]
                    answer += 'L'
                else:
                    r_position = [1, 1]
                    answer += 'R'
            elif numbers[i] == 8:
                if length(2, 1, l_position[0], l_position[1], r_position[0], r_position[1], hand) == 'L':
                    l_position = [2, 1]
                    answer += 'L'
                else:
                    r_position = [2, 1]
                    answer += 'R'
            elif numbers[i] == 0:
                if length(3, 1, l_position[0], l_position[1], r_position[0], r_position[1], hand) == 'L':
                    l_position = [3, 1]
                    answer += 'L'
                else:
                    r_position = [3, 1]
                    answer += 'R'
    return answer


def length(r, c, lr, lc, rr, rc, h):
    if abs(r - lr) + abs(c - lc) < abs(r - rr) + abs(c - rc):
        return 'L'
    elif abs(r - lr) + abs(c - lc) > abs(r - rr) + abs(c - rc):
        return 'R'
    else:
        if h == 'left':
            return 'L'
        else:
            return 'R'


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
