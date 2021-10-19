a_human = input()
b_human = input()
a = input()
b = input()

if a == b:
    print('비겼습니다.')
elif a == '가위' and b == '바위' :
    print('바위가 이겼습니다!')
elif a == '가위' and b == '보':
    print('가위가 이겼습니다!')
elif a == '바위' and b == '보':
    print('보가 이겼습니다!')
elif a == '바위' and b == '가위':
    print('바위가 이겼습니다!')
elif a == '보' and b == '바위':
    print('보가 이겼습니다!')
elif a == '보' and b == '가위':
    print('가위가 이겼습니다!')