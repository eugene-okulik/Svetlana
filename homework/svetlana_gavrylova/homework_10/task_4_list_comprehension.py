PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

# price_list = PRICE_LIST.split('\n')
# price_couple = [item[:-1].split() for item in price_list]
# form_dict = {key: int(value) for key, value in price_couple}
# print(price_couple)

# in one line:
form_dict = {key: int(value) for key, value in [item[:-1].split() for item in PRICE_LIST.split('\n')]}
# or this one - not sure which one is better:
new_list = {x.split(' ')[0]: int(x.split(' ')[1][:-1]) for x in PRICE_LIST.split('\n')}

print(form_dict)
print(new_list)
