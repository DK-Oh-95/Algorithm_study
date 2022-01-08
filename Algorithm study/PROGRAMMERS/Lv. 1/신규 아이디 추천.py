def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    new_id_list = list(new_id)
    for i in range(len(new_id_list)):
        # 5단계
        if new_id_list[i] == '':
            new_id_list[i] = 'a'
        # 2단계
        if not new_id_list[i].isalpha() and not new_id_list[i].isnumeric() and new_id_list[i] not in ['-', '_', '.']:
            new_id_list[i] = ''

    new_id = ''.join(new_id_list)
    new_id_list = list(new_id)

    # 3단계
    for i in range(len(new_id_list)):
        if i != len(new_id_list) - 1 and new_id_list[i] == '.' and new_id_list[i + 1] == '.':
            new_id_list[i] = ''

    new_id = ''.join(new_id_list)
    new_id_list = list(new_id)

    # 4단계
    for i in range(len(new_id_list)):
        if i == 0 and new_id_list[i] == '.' or i == len(new_id_list)-1 and new_id_list[i] == '.':
            new_id_list[i] = ''
    new_id = ''.join(new_id_list)

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:14]

    # 7단계
    while len(new_id) <= 2:
        if new_id:
            new_id += new_id[-1]
        else:
            new_id = 'aaa'

    return new_id


print(solution('...!@BaT#*..y.abcdefghijklm'))
# print(solution('z-+.^.'))
# print(solution('=.='))
# print(solution('123_.def'))
# print(solution('abcdefghijklmn.p'))

#############################################################
# 학습 추천
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
