# 테스트케이스
T = int(input())

# 고지식한 패턴 검색 알고리즘 사용
def bruteforce(str1, str2):
    # 전체 텍스트의 인덱스
    i = 0
    # 찾을 패턴의 인덱스
    j = 0

    # 전체 텍스트 인덱스 끝까지 반복
    while i < len(str2) and j < len(str1):
        # 해당 인덱스의 글자가 다르면 i는 처음 비교한 j인덱스 다음으로 옮기고 j는 0으로 되돌림
        if str2[i] != str1[j]:
            i = i - j
            j = -1
        i += 1
        j += 1

    if j == len(str1):
        return 1
    else:
        return 0


for tc in range(1, T+1):
    # 문자열 1, 2 입력
    str1 = input()
    str2 = input()

    print('#{} {}'.format(tc, bruteforce(str1, str2)))