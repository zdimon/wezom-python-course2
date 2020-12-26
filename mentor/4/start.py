#print('Hello')
a = 3
b = 4
c = a+b
a = 777
n = a
name = 'Dima,Fedor,Yeugen,Ilya'
name2 = 'Dima,Fedor,Yeugen,Ilya'
#name[0] = 'B'
#name2 = name

print(id(name))
print(id(name2))

name = 'onethow'
print(name2)

print(id(name))
print(id(name2))

lst = [1,2,3]
#print(dir(lst))
tuple = (1,2)


from libs.utils import add

rez = add(2,6,3,4,5,6)
print(rez)

#name = 'Dima-Fedor-Yeugen-Ilya'
#name = '1.Dima;2.Fedor;3.Yeugen;4.Ilya'
#arr = 'fff;fff;ff'.split(',')
#arr = name.split(',')
#d = '-'.join(arr)
#print(d)
#print(dir(name))
# for index, el in enumetare(name):
#     print(i)








#print(id(a))
#f = print(n)
#print(f)
