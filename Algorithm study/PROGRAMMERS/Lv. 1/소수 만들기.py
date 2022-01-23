def solution(nums):
    global answer

    used = [0] * len(nums)
    power_set(used, nums)

    return answer/6


def power_set(arr, arr_nums):
    global answer

    if sum(arr) == 3:
        tmp = 0
        for i in range(len(arr)):
            if arr[i]:
                tmp += arr_nums[i]

        for i in range(2, tmp):
            if tmp % i == 0:
                break
        else:
            print(tmp)
            answer += 1

    for i in range(len(arr)):
        if not arr[i]:
            arr[i] = 1
            power_set(arr, arr_nums)
            arr[i] = 0


answer = 0

print(solution([1,2,3,4]))