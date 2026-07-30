text = '''Etiam tincidunt neque erat, quis molestie enim imperdiet vel. 
Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'''
ending = 'ing'
lst_old = text.split()
lst_new = []
for item in lst_old:
    if item.endswith('.'):
        item = f"{item.strip('.')}{ending}{'.'}"
        lst_new.append(item)
    elif item.endswith(','):
        item = f"{item.strip(',')}{ending}{','}"
        lst_new.append(item)
    else:
        item = f"{item}{ending}"
        lst_new.append(item)
print(' '.join(lst_new))
