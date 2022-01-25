N = int(input())
result = 0

for _ in range(N):
    word = input()

    tmp = word[0]
    used = []
    for i in range(1, len(word)):
        if word[i] in used:
            break

        if tmp == word[i]:
            pass
        else:
            used.append(tmp)
            tmp = word[i]
    else:
        result += 1

print(result)
