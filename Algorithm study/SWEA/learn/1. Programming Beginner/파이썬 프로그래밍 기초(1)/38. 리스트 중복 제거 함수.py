a = [1, 2, 3, 4, 3, 2, 1]

def duplicated(alist):
    set_list = set(alist)
    sort_list = sorted(list(set_list))
    print(alist)
    return sort_list

print(duplicated(a))