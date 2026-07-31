for item in range(1, 101):
    if item % 3 == 0 and item % 5 == 0:
        print('FuzzBuzz')
    elif item % 3 == 0:
        print('Fuzz')
    elif item % 5 == 0:
        print('Buzz')
    else:
        print(item)
