words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for word, count in words.items():
    for i in range(count):
        print(word, end='')
