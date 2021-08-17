# 테스트케이스
T = int(input())

def bruteforce(str1, str2):
    # 전체 텍스트의 인덱스
    i = 0
    # 찾을 패턴의 인덱스
    j = 0

    cnt = 0
    # 전체 텍스트 인덱스 끝까지 반복
    while i < len(str1) and j < len(str2):
        # 해당 인덱스의 글자가 다르면 i는 처음 비교한 j인덱스 다음으로 옮기고 j는 0으로 되돌림
        if str1[i] != str2[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1

        if j == len(str2):
            cnt += 1
            j = 0
    
    # 가장 적은 타이핑수는 str2가 str1에 포함된 곳들을 한글자로 생각하면 된다
    return len(str1) - cnt * (len(str2) - 1)

for tc in range(1, T+1):
    A, B = input().split()

    print('#{} {}'.format(tc, bruteforce(A, B)))