input_value = input()

def give_value(character):
    if character == 'I':
        return 1
    elif character == 'V':
        return 5
    elif character == 'X':
        return 10
    elif character == 'L':
        return 50
    elif character == 'C':
        return 100
    elif character == 'D':
        return 500
    elif character == 'M':
        return 1000
    else:
        return 0

sum = 0
for i in range(len(input_value)):
    sum += give_value(input_value[i])

print(sum)
