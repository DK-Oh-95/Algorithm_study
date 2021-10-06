scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

i=0
n=0
while i<len(scores):
    if scores[i]>=80:
        n += scores.pop(i)
        # print(scores[i])
    else:
        z = scores.pop(i)
print(n)