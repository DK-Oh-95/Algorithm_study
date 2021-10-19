num = input()

num_list = list(num.split(', '))

def square(input_list):
    
    string = ''
    for number in input_list:
        square_num = int(number) ** 2
        string += f'square({number}) => {square_num}\n'

    return string[:-1:]

print(square(num_list))
