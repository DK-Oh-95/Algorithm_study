def solution(nums):
    tmp = set(nums)
    if len(nums)/2 > len(tmp):
        return len(tmp)
    else:
        return len(nums)/2


print(solution([3,3,3,2,2,2]))
