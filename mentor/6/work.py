import json
print('Hello')
file = open('bd.json', 'r')
s = file.read()
# print(s)
dictionary = json.loads(s)
print(dictionary['users'])
dictionary['random_number'] = 123
str_dict = json.dumps(dictionary)
print(str_dict)