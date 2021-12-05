# # 계산 범위는 0 ~ 999
# # 터치 횟수가 M을 넘으면 안된다
# def solve():
#
#
#
#
#
# for tc in range(int(input())):
#     # N: 터치가능 숫자 수, O: 터치가능 연산자 수, M: 최대 터치 가능 수
#     N, O, M = map(int, input().split())
#     numbers = list(map(int, input().split()))  # 입력 가능한 숫자
#     # ‘+’: 1, ‘-‘: 2, ‘*’: 3, ‘/’: 4
#     operators = list(map(int, input().split()))  # 입력 가능한 연산자
#     W = int(input())  # 목표 값
#
#     # W의 각 자리수를 모두 누를 수 있으면 자리수가 최소 입력 횟수
#     tmp = W
#     for i in range(len(str(W))):
#         if tmp % 10 not in numbers:
#             # 누를 수 없는 수가 있는 경우 함수 동작
#             ans = solve()
#             break
#         tmp //= 10
#     else:
#         ans = len(str(W))
#

