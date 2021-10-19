scores=[88, 30, 61, 55, 95]

k=0
for i in scores:
    if i>=60:
        k+=1
        print("{0}번 학생은 {1}점으로 합격입니다.".format(k, i))
    else:
        k+=1
        print("{0}번 학생은 {1}점으로 불합격입니다.".format(k, i))    