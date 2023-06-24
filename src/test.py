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
    'session': '9a9e01b9b9d62949ae67360d658c2775abd04907gAWVSQAAAAAAAABK4naWZEdB2SWWyb+v+X2UjAdfY3NyZnRflIwoOWJhNmI0ZmU0MzAzZTJjOGVlYzQ0NTZkZGJkODc2NjJiZTIxOWNhNJRzh5Qu',
    'recent_srs': 't5_34a0h^%^2Ct5_2qh22^%^2Ct5_2vm97^%^2C',
    'g_state': '{i_t:1687662245130,i_l:0}',
    'token_v2': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJleUpoYkdjaU9pSlNVekkxTmlJc0ltdHBaQ0k2SWxOSVFUSTFOanB6UzNkc01ubHNWMFZ0TWpWbWNYaHdUVTQwY1dZNE1YRTJPV0ZGZFdGeU1ucExNVWRoVkd4amRXTlpJaXdpZEhsd0lqb2lTbGRVSW4wLmV5SnpkV0lpT2lKMWMyVnlJaXdpWlhod0lqb3hOamczTmpZeU1qYzVMalExTlRFeE5Td2lhV0YwSWpveE5qZzNOVGMxT0RjNUxqUTFOVEV4TlN3aWFuUnBJam9pYUVsaFMycGFlVjlDVlRCeloydHNNMko2T0VWUFVVZFlSbEpyUVZsbklpd2lZMmxrSWpvaU9YUk1iMFl3YzI5d05WSktaMEVpTENKc2FXUWlPaUowTWw5bE1YYzJOWFU1Wm13aUxDSmhhV1FpT2lKME1sOWxNWGMyTlhVNVptd2lMQ0pzWTJFaU9qRTJPRGMxTnpVd05UTXpNek1zSW5OamNDSTZJbVZLZUd0clpFZFBPVU5CU1doa0xVWmhOVjluWmpWVlgyMDBNVlpQYTA1WGNGRkljMXBPTlMxWmVYVmtTbTUyVmtFdFpGUTBabEZmV1VreFZVbE5Ra2RDUVVacFUzUjVZbEZaUVd0dFJFOWFVV2RFVFU1RWNISnBVMUZSTkVWc2NVeEhPRWxSUW0xaWExRXhXbUZOWTJGWE0zZG5Ra3RwWTBVM1pWWkljR015YjJGVlltazFOR1IyTm5CNVRHcDVjRTlWWm13elRtcHRURmQ0VURsRVRXSnhNREp3VjA1YVZHMWpVakZ3V0ZGWFRGOXZXazg1VXpNNWRWVjZYMU5oTUZJNFQwdHhka2RDYjNsTldUaGZTRnBYVFZwcFIzWm1lRzV3Y2pCYVJqQjNjVGN6VEZGWGNHWTJja2MzT1d0WFZEQkVTelJmVW5oMmRrUmhWRWRZU21WdGNEZFNYM1F6TVZNdGFrRlFZMTlNT1U1eFFrZGhkamRZY25KMFYySjBYekZSTlZWNmFXcFNWMHA2TkU1Q2VUVmpkbXRsZG5kVVlrNWxiR1kwTTFwclRFdzBXbU5rVFdKbWJYTTJUMjVLZURSMFEyNDRabFZpUVVGRVgxOHhPRk15UmtVaUxDSnlZMmxrSWpvaVpuTnJaakZhUXpoZllrMU5UMVJsVkZGWlZEUnpaVFJDZUhNMGRrbHJOMjFDWlZOUE1XdFZlbkl6VlNJc0ltWnNieUk2TW4wLk1ia0xicmF1QllrdFdSMk1rUXlta0xiMEU2d2dGZHRRYU9EekFHMW5vT1AtWGVianFLSmt2cU5KZl9iZjJLVWZIZVhsUHp3YzZLZF94VnVvSmR0Z1NCWDZFQk5VWFBMb1o2VEUzc2hzdEhMdkZCZnV0SU84TDJJRnhnUmZnUDl0UHZUY2NHUjFLNVY2QkpBOXdzZEx3WFNqZTVveG9tMTBySEpaVG10eFBqaWt2Rm55MGlDd245Y3BlZVBkbnZ1bXdYbFJHMVJnRWdEQnQxRnl6Z3pYV1d2UlAzS0ZPb2lHeDlGTkhFQmVkRDdtZXlmelVIZFBkekF5WHRqSE95dzhiWmNwQ0V6OTQwVU54aWZLUEtkU2xNd1N1cXZsVUlyQUJVaUJfYXp1ZURiS01CVnFROWRHby1Sc2Fsbk1maTVPakwxeDI5ZElMYjlGV1o5YXhsd0d3QSIsImV4cCI6MTY4NzY2MjE1OSwibG9nZ2VkSW4iOnRydWUsInNjb3BlcyI6WyIqIiwiZW1haWwiLCJwaWkiXSwiY2lkIjoiOXRMb0Ywc29wNVJKZ0EifQ.2gRmdDrXR-5ByaDnVpcHQ3YvzWsp8R94TQiJ7djuQ28',
    'reddit_session': reddit_session_cookie,
    'pc': '8g',
    '177954_recentclicks2': 't3_14g1cwy',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://www.reddit.com/prefs/apps',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.reddit.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    # 'Cookie': 'loid=000000000e1w65u9fl.2.1687575053333.Z0FBQUFBQmtsbDFIWmFrWktPQTFLemFVTTlXNHhxMXE5YWJjQnd5ekZodTFoMkNkNUFacVdueXc2cGp2UWowUHRfeGZxMzNSU0Zhb2tsd09teXJQa29WVjJ1U2tqT1VBajBZMjhxSHdfMWFaS0d4S1g0MVJueTUtSmNqV0tuUDVGTG03NUR5cElMWEk; session_tracker=mjhroanamrgkrgrjrj.0.1687582435178.Z0FBQUFBQmtsbmJqRFdEOUV5UmxvTlhNNUFBRTFMUzFYUEVYVWJraHctWTNOUnZQZTdKQ0w2THVnZ1RMa1JFSGlnNzFPS2F6dXVwYmEwQ1VNVnJKRzJzTTFNYWZXY2Q0ZnphSG9uSmZVbnFXdXdRZ2ZMMmpYY2FNR2Q0T3p1Z3pjbjFVUlc5cHlQNVA; csv=2; edgebucket=ebgkziqvUc2bPUH5Ph; USER=eyJwcmVmcyI6eyJ0b3BDb250ZW50RGlzbWlzc2FsVGltZSI6MCwiZ2xvYmFsVGhlbWUiOiJSRURESVQiLCJuaWdodG1vZGUiOnRydWUsImNvbGxhcHNlZFRyYXlTZWN0aW9ucyI6eyJmYXZvcml0ZXMiOmZhbHNlLCJtdWx0aXMiOmZhbHNlLCJtb2RlcmF0aW5nIjpmYWxzZSwic3Vic2NyaXB0aW9ucyI6ZmFsc2UsInByb2ZpbGVzIjpmYWxzZX0sInRvcENvbnRlbnRUaW1lc0Rpc21pc3NlZCI6MH19; session=9a9e01b9b9d62949ae67360d658c2775abd04907gAWVSQAAAAAAAABK4naWZEdB2SWWyb+v+X2UjAdfY3NyZnRflIwoOWJhNmI0ZmU0MzAzZTJjOGVlYzQ0NTZkZGJkODc2NjJiZTIxOWNhNJRzh5Qu; recent_srs=t5_34a0h^%^2Ct5_2qh22^%^2Ct5_2vm97^%^2C; g_state={i_t:1687662245130,i_l:0}; token_v2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJleUpoYkdjaU9pSlNVekkxTmlJc0ltdHBaQ0k2SWxOSVFUSTFOanB6UzNkc01ubHNWMFZ0TWpWbWNYaHdUVTQwY1dZNE1YRTJPV0ZGZFdGeU1ucExNVWRoVkd4amRXTlpJaXdpZEhsd0lqb2lTbGRVSW4wLmV5SnpkV0lpT2lKMWMyVnlJaXdpWlhod0lqb3hOamczTmpZeU1qYzVMalExTlRFeE5Td2lhV0YwSWpveE5qZzNOVGMxT0RjNUxqUTFOVEV4TlN3aWFuUnBJam9pYUVsaFMycGFlVjlDVlRCeloydHNNMko2T0VWUFVVZFlSbEpyUVZsbklpd2lZMmxrSWpvaU9YUk1iMFl3YzI5d05WSktaMEVpTENKc2FXUWlPaUowTWw5bE1YYzJOWFU1Wm13aUxDSmhhV1FpT2lKME1sOWxNWGMyTlhVNVptd2lMQ0pzWTJFaU9qRTJPRGMxTnpVd05UTXpNek1zSW5OamNDSTZJbVZLZUd0clpFZFBPVU5CU1doa0xVWmhOVjluWmpWVlgyMDBNVlpQYTA1WGNGRkljMXBPTlMxWmVYVmtTbTUyVmtFdFpGUTBabEZmV1VreFZVbE5Ra2RDUVVacFUzUjVZbEZaUVd0dFJFOWFVV2RFVFU1RWNISnBVMUZSTkVWc2NVeEhPRWxSUW0xaWExRXhXbUZOWTJGWE0zZG5Ra3RwWTBVM1pWWkljR015YjJGVlltazFOR1IyTm5CNVRHcDVjRTlWWm13elRtcHRURmQ0VURsRVRXSnhNREp3VjA1YVZHMWpVakZ3V0ZGWFRGOXZXazg1VXpNNWRWVjZYMU5oTUZJNFQwdHhka2RDYjNsTldUaGZTRnBYVFZwcFIzWm1lRzV3Y2pCYVJqQjNjVGN6VEZGWGNHWTJja2MzT1d0WFZEQkVTelJmVW5oMmRrUmhWRWRZU21WdGNEZFNYM1F6TVZNdGFrRlFZMTlNT1U1eFFrZGhkamRZY25KMFYySjBYekZSTlZWNmFXcFNWMHA2TkU1Q2VUVmpkbXRsZG5kVVlrNWxiR1kwTTFwclRFdzBXbU5rVFdKbWJYTTJUMjVLZURSMFEyNDRabFZpUVVGRVgxOHhPRk15UmtVaUxDSnlZMmxrSWpvaVpuTnJaakZhUXpoZllrMU5UMVJsVkZGWlZEUnpaVFJDZUhNMGRrbHJOMjFDWlZOUE1XdFZlbkl6VlNJc0ltWnNieUk2TW4wLk1ia0xicmF1QllrdFdSMk1rUXlta0xiMEU2d2dGZHRRYU9EekFHMW5vT1AtWGVianFLSmt2cU5KZl9iZjJLVWZIZVhsUHp3YzZLZF94VnVvSmR0Z1NCWDZFQk5VWFBMb1o2VEUzc2hzdEhMdkZCZnV0SU84TDJJRnhnUmZnUDl0UHZUY2NHUjFLNVY2QkpBOXdzZEx3WFNqZTVveG9tMTBySEpaVG10eFBqaWt2Rm55MGlDd245Y3BlZVBkbnZ1bXdYbFJHMVJnRWdEQnQxRnl6Z3pYV1d2UlAzS0ZPb2lHeDlGTkhFQmVkRDdtZXlmelVIZFBkekF5WHRqSE95dzhiWmNwQ0V6OTQwVU54aWZLUEtkU2xNd1N1cXZsVUlyQUJVaUJfYXp1ZURiS01CVnFROWRHby1Sc2Fsbk1maTVPakwxeDI5ZElMYjlGV1o5YXhsd0d3QSIsImV4cCI6MTY4NzY2MjE1OSwibG9nZ2VkSW4iOnRydWUsInNjb3BlcyI6WyIqIiwiZW1haWwiLCJwaWkiXSwiY2lkIjoiOXRMb0Ywc29wNVJKZ0EifQ.2gRmdDrXR-5ByaDnVpcHQ3YvzWsp8R94TQiJ7djuQ28; reddit_session=39643932510273^%^2C2023-06-24T03^%^3A04^%^3A39^%^2C783518775a32ff33d62dfb82f1efad9b730a4d2a; pc=8g; 177954_recentclicks2=t3_14g1cwy',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = 'uh=c09atzx2sw68009547827fa3c1b4f22b2997939680c636a382&name=example&app_type=script&description=&about_url=example.com&redirect_uri=http://www.example.com&id=^%^23create-app&renderstyle=html'

response = requests.post('https://www.reddit.com/api/updateapp', cookies=cookies, headers=headers, data=data)

text = response.text

app_id = text.split('developed-app-')[1].split('"')[0]
print(f'App ID: {app_id}')

app_secret = text.split('class="prefright"&gt;')[1].split('&')[1]
print(f'App Secret: {app_secret}')