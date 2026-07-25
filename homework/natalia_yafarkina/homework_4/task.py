my_dict = {
    "tuple": (1, 2.0, 6, 1024, 3.5, 10, 7.5),
    "list": ['15-89-56', 'удалить', 67.9, 90, 1, None, -8],
    "dict": {
        "person1": {"name": "Иван", "favorite_color": "красный"},
        "person2": {"name": "Петр", "favorite_color": "оранжевый"},
        "person3": {"name": "Федор", "favorite_color": "желтый"},
        "person4": {"name": "Мария", "favorite_color": "зеленый"},
        "person5": {"name": "Анастасия", "favorite_color": "голубой"},
        "person6": {"name": "Анна", "favorite_color": "синий"},
        "person7": {"name": "Инна", "favorite_color": "фиолетовый"}
        },
    "set": {'рубашка', 'брюки', 'юбка', 'блузка', 'шорты', 'футболка', 'джемпер'}
}

# Для того, что хранится под ключом ‘tuple’:
# выведите на экран последний элемент

print(my_dict['tuple'][-1])


# Для того, что хранится под ключом ‘list’:
# добавьте в конец списка еще один элемент
# удалите второй элемент списка

my_dict['list'].append(5)
my_dict['list'].remove(my_dict['list'][1])
print(my_dict['list'])


# Для того, что хранится под ключом ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением
# удалите какой-нибудь элемент

my_dict['dict'][('i am a tuple',)] = 22
del my_dict['dict']['person7']
print(my_dict['dict'])


# Для того, что хранится под ключом ‘set’:
# добавьте новый элемент в множество
# удалите элемент из множества

my_dict['set'].add('водолазка')
my_dict['set'].discard('шорты')
print(my_dict['set'])


# В конце выведите на экран весь словарь

print(my_dict)