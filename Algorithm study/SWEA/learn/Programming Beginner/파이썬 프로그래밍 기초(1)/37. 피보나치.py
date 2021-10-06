num = int(input())

i = 1
fibo = [1]
fibo_num = 1
fibo_num2= 1

while i < num:
    fibo.append(fibo_num)
    fibo_num2, fibo_num = fibo_num, fibo_num + fibo_num2
    i += 1

print(fibo)