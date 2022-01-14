def solution(numbers):
    answer = 0
    for d in range(1, 10):
        if d not in numbers:
            answer += d

    return answer


print(solution([1,2,3,4,6,7,8,0]))