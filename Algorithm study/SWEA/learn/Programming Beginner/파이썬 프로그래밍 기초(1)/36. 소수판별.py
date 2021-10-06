number = int(input())

cnt = 0
for num in range(1, number+1):
    if number % num == 0:
        cnt += 1

if cnt == 2:
    print('소수입니다.')
else:
    print('소수가 아닙니다.')