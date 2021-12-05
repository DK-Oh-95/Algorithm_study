# 순열, 모든 자리수와 교환하여 나올 수 있는 경우의 수 출력
def perm(cnt):  # idx: 위치 교환을 시작할 인덱스, cnt: 교환 횟수
    global max_benefit

    # 교환 가능 횟수 소진
    if not cnt:
        tmp = int(''.join(numbers))
        if max_benefit < tmp:
            max_benefit = tmp
        return

    # 본인과 바꾸는 것 포함, 뒤의 요소랑 자리 변환
    for i in range(N):
        for j in range(i+1, N):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            # 상금 목록에 없다면 추가하고 다음 인덱스 작업
            if (''.join(numbers), cnt) not in benefit_list:
                benefit_list.append((''.join(numbers), cnt))
                perm(cnt-1)  # 카운트 줄여서 자리 변환
            numbers[i], numbers[j] = numbers[j], numbers[i]  # 원상복구


T = int(input())
for tc in range(1, T+1):
    numbers, count = input().split()
    numbers = list(numbers)
    count = int(count)

    N = len(numbers)
    max_benefit = 0  # 최대 상금
    benefit_list = []  # 가능한 상금 목록
    perm(count)

    print('#{} {}'.format(tc, max_benefit))
