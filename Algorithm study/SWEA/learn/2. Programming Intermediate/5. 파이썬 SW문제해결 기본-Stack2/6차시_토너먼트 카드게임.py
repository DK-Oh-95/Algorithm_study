# 영역이 필요하다
def game(s, e):
    # s, e에 포함되는 학생 중 승자를 반환하는 함수
    # 승자의 인덱스를 반환
    # 더 이상 쪼갤 수 없으면, 스스로가 승자
    # 요소가 하나일 때 s, e가 같음
    if s == e:
        return s

    # 쪼갤 수 있는 상태
    # 왼쪽 그룹 승자 구하기
    left_win = game(s, (s+e)//2)
    # 오른쪽 그룹 승자 구하기
    right_win = game((s+e)//2 + 1, e)

    # arr[left_win] >> 왼쪽 승자 카드
    # arr[right_win] >> 오른쪽 승자 카드
    # 가위바위보 승자 찾기
    # return winner

    winner = left_win
    left_card = cards[left_win]
    right_card = cards[right_win]

    if left_card == 1:
        if right_card == 2:
            winner = right_win
        elif right_card == 3:
            winner = left_win
    elif left_card == 2:
        if right_card == 3:
            winner = right_win
        elif right_card == 1:
            winner = left_win
    elif left_card == 3:
        if right_card == 1:
            winner = right_win
        elif right_card == 2:
            winner = left_win

    return winner


# 테스트케이스
T = int(input())

for tc in range(1, T+1):
    # 인원수 N
    N = int(input())
    # N명이 고른 카드 1: 가위, 2: 바위, 3: 보
    cards = list(map(int, input().split()))

    result = game(0, N-1) + 1
    print('#{} {}'.format(tc, result))
