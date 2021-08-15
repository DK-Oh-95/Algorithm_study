# Test case 10개
T = 10

# 해당 빌딩이 최고 높이인지 확인하는 함수 생성
def hightest(list):
    if list[i] > list[i-2] and list[i] > list[i-1] and list[i] > list[i+1] and list[i] > list[i+2]:
        return True

# 각각의 Testcase에서 작업 반복
for tc in range(1, T+1):
    # 빌딩 수 N 입력
    N = int(input())
    # 빌딩 높이 리스트 입력
    building_heights = list(map(int, input().split()))

    # 각 테스트케이스에서 조망권 있는 층수 합 계산
    sum_heights = 0
    for i in range(2, N-2):
        # 최고 높이 판정 함수 실행
        if hightest(building_heights):
            # 좌우 빌딩들 중 가장 높은 빌딩과의 차이를 구하기 위해 반복문으로 최대값 구함
            LR_list = [building_heights[i-2], building_heights[i-1], building_heights[i+1], building_heights[i+2]]
            # 4개 빌딩 중 max_height보다 높은 빌딩 값 할당
            max_height = 0
            for building in LR_list:
                if max_height < building:
                    max_height = building
            # 조망권이 있는 층수는 해당 인덱스의 빌딩 높이와 max_height의 차이
            view_layer = building_heights[i]-max_height

            # 조망권 있는 층수들의 총합 계산
            sum_heights += view_layer

    print('#{} {}'.format(tc, sum_heights))