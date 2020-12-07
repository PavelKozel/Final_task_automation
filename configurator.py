

class Configurator:
    def __init__(self, user_role):                    # Reads json according to the input parameter user_role
        with open('config.json') as f:
            self.config = eval(f.read())
        self.config = self.config[user_role]

    def get_login(self):                              # Gets login from json
        return self.config['login']

    def get_password(self):                           # Gets password from json
        return self.config['password']