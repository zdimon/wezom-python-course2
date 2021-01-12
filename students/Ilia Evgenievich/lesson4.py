name = 'Dima,Fedor,Yeugen,Ilya'

arr = name.split(',')
print(arr)
name2 = name.replace(",","-")
name3 = name.replace(",",';')
i=1
text = ''
for elem in arr:
    text+=f'{i}.{elem};'
    i+=1
text = text[:-1]
print(text)
print(name2)
#print(id(a))
#f = print(n)
#print(f)

from libs.add import add
from libs.utils import Dog, Cat

dog = Dog()
cat = Cat()

dog.jump()
cat.jump()
print(add(2,3,4,7,5,6))