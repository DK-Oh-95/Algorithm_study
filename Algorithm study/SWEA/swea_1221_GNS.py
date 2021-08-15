# 테스트케이스 개수 입력
T = int(input())

def search_num(arr, pattern):
    # 입력받은 배열을 순회하며 찾고있는 pattern이랑 동일하면 리스트에 저장
    # 값을 저장할 리스트 생성
    result = []
    for i in arr:
        if i == pattern:
            result += [i]
    return result

for _ in range(T):
    # 테스트케이스 번호, 길이 입력
    tc, len_tc = input().split()
    # 단어 입력
    numbers = list(input().split())

    # ZRO, ONE, TWO, THR, FOR, FIV, SIX, SVN, EGT, NIN 각 경우의 리스트 합침
    result = search_num(numbers, 'ZRO') + search_num(numbers, 'ONE') + search_num(numbers, 'TWO') + search_num(numbers, 'THR') + search_num(numbers, 'FOR') + search_num(numbers, 'FIV') + search_num(numbers, 'SIX') + search_num(numbers, 'SVN') + search_num(numbers, 'EGT') + search_num(numbers, 'NIN')

    print('{}'.format(tc), *result)