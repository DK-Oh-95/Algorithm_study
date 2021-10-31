# 각 인덱스에 있는 요소와 교환해서 만들 수 있는 모든 경우의 수 살펴보기
def perm(idx):
    if idx == N-1:
        # 순열이 생성되면 그 때의 배터리 총 사용량 계산
        leakage(p)
        return
    # 나보다 뒤쪽에 있는 요소들이랑 모두 자리 바꾸어보기 (자리 안바꾸는 것도 포함)
    for j in range(idx, N-1):
        p[j], p[idx] = p[idx], p[j]
        # idx+1 요소 자리바꾸기
        perm(idx+1)
        p[j], p[idx] = p[idx], p[j]  # 원상복구


# 생성된 경로에 따라 배터리 사용량 계산하는 함수
def leakage(route):
    global min_leakage

    battery_leak = 0
    # 순열로 만들어진 경로에 따라 이동
    battery_leak += battery[0][route[0]]
    for d in range(1, len(route)):
        battery_leak += battery[route[d-1]][route[d]]
    battery_leak += battery[route[-1]][0]  # 출발지로 되돌아올 때 사용량

    # 최소 사용량과 비교 후 갱신
    if min_leakage > battery_leak:
        min_leakage = battery_leak
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]

    # 순열을 만들기 위한 리스트
    p = []
    for i in range(1, N):
        p.append(i)

    min_leakage = 1000  # 최소 배터리 사용량 비교할 변수
    perm(0)

    print('#{} {}'.format(tc, min_leakage))
