def choose_ingredients():
    global min_difference, cuisine_1, cuisine_2

    if len(ingredient) == N // 2:
        # 재료 조합 중 절반의 경우(0번 인덱스 0이면 모든 경우의 절반)
        if ingredient[0] == 0:
            # 생성한 재료 조합으로 요리 생성
            make_food(ingredient, 1)

            # 생성한 조합의 반대 재료 조합 생성 후 요리 생성
            complement_ingredient = []
            for m in range(N):
                if m not in ingredient:
                    complement_ingredient.append(m)
            make_food(complement_ingredient, 2)

            # 각 경우 만든 요리의 맛 차이를 확인
            if min_difference > abs(cuisine_1 - cuisine_2):
                min_difference = abs(cuisine_1 - cuisine_2)
            cuisine_1, cuisine_2 = 0, 0  # 초기화
        return

    # 0 ~ N까지 숫자 중 중복 없이 오름차순으로 가능한 경우 생성
    for d in range(N):
        if d not in ingredient:
            if ingredient and ingredient[-1] > d:
                continue
            ingredient.append(d)
            choose_ingredients()
            ingredient.pop()


def make_food(arr, num):  # num : 원래 재료조합인지 반대 조합인지 구분 용도
    global cuisine_1, cuisine_2

    if len(food) == 2 and num == 1:
        cuisine_1 += S[food[0]][food[1]]
        return
    elif len(food) == 2 and num == 2:
        cuisine_2 += S[food[0]][food[1]]
        return

    # 재료들을 가지고 2개씩 묶어서 만들 수 있는 요리 조합 생성
    for k in range(N//2):
        if arr[k] not in food:
            food.append(arr[k])
            make_food(arr, num)
            food.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    ingredient = []  # 식재료 고르는 모든 경우
    food = []  # 선택한 식재료 중 2개씩 만들 수 있는 시너지
    cuisine_1 = 0  # 조합한 요리 1
    cuisine_2 = 0  # 조합한 요리 2
    min_difference = 40000
    choose_ingredients()

    print('#{} {}'.format(tc, min_difference))
