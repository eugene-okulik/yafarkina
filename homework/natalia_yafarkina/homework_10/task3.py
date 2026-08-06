def controls_operation(func):
    def wrapper(first, second, operation):
        if first == second:
            operation = '+'
        if first > second:
            operation = '-'
        if first < second:
            operation = '/'
        if first < 0 or second < second:
            operation = '*'
        return func(first, second, operation)
    return wrapper


@controls_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


result = calc(54,12, '+')
print(result)
