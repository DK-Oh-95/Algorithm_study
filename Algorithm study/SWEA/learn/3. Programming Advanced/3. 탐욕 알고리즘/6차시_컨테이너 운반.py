T = int(input())
for tc in range(1, T+1):
    # N: 컨테이너 수, M: 트럭 수
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))  # 화물 무게
    ti = list(map(int, input().split()))  # 적재 용량

    # 무게에 따라 정렬
    wi.sort(reverse=True)
    # 적재용량에 따라 정렬
    ti.sort()

    # 무거운 화물부터 실을 수 있으면 적재
    sum_weight = 0
    for i in range(N):
        for j in range(M):
            # 가장 무거운 화물을 실을 수 있는 적재용략이 가작 적은 트럭부터 적재
            if wi[i] <= ti[j]:
                sum_weight += wi[i]
                ti[j] = 0  # 해당 트럭은 더이상 적재 불가
                break

    print('#{} {}'.format(tc, sum_weight))
