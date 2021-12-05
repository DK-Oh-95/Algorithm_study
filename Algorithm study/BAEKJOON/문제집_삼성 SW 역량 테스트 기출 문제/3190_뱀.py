N = int(input())  # 보드의 크기
K = int(input())  # 사과의 개수
k_list = [list(map(int, input().split())) for _ in range(K)]  # 사과 위치
L = int(input())  # 뱀 방향전환 횟수
l_list = [list(input().split()) for _ in range(L)]  # x초 뒤 방향전환, 'L': 왼쪽, 'D': 오른쪽

# 보드 생성
board = [[0] * N for _ in range(N)]
# 사과 생성
for i in range(K):
    board[k_list[i][0]][k_list[i][1]] = 1

second = 0
r = c = 0
while 0 <= r < N and 0 <= c < N:
