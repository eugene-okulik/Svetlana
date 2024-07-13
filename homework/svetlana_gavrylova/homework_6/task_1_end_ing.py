text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, ' \
        + 'facilisis vitae semper at, dignissim vitae libero'

words = text.split()

for word in words:
    if word.endswith('.'):
        word = word.replace(word[-1], 'ing.')
    elif word.endswith(','):
        word = word.replace(word[-1], 'ing,')
    else:
        word = word + 'ing'

    print(word, end=' ')
