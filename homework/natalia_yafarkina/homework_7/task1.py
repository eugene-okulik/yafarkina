picked_number = 7
num = int(input('Угадай цифру: '))
while picked_number != num:
    print('Попробуйте снова')
    num = int(input('Угадай цифру: '))
else:
    print('Поздравляю! Вы угадали!')
