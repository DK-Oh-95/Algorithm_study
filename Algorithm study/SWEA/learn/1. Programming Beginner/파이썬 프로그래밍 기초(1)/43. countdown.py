def countdown(num):
    if num < 1:
        return '카운트다운을 하려면 0보다 큰 입력이 필요합니다.'

    while num != 1:
        print(num)
        num -= 1
    return 1

print(countdown(0))
print(countdown(10))
