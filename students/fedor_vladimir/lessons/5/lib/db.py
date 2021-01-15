import json
from json.decoder import JSONDecodeError


class Users:
    @property
    def users(self):
        try:
            return self.get()
        except JSONDecodeError:
            return {}

    def get(self):
        with open("db/users.json", "a+") as file:
            return json.loads(file.read())

    def add(self, user):
        with open("db/users.json", "a+") as file:
            users = self.users
            users.update({user: user})
            file.write(json.dumps(users))
