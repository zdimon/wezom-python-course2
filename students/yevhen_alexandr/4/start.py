from libs.utils import add

name = 'Dima,Fedor,Yeugen,Ilya'

name_2 = name.replace(',', '-')

print(name_2)

name_arr = name.split(',')

name_3 = []
for i, item in enumerate(name.split(',')):
    name_3.append(f'{i + 1}.{item};')

name_3 = ''.join(name_3)
print(name_3)

print(add(5, 6, 7, 8))