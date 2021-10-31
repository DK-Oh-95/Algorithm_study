def mergesort(arr):
    global cnt
    # 분할된 숫자가 하나일 경우 바로 반환
    if len(arr) == 1:
        return arr

    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    # tmp_l: 왼쪽배열, tmp_r: 오른쪽배열, merge_arr: 두 배열을 병합할 배열
    tmp_l = mergesort(left)
    tmp_r = mergesort(right)
    merge_arr = [0] * (len(tmp_l) + len(tmp_r))

    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수
    if tmp_l[-1] > tmp_r[-1]:
        cnt += 1

    # i: 왼쪽배열 인덱스, j: 오른쪽배열 인덱스, d: 병합될 배열 인덱스
    i = j = d = 0
    while d < len(merge_arr):  # 병합할 정렬 다 채울때까지
        # 왼쪽 배열의 수들 모두 병합했다면 오른쪽 배열값 입력
        if j != len(tmp_r) and i == len(tmp_l):
            merge_arr[d] = tmp_r[j]
            d += 1
            j += 1
        # 오른쪽 배열의 수들 모두 병합했다면 왼쪽 배열값 입력
        elif i != len(tmp_l) and j == len(tmp_r):
            merge_arr[d] = tmp_l[i]
            d += 1
            i += 1
        # 양쪽 배열 값들 각각 순서대로 확인하며 더 작은 값 입력
        elif tmp_l[i] <= tmp_r[j]:
            merge_arr[d] = tmp_l[i]
            d += 1
            i += 1
        elif tmp_l[i] >= tmp_r[j]:
            merge_arr[d] = tmp_r[j]
            d += 1
            j += 1

    # 병합 완료된 배열 반환
    return merge_arr


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    result = mergesort(a)
    print('#{} {} {}'.format(tc, result[N//2], cnt))
