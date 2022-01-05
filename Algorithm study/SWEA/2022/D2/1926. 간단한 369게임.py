N = int(input())

# 각 자리수가 3의 배수인지 확인한다
for i in range(1, N+1):
    result = i  # 출력할 결과

    # 3자리수 일 때 100의 자리 3의 배수인지 확인
    if i >= 100:
        quotient = i // 100
        remain = i % 100
        if quotient % 3 == 0:
            result = '-'

        # 10의 자리 3의 배수인지 확인
        if remain >= 10:
            quotient = remain // 10
            remain = remain % 10
            # 앞 자리가 3의 배수였을 경우
            if type(result) == str and quotient % 3 == 0:
                result += '-'
            elif quotient % 3 == 0:
                result = '-'

        # 1의 자리 3의 배수인지 확인
        if type(result) == str and remain != 0 and remain % 3 == 0:
            result += '-'
        elif remain != 0 and remain % 3 == 0:
            result = '-'

    # 2자리수 일 때 10의 자리 3의 배수인지 확인
    elif i >= 10:
        quotient = i // 10
        remain = i % 10
        if quotient % 3 == 0:
            result = '-'

        # 1의 자리 3의 배수인지 확인
        if type(result) == str and remain != 0 and remain % 3 == 0:
            result += '-'
        elif remain != 0 and remain % 3 == 0:
            result = '-'

    # 1자리수 일 때 1의 자리 3의 배수인지 확인
    else:
        if i != 0 and i % 3 == 0:
            result = '-'

    print(result, end=' ')
