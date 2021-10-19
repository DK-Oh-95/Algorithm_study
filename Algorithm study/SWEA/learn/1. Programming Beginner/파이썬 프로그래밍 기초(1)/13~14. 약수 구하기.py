data = int(input())

i = 1
cnt = 0

while i<=data:
    if data % i == 0:
        result = i
        print(f'{result}(은)는 {data}의 약수입니다.')
        i+=1
        cnt+=1
    else:
        i+=1
if cnt == 2: #소수면 표시
            print(f'{data}(은)는 1과 {data}로만 나눌 수 있는 소수입니다.')
            i+=1
            cnt+=1
