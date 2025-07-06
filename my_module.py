def calc(a, b, sign):
    if sign == '+':
        return a + b
    elif sign == '-':
        return a - b
    else:
        return 'Invalid operator'

print(calc(4, 2, '+'))
