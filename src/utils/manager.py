class Manager:
    def __init__(self, file=None):
        self.accounts = {}
        if file != None:
            self.load(file)

    def load(self, file):
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
                        'password': line[1],
                        'app_id': line[2],
                        'app_secret': line[3]
                    }
    
    def save(self, file):
        with open(file, 'w') as f:
            for username in self.accounts:
                account = self.accounts[username]
                f.write(f'{username}:{account["password"]}:{account["app_id"]}:{account["app_secret"]}\n')
    
    def get_api(self, username):
        import praw

        # get the account
        account = self.accounts[username]

        # create a reddit instance
        reddit = praw.Reddit(
            client_id=account['app_id'],
            client_secret=account['app_secret'],
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
            username=username,
            password=account['password']
        )

        return reddit

if __name__ == '__main__':
    # run main.py
    import os
    os.system('python src/main.py')

        
