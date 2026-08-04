import sys


sys.set_int_max_str_digits(100000)


def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


lst = [5, 200, 1000, 10000, 100000]
for n in lst:
    fib = fibonacci()
    pos = 1
    for num in fib:
        if pos == n:
            print(f'число Фибоначчи для позиции {pos}: {num}', end=' ')
            break
        pos += 1
    print()
