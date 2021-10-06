students = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

a=0
b=0
ab=0
o=0

for i in students:
    if i == 'A':
        a += 1
    elif i == 'B':
        b += 1
    elif i == 'AB':
        ab +=1
    elif i == 'O':
        o += 1

print("{'A': %d, 'O': %d, 'B': %d, 'AB': %d}" % (a, o, b, ab))
