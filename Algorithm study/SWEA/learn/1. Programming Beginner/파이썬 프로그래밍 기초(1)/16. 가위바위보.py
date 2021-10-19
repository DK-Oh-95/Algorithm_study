Man1 = str(input())
Man2 = str(input())
print(type(Man1))

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


