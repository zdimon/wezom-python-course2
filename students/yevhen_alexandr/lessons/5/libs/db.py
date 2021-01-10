import json
from os import path


class DB():
    def __init__(self, file):
        self.file = file
        self.data = {}
        self.read_bd()


    def read_bd(self):
        print(path.exists(self.file))
        if path.exists(self.file):
            db_file = open(self.file)
            self.data = json.loads(db_file.read())
            db_file.close()


    def write_bd(self):
        db_file = open(self.file, 'w')
        db_file.write(json.dumps(self.data))
        db_file.close()


    def get_users(self):
        users = self.data.get('users')

        if users:
            return users.copy()

        return {}


    def add_user(self, user):
        users = self.get_users()
        user_id = user.get('id')
        if str(user_id) not in users.keys():
            users.update({ str(user.get('id')): user })
            self.data.update({ 'users': users })
            self.write_bd()