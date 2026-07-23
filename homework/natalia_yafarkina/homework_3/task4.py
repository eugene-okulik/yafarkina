# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь

import math as m


leg1=10
leg2=20
hypotenuse = m.sqrt(m.pow(leg1,2)+m.pow(leg2,2))
square = (leg1*leg2)/2
print(hypotenuse)
print(square)