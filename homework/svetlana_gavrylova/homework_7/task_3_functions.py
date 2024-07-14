def get_index_of_number_in_text(text, char):
    return text.index(char)


def get_number_and_sum(text, index, num):
    return int(text[index + 1:].strip()) + num


results = ('результат операции: 42', 'результат операции: 514', 'результат работы программы: 9')

for result in results:
    ind = get_index_of_number_in_text(result, ':')
    number = get_number_and_sum(result, ind, 10)
    print(number)
