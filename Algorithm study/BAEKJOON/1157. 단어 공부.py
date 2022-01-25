word = input().upper()
word_set = list(set(word))
n = len(word_set)
word_cnt = [0] * n

for i in range(n):
    for j in range(len(word)):
        if word_set[i] == word[j]:
            word_cnt[i] += 1

max_cnt = max(word_cnt)
if word_cnt.count(max_cnt) > 1:
    print('?')
else:
    for i in range(n):
        if word_cnt[i] == max_cnt:
            print(word_set[i])
