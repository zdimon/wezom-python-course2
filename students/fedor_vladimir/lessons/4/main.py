from lib.utils import add
print('Hello')
a = 3
b = 4
c = a+b
a = 777
n = a
name = 'Dima,Fedor,Yeugen,Ilya'
# print(dir(name))

arr = name.split(',')
name1 = name.replace(',', '-')
name2 = ''
for i in range(len(arr)):
    name2 = name2 + "%i.%s; " % (i + 1, arr[i])

print(name2)


#print(id(a))
#f = print(n)
#print(f)


if __name__ == "__main__":
    print(add(1,2,3,4,5,6))