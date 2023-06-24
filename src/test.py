import requests
import base64

# POST request to login with username and password
username = "177954"
password = '4P."f7ybqKrStjE'
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

print(response.text)

cookies = response.cookies
edgebucket_cookie = cookies.get('edgebucket')
loid_cookie = cookies.get('loid')
reddit_session_cookie = cookies.get('reddit_session')
session_tracker_cookie = cookies.get('session_tracker')

connection = response.headers.get('Connection')
content_length = response.headers.get('Content-Length')
x_ua_compatible = response.headers.get('x-ua-compatible')
access_control_allow_origin = response.headers.get('access-control-allow-origin')
access_control_expose_headers = response.headers.get('access-control-expose-headers')
access_control_allow_methods = response.headers.get('access-control-allow-methods')
access_control_allow_credentials = response.headers.get('access-control-allow-credentials')
access_control_allow_headers = response.headers.get('access-control-allow-headers')
content_type = response.headers.get('content-type')
x_frame_options = response.headers.get('x-frame-options')
expires = response.headers.get('expires')
cache_control = response.headers.get('cache-control')
set_cookie = response.headers.get('set-cookie')
strict_transport_security = response.headers.get('strict-transport-security')
x_moose = response.headers.get('x-moose')
accept_ranges = response.headers.get('Accept-Ranges')
date = response.headers.get('Date')
via = response.headers.get('Via')
server = response.headers.get('Server')
report_to = response.headers.get('Report-To')
nel = response.headers.get('NEL')

# user token is a json object base64 encoded
user_raw = '{"prefs":{"topContentDismissalTime":0,"globalTheme":"REDDIT","nightmode":true,"collapsedTraySections":{"favorites":false,"multis":false,"moderating":false,"subscriptions":false,"profiles":false},"topContentTimesDismissed":0}}'
user_token = base64.b64encode(user_raw.encode('utf-8')).decode('utf-8')



cookies = {
    'loid': loid_cookie,
    'session_tracker': session_tracker_cookie,
    'csv': '2',
    'edgebucket': edgebucket_cookie,
    'USER': user_token,
    'reddit_session': reddit_session_cookie,
    'pc': '8g',
}

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

data = 'uh=c09atzx2sw68009547827fa3c1b4f22b2997939680c636a382&name=example&app_type=script&description=&about_url=example.com&redirect_uri=http://www.example.com&id=^%^23create-app&renderstyle=html'

response = requests.post('https://www.reddit.com/api/updateapp', cookies=cookies, headers=headers, data=data)

text = response.text

# only the first 1XJL_fyref3AVSd6y50eAQ characters
app_id = text.split('developed-app-')[1].split('"')[0][:22]
print(f'App ID: {app_id}')

app_secret = text.split(r'secret&lt;/th&gt;&lt;td class=\"prefright\"&gt;')[1].split("&")[0]
print(f'App Secret: {app_secret}')