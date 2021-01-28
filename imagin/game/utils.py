import json
from imagin.settings import BASE_DIR
from game.models import Gameuser
json_path = f'{BASE_DIR}/static/data.json'

def update_online_users_in_json():
    with open(json_path, 'r') as file:
        json_data = json.loads(file.read())
    users = []
    for user in Gameuser.objects.filter(is_online=True):
        users.append({ \
             'login': user.login, \
             'image': user.image.url, \
             'cards': [ \
                 {'image': 'static/images/8.jpg'}, \
                 {'image': 'static/images/9.jpg'}, \
             ]}) 

        print('append',user.login)
    json_data['users'] = users
    with open(json_path, 'w') as file:
        file.write(json.dumps(json_data))
    