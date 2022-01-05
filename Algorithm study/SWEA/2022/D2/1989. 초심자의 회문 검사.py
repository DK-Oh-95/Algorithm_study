for tc in range(int(input())):
    word = input()
    ans = 1
    for i in range(len(word)//2 + 1):
        if word[i] != word[len(word) - i - 1]:
            ans = 0
            break

    # print(f'#{tc+1} {ans}')
    print('#{} {}'.format(tc+1, ans))
