ans = ''
for i in range(100,301):
    if int(str(i)[0])%2==0 and int(str(i)[1])%2==0 and int(str(i)[2])%2==0:
        ans += str(i) + ","
        
print(ans[:-1])
