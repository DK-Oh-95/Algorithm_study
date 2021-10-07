def p_length(string):
    pattern = []
    pattern.append(string[0])

    for i in range(1, n):
        # 현재 글자가 패턴의 첫 글자와 다르면 패턴에 추가
        if string[i] != pattern[0]:
            pattern.append(string[i])
        # 현재 글자가 패턴의 첫 글자와 같으면 패턴 전체와 비교
        elif string[i] == pattern[0]:
            for j in range(len(pattern)):
                if string[i + j] != pattern[j]:
                    # 패턴과 다른 글자 발견하면 패턴에 추가하고 중단
                    pattern.append(string[i])
                    break
            # 다른 글자 하나도 없이 반복문을 마무리하면 그 때의 패턴 길이 반환
            else:
                return len(pattern)


T = int(input())
for tc in range(1, T+1):
    s = input()
    n = 30  # 문자열 길이

    print('#{} {}'.format(tc, p_length(s)))
