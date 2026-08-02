import random as rnd


salary = int(input('введите число'))
bonus = bool(rnd.randint(0,1))
if bonus:
    print(f"{salary}, {bonus} - ${salary + rnd.randrange(1,1001)}")
else:
    print(f"{salary}, {bonus} - ${salary}")
