import json


class Users:
    @property
    def users(self):
        return self.get()

    def get(self):
        file = open('db/users.json', 'r')
        users = json.loads(file.read())
        file.close()
        return users

    def add(self, user):
        print(user)
        file = open('db/users.json', 'w')

        self.users.append(user)
        if user not in self.users:
            pass

        file.write(json.dumps(self.users))
        file.close()
