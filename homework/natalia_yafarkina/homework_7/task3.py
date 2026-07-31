str1 = 'результат операции: 42'
str2 = 'результат операции: 54'
str3 = 'результат работы программы: 209'
str4 = 'результат: 2'

def sep_num(my_str):
    pos_dig = my_str.index(':') + 1
    dig = int(my_str[pos_dig:].strip())
    result = dig + 10
    return result

print(sep_num(str1))
print(sep_num(str2))
print(sep_num(str3))
print(sep_num(str4))
