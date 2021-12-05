# 테스트케이스
T = int(input())

for tc in range(1, T+1):
    # 문자열 5개 입력
    N = 5
    strings = [input() for _ in range(N)]

    # 세로 문자열 담을 변수
    col_str = ''

    # 반복 횟수를 확인하기 위해 가장 긴 문자열 확인
    max_len = 0
    for i in range(N):
        if max_len < len(strings[i]):
            max_len = len(strings[i])

    # 각 행의 같은 열을 참조
    for i in range(max_len):    # 가장 긴 문자열 길이만큼 반복
        for j in range(N):  # 문자열은 5개
            # 문자열 길이가 짧은 행은  추가하지 않고 넘어감
            if len(strings[j]) <= i:    # j번째 행의 길이가 찾는 인덱스보다 작다
                continue
            col_str += strings[j][i]

    print('#{} {}'.format(tc, col_str))