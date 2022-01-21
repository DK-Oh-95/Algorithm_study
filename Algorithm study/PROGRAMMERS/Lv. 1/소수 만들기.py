def solution(nums):
    answer = 0
    n = len(nums)
    used = [0] * n
    power_set(used)


    return answer

def power_set(arr):
    global answer

    if sum(arr) == 3:
        for i in range(len(arr)):

            nums[i]
        return

    for i in range(n):
        arr[i] = 1
        power_set(arr)
        arr[i] = 0
