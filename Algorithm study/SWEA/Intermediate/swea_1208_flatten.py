# 총 테스트케이스는 10개
T = 10

for tc in range(1, T+1):
    # 각 테스트케이스의 덤프 횟수
    D = int(input())
    # 박스들의 높이
    boxes = list(map(int, input().split()))

    for _ in range(D):
        # 최고, 최저 높이의 박스 값 확인을 위해 변수 설정
        highest_box = 0
        lowest_box = 101
        # boxes 리스트를 순회하며 최대값 최소값 할당
        for i in range(len(boxes)):
            # i번째 인덱스의 리스트 값이 현재 최고값보다 크면 할당
            if boxes[i] >= highest_box:
                highest_box = boxes[i]
                highest_point = i   # 가장 높을 때 인덱스
            # i번째 인덱스의 리스트 값이 현재 최저값보다 작으면 할당
            if boxes[i] <= lowest_box:
                lowest_box = boxes[i]
                lowest_point = i    # 가장 낮을 때 인덱스
        # 최고 박스와 최저 박스 높이 차가 1보다 크면 평탄화 시행
        if highest_box - lowest_box > 1:
            boxes[highest_point] -= 1
            boxes[lowest_point] += 1

    # 작업이 완료된 후 마지막 최고, 최저점 값 다시 확인후 차이 계산
    for i in range(len(boxes)):
        if boxes[i] >= highest_box:
            highest_point = i
        if boxes[i] <= lowest_box:
            lowest_point = i

    difference_box = boxes[highest_point] - boxes[lowest_point]
    print('#{} {}'.format(tc, difference_box))