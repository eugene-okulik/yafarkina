words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
for key in words:
    i = int(words[key])
    while i > 0:
        print(key, end=' ')
        i -= 1
    else:
        print()
