def quick_sort(arr, start, end):
    if start >= end:
        return
    # 피벗 설정
    pivot = arr[start]

    # 큰값과 작은값을 찾기위한 인덱스 i, j 정의
    i = start + 1
    j = end
    while i <= j:
        # 리스트 왼쪽에 피벗보다 작은 값만 두기 위해
        # 피벗보다 큰 값 찾을 때까지 조회
        while i <= j and arr[i] <= pivot:
            i += 1
        # 리스트 오른쪽에 피벗보다 큰 값만 두기 위해
        # 피벗보다 작은 값 찾을 때까지 조회
        while i <= j and arr[j] >= pivot:
            j -= 1
        # 피벗보다 작은 값이 피벗보다 큰 값보다 오른쪽에 있다면 위치 교환
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # 설정한 피벗과, 피벗보다 작은 값중에 마지막을 가리키는 j 인덱스 값과 교체
    arr[start], arr[j] = arr[j], arr[start]

    # 분할된 부분에 대한 재귀호출
    quick_sort(arr, start, j - 1)
    quick_sort(arr, j + 1, end)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    quick_sort(a, 0, N-1)
    print('#{} {}'.format(tc, a[N//2]))
