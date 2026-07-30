str1 = 'результат операции: 42'
str2 = 'результат операции: 514'
str3 = 'результат работы программы: 9'
pos_dig_1 = str1.index(':') + 1
pos_dig_2 = str2.index(':') + 1
pos_dig_3 = str3.index(':') + 1
dig_1 = int(str1[pos_dig_1:].strip())
dig_2 = int(str2[pos_dig_2:].strip())
dig_3 = int(str3[pos_dig_3:].strip())
result_1 = dig_1 + 10
result_2 = dig_2 + 10
result_3 = dig_3 + 10
print(result_1)
print(result_2)
print(result_3)

