import json


class DB():
    def __init__(self, file):
        self.file = file
        self.read_bd()


    def read_bd(self):
        db_file = open(self.file)
        self.data = json.loads(db_file.read())
        db_file.close()


    def write_bd(self):
        db_file = open(self.file, 'w')
        db_file.write(json.dumps(self.data))
        db_file.close()


    def add_user(self, message):
        users = self.data.get('users')
        users.append(message.from_user)
        print(users)
        self.data['users'] = users
        self.write_bd()