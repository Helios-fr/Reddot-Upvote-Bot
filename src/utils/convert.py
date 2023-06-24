import requests

def login(username, password):
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

    # save the modhash in the response text
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

def create_app(cookies, uh):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'https://www.reddit.com/prefs/apps',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.reddit.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'DNT': '1',
        'Sec-GPC': '1',
        'Connection': 'keep-alive'
    }

    data = f'uh={uh}&name=example&app_type=script&description=&about_url=example.com&redirect_uri=http://www.example.com&id=^%^23create-app&renderstyle=html'

    response = requests.post('https://www.reddit.com/api/updateapp', cookies=cookies, headers=headers, data=data)

    return response.text

def Convert(username, password):
    cookies, uh = login(username, password)
    response_text = create_app(cookies, uh)

    app_id = response_text.split('developed-app-')[1].split('"')[0][:22]
    app_secret = response_text.split(r'secret&lt;/th&gt;&lt;td class=\"prefright\"&gt;')[1].split("&")[0]

    return f"{username}:{password}:{app_id}:{app_secret}"

# print(Convert("177954", '4P."f7ybqKrStjE'))

if __name__ == '__main__':
    username = input("Username: ")
    password = input("Password: ")

    print(Convert(username, password))
