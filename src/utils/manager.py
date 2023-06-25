class Manager:
    def __init__(self, file=None):
        self.accounts = {}
        self.proxies = None
        if file != None:
            self.load(file)

    def load(self, file, logging=False):
        import colorama

        with open(file, 'r') as f:
            for line in f:
                # split the line by :
                line = line.split(':')
                # check if the list has 2 values
                if len(line) == 2:
                    # the accounts dont have an app id
                    pass
                
                if len(line) == 4:
                    # add the account to the accounts dictionary
                    # the line is username:password:app_id:app_secret
                    self.accounts[line[0]] = {
                        'username': line[0],
                        'password': line[1],
                        'app_id': line[2],
                        'app_secret': line[3].strip()
                    }

                    if logging:
                        # [+] Loaded account {username} into database
                        print(colorama.Fore.CYAN + f"[" + colorama.Fore.GREEN + "+" + colorama.Fore.CYAN + f"] Loaded account {line[0]} into database")
    
    def save(self, file):
        with open(file, 'w') as f:
            for username in self.accounts:
                account = self.accounts[username]
                f.write(f'{username}:{account["password"]}:{account["app_id"]}:{account["app_secret"]}\n')
    
    def get_api(self, username):
        from api import User

        user = User(self.accounts[username]['username'], 
                    self.accounts[username]['password'], 
                    self.accounts[username]['app_id'], 
                    self.accounts[username]['app_secret'])

        return user

if __name__ == '__main__':
    # run main.py
    import os
    os.system('python src/main.py')

        
