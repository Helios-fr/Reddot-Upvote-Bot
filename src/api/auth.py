def login(username, password):
    import requests

    login_data = {
        "op": "login-main",
        "user": username,
        "passwd": password,
        "api_type": "json"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "origin": "https://old.reddit.com",
        "referer": "https://old.reddit.com/"
    }
    response = requests.post(f"https://old.reddit.com/api/login/{username}", data=login_data, headers=headers)

    modhash = response.json()['json']['data']['modhash']

    edgebucket_cookie = response.cookies.get('edgebucket')
    loid_cookie = response.cookies.get('loid')
    reddit_session_cookie = response.cookies.get('reddit_session')
    session_tracker_cookie = response.cookies.get('session_tracker')

    cookies = {
        'loid': loid_cookie,
        'session_tracker': session_tracker_cookie,
        'csv': '2',
        'edgebucket': edgebucket_cookie,
        'reddit_session': reddit_session_cookie,
    }

    return cookies, modhash

def get_access_token(user):
    import requests

    username = user.username
    password = user.password
    app_id = user.app_id
    app_secret = user.app_secret

    # create the data
    data = {
        'grant_type': 'password',
        'username': username,
        'password': password
    }

    # create the headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0'
    }

    # create the auth
    auth = requests.auth.HTTPBasicAuth(app_id, app_secret)

    # send the request
    response = requests.post('https://www.reddit.com/api/v1/access_token', data=data, headers=headers, auth=auth)

    return response.json()['access_token']