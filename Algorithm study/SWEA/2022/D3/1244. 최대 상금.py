def solve(n, c):
    global max_num

    # 교환 횟수를 모두 소진했을 때, 최대값보다 크면 갱신
    if not c:
        if max_num < int(''.join(n)):
            max_num = int(''.join(n))
        return

    # 이미 확인한 숫자면 중단
    if ''.join(n) in num_list:
        return
    num_list.append(''.join(n))

    # 자신 이외의 값과 교환
    for i in range(len(n)):
        for j in range(len(n)):
            if i == j:
                continue
            n[i], n[j] = n[j], n[i]
            solve(n, c-1)
            n[i], n[j] = n[j], n[i]  # 원상복구


for tc in range(int(input())):
    num, change = input().split()

    list_num = list(num)  # 순서 바꿔주기 위한 변수
    num_list = []  # 가능한 경우 기록할 리스트
    max_num = 0
    solve(list_num, int(change))

    print('#{} {}'.format(tc+1, max_num))
