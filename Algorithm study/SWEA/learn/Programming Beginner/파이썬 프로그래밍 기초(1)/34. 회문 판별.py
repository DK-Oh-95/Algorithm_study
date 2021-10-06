word = input()

reversed_word = word[::-1]

print(reversed_word)
if reversed_word == word:
    print('입력하신 단어는 회문(Palindrome)입니다.')