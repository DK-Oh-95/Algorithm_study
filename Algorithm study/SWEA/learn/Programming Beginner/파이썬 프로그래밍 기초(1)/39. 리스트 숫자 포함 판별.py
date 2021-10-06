sample_list = [2, 4, 6, 8, 10]

def find_num(sample_list):
    cnt_5 = 0
    cnt_10 = 0

    for num in sample_list:
        if num == 5:
            cnt_5 += 1
        else:
            pass
        if num == 10:
            cnt_10 += 1
        else:
            pass

    print(sample_list)
    if cnt_5 < 1 and cnt_10 > 0:
        return '5 => False\n10 => True'
        
print(find_num(sample_list))
