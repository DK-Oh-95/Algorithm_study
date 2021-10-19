def palindrome(n, m, arr):
    for i in range(n):
        # row 우선 순회로 회문 있는지 검사
        for j in range(n-m+1):
            word_r = ''
            reverse_word_r = ''
            # (i, j) 위치부터 길이 m만큼 문자열을 정방향과 역방향으로 생성 후 비교
            for d in range(j, m+j):
                word_r += arr[i][d]
            for d in reversed(range(j, m+j)):
                reverse_word_r += arr[i][d]
            if word_r == reverse_word_r:
                return word_r

        # row를 참조해서 회문을 찾지 못하면 column으로 재검사
        for j in range(n-m+1):
            word_c = ''
            reverse_word_c = ''
            # (j, i) 위치부터 길이 m만큼 문자열을 정방향과 역방향으로 생성 후 비교
            for d in range(j, m+j):
                word_c += arr[d][i]
            for d in reversed(range(j, m+j)):
                reverse_word_c += arr[d][i]
            if word_c == reverse_word_c:
                return word_c


# 테스트케이스
T = int(input())

for tc in range(1, T+1):
    # 글자판 크기 N, 문자열 길이 M
    N, M = map(int, input().split())
    # 글자판 입력
    words = [input() for _ in range(N)]

    print('#{} {}'.format(tc, palindrome(N, M, words)))
