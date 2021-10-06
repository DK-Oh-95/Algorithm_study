word = input()

word_list = list(word.split(', '))

def compare(word_list):
    if len(word_list[0]) > len(word_list[1]):
        return word_list[0]
    else:
        return word_list[1]

print(compare(word_list))