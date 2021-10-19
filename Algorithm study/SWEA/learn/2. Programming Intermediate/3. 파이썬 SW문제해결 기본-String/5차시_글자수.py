# 테스트케이스
T = int(input())

for tc in range(1, T+1):
    # 문자열 1, 2 입력
    str1 = list(set(input()))   # 중복 제거
    str2 = input()

    max_cnt = 0
    max_str = ''
    # str1의 각 글자를 str2의 각 글자와 비교해서 같으면 카운팅
    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt += 1
        # 각 글자의 개수를 구한 후 최대값 비교
        if max_cnt < cnt:
            max_cnt = cnt
            max_str = str1[i]

    print('#{} {} {}'.format(tc, max_cnt, max_str))
