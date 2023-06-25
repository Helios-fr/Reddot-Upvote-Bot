class User:
    def __init__(self, username, password, app_id, app_secret):
        from .auth import login
        self.username = username
        self.password = password
        self.app_id = app_id
        self.app_secret = app_secret
        self.cookie, self.modhash = login(username, password)