# 테스트케이스
T = int(input())

for tc in range(1, T+1):
    # N, Q 입력
    NQ = list(map(int, input().split()))
    N = NQ[0]
    Q = NQ[1]

    # 처음 상자들은 N개의 0
    boxes = [0] * N

    # Q회만큼 i 묶음으로 수 바꾸기
    for i in range(1, Q+1):
        # L, R 입력
        LR = list(map(int, input().split()))
        L = LR[0]
        R = LR[1]
        # L부터 R까지 인덱스에 i 입력
        for j in range(L-1, R):
            boxes[j] = i

    print('#{}'.format(tc),end=' ')
    # boxes 각 인자 출력
    for i in range(len(boxes)-1):
        print('{}'.format(boxes[i]),end=' ')
    print('{}'.format(boxes[-1]))