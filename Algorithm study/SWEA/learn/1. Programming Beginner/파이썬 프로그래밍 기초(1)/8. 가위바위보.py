Man1 = str(input())
Man2 = str(input())

#1=가위, 2=바위, 3=보
if Man1=="가위" and Man2 =="가위":
    print("Result : Draw")
elif Man1=="가위" and Man2 =="바위":
    print("Result : Man1 Win!")
elif Man1=="가위" and Man2 =="보":
    print("Result : Man2 Win!")
elif Man1=="바위" and Man2 =="가위":
    print("Result : Man1 Win!")
elif Man1=="바위" and Man2 =="바위":
    print("Result : Draw")
elif Man1=="바위" and Man2 =="보":
    print("Result : Man2 Win!")
elif Man1=="보" and Man2 =="가위":
    print("Result : Man2 Win!")
elif Man1=="보" and Man2 =="바위":
    print("Result : Man1 Win!")
elif Man1=="보" and Man2 =="보":
    print("Result : Draw")
else:
    print("가위, 바위, 보 중에서 2가지 입력해주시기 바랍니다.")


