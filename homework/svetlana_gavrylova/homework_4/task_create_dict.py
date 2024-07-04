my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [6, 7, 8, 9, 10],
    'set': {11, 12, 13, 14, 15},
    'dict': {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3',
        'key4': 'value4',
        'key5': 'value5'
    }
}

last_tuple_element = my_dict['tuple'][-1]

my_dict['list'].append(555)
my_dict['list'].pop(1)

my_dict['dict']['i am a tuple'] = ('Sometimes', 'I', 'feel', 'like', 'a', 'tuple')
del my_dict['dict']['key1']

my_dict['set'].add(777)
my_dict['set'].remove(13)

print(f'The last element in the tuple: {last_tuple_element}')
print(f'The dictionary after updates:\n{my_dict}')
