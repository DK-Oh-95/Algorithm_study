for s in range(1, int(input())+1):
    str_s = str(s)
    cnt_369 = str_s.count('3') + str_s.count('6') + str_s.count('9')

    if cnt_369:
        print('-'*cnt_369, end=' ')
    else:
        print(s, end=' ')
