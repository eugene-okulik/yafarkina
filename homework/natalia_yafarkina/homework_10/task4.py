PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


# вариант 1
split_list1 = PRICE_LIST.split()
clear_list1 = [item.rstrip('р') for item in split_list1]
key1 = [item for item in clear_list1 if item.isalpha()]
values1 = [int(item) for item in clear_list1 if item.isdigit()]
price_dict1 = dict(zip(key1, values1))
print('вариант 1: ', price_dict1)


# вариант 2
split_list2 = PRICE_LIST.split()
key2 = [split_list2[i] for i in range(0, len(split_list2), 2)]
values2 = [split_list2[i+1].replace('р', '') for i in range(0, len(split_list2), 2)]
d_values2 = list(map(int, values2))
price_dict2 = {key : values for key, values in zip(key2, d_values2)}
print('вариант 2: ',price_dict2)


# вариант 3
split_list3 = PRICE_LIST.split()
clear_list3 = [item.rstrip('р') for item in split_list3]
new_list = [int(item) if item.isdigit() else item for item in clear_list3]
price_dict3 = {new_list[i] : new_list[i+1] for i in range(0, len(new_list), 2)}
print('вариант 3: ', price_dict3)








