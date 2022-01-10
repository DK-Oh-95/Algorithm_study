def solution(s):
    answer = ''

    numbers = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
               'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    tmp = ''
    for i in range(len(s)):
        if s[i].isnumeric():
            answer += s[i]
        else:
            tmp += s[i]

        if tmp in numbers:
            answer += numbers[tmp]
            tmp = ''
    return int(answer)


print(solution("one4seveneight"))
print(solution("23four5six7"))
