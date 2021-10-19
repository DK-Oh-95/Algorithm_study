for i in range(200):
    if i==196:
        print(f'{i}', end='')
    elif    i%7 == 0 and i%5 != 0:
        print(f'{i},', end='')

