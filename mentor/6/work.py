import json
print('Hello')
file = open('bd.json', 'r')
s = file.read()
file.close()
# print(s)
dictionary = json.loads(s)
print(dictionary['users'])
dictionary['random_number'] = 123
is_single = 0
for index in range(len(dictionary['users'])):
    if dictionary['users'][index]['chat_id'] == 123:
        is_single+=1
if is_single == 0:
    dictionary['users'].append({"name": "Dima", "chat_id": 123, "account": 0})
str_dict = json.dumps(dictionary)
file = open('bd.json', 'w')
file.write(str_dict)
file.close()

print(str_dict)

with open('path','w') as f:
    f.write('ss')

