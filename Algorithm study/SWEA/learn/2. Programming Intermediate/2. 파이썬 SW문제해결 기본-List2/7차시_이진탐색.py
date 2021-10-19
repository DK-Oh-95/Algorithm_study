# 테스트케이스 입력
T = int(input())

# 반복 횟수 계산하는 함수 생성
def count_repeat(p, p_target):
    # 시작, 끝지점과 몇 번 반복했는지 할당할 변수 생성
    start = 1
    end = p
    cnt = 1

    # 탐색 중 start가 end보다 뒤로 가면 중단
    # 페이지가 없는 경우는 없으므료 중단 됐을 때 return은 따로 지정하지 않는다
    # 작업 시행할 때마다 횟수 올림
    while start <= end:
        # center 값은 시작과 끝의 합을 2로 나눈 몫으로 지정
        c = (start + end) // 2
        # 찾는 값과 c가 같다면 그 때의 횟수 기록
        if p_target == c:
            return cnt
        # 찾는 값이 c보다 크면 작은 값들 버림
        elif p_target > c:
            start = c
            cnt += 1
        # 찾는 값이 c보다 작으면 큰 값들 버림
        else:
            end = c
            cnt += 1

for tc in range(1, T+1):
    # 전체페이지 p, A와 B가 찾을 쪽수 pa, pb 입력
    p, pa, pb = map(int, input().split())

    # 목표 페이지를 펼치는데 더 적은 횟수를 사용한 사람을 출력
    if count_repeat(p, pa) < count_repeat(p, pb):
        print('#{} A'.format(tc))
    elif count_repeat(p, pa) > count_repeat(p, pb):
        print('#{} B'.format(tc))
    else:
        print('#{} 0'.format(tc))


