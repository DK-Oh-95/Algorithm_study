# 테스트케이스 T 입력
T = int(input())

for tc in range(1, T+1):
    # 카드 수 입력
    N = int(input())
    # 숫자 입력(여백이 없기 때문에 litarable한 문자열 그대로 입력)
    aj = input()

    aj_list=[]
    for i in aj:
        aj_list += [int(i)]
    # 0 <= aj <= 9 이므로 인덱스로 사용하기 위해 배열의 최대값보다 1 큰 10을 크기로 하는 리스트 생성
    count = [0] * 10

    for i in aj_list:
        # aj_list[i] 요소가 몇 번 나왔는지 체크
        count[i] += 1

    # 가장 많이 반복된 횟수
    most_value = 0
    # 가장 큰 숫자
    biggest_number = 0
    # 각 숫자가 반복된 횟수가 적힌 리스트에서 가장 많이 반복된 값을 찾을 때의 인덱스를 가장 큰 값으로 할당
    for j in range(len(count)):
        # 인덱스를 순차적으로 돌기 때문에 조건을 >=로 지정하면 횟수 같을 때 어차피 가장 큰 인덱스 값이 할당된다.
        if count[j] >= most_value:
            # 해당 반복횟수를 변수에 할당
            most_value = count[j]
            # 그 때의 인덱스 값을 가장 큰 수 변수에 할당
            biggest_number = j

    print('#{} {} {}'.format(tc, biggest_number, most_value))