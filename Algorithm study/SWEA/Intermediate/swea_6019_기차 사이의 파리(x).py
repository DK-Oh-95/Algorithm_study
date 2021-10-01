###### 도저히 모르겠다

# 테스트케이스
T = int(input())

for tc in range(1, T + 1):
    # 거리, A 속력, B 속력, 파리 속력 입력
    length, A, B, fly = list(map(int, input().split()))

    # 각 요소의 처음 위치 변수
    location_a = 0
    location_b = length
    location_fly = 0

    # 파리가 이동한 거리 변수
    distance_fly = 0

    while location_a + (A + B) < location_b:
        while location_fly + (B + fly) <= location_b:
            location_a += A
            location_b -= B
            location_fly += fly
            distance_fly += fly

        while location_fly - (A + fly) >= location_a:
            location_a += A
            location_b -= B
            location_fly -= fly
            distance_fly += fly

    print('#{} {:.10f}'.format(tc, distance_fly + fly))