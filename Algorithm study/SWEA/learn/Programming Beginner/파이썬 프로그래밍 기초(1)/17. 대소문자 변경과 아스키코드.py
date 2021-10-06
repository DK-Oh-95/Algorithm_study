word = input()

if word.isupper():
    change = word.lower()
    print(f'{word}(ASCII: {ord(word)}) => {change}(ASCII: {ord(change)})')
elif word.islower():
    change = word.upper()
    print(f'{word}(ASCII: {ord(word)}) => {change}(ASCII: {ord(change)})')
else:
    print(word)