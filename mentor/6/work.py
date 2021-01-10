import json
print('Hello')
file = open('bd.json', 'r')
s = file.read()
# print(s)
dictionary = json.loads(s)
print(dictionary['users'])
dictionary['random_number'] = 123
dictionary['users'].append({"name": "Dima", "chat_id": 123, "account": 0})
str_dict = json.dumps(dictionary)
print(str_dict)

with open('path','w') as f:
    f.write('ss')

