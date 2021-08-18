# 테스트케이스
T = int(input())

for tc in range(1, T + 1):
    # 삼각형 크기 N
    N = int(input())

    # 삼각형을 만들 배열
    arr = [[1]]
    for i in range(1, N):   # 첫 번째 행은 1로 고정이므로 2번째 행부터 생성
        sub_arr = []    # 전체 배열에 더할 각 행 배열
        for j in range(i+1):
            if j == 0 or j == i:  # 양 끝은 1
                sub_arr += [1]
            else:   # 양 끝이 아니면 이전 행의 이전열과 같은 열 합
                sub_arr += [arr[i-1][j-1] + arr[i-1][j]]
        # 각 행을 전체 배열에 추가
        arr += [sub_arr]

    print('#{}'.format(tc))
    for i in range(N):
        # 전체 배열의 각 행을 문자열로 바꿔 join 함수를 사용해 띄어쓰기를 포함해 출력
        print(' '.join(map(str, (arr[i]))))
