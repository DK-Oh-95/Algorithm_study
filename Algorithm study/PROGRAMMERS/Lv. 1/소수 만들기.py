def solution(nums):
    answer = 0
    n = len(nums)
    used = [0] * n
    power_set(used, nums)


    return answer


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
            answer += 1

        return

    for i in range(len(arr)):
        if not arr[i]:
            arr[i] = 1
            power_set(arr)
            arr[i] = 0
