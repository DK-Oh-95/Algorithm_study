T = int(input())
for tc in range(1, T+1):
    memory = input()
    n = len(memory)

    cnt = 0
    for i in range(n):
        if i == 0 and memory[i] == '1':
            cnt += 1
        elif i > 0 and memory[i-1] != memory[i]:
            cnt += 1

    print('#{} {}'.format(tc, cnt))
