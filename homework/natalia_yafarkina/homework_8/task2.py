def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b

lst = [5, 200, 1000, 10000, 100000]
for n in lst:
    fib = fibonacci()
    print(f'ряд Фибоначи для {n}:', end=' ')
    for num in fib:
        if num > n:
            break
        print(num, end=' ')
    print()
