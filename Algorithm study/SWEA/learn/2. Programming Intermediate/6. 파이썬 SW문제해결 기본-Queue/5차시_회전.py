T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = [0]

    front = 1
    rear = 0

    while arr:
        queue.append(arr.pop(0))
        rear += 1

    # M번 동안 front 위치의 값을 rear 위치로 옮김
    for _ in range(M):
        rear += 1
        queue[rear % (N+1)] = queue[front % (N+1)]
        front += 1

    print('#{} {}'.format(tc, queue[front % (N+1)]))



