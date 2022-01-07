for tc in range(10):
    N = int(input())
    chars = [input() for _ in range(8)]

    result = 0
    for i in range(8):
        for j in range(9-N):
            for d in range(N//2):
                if chars[i][j+d] != chars[i][j+N-1-d]:
                    break
            else:
                result += 1

    for i in range(9 - N):
        for j in range(8):
            for d in range(N//2):
                if chars[i+d][j] != chars[i+N-1-d][j]:
                    break
            else:
                result += 1

    print('#{} {}'.format(tc+1, result))
