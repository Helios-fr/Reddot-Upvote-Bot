import requests

'''
# GET request to retrieve CSRF token
response = requests.get("https://accounts.reddit.com", headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Pragma": "no-cache",
    "Accept": "*/*"
})
csrf_token = response.text.split('"tracker_secret": "')[1].split('"')[0]

print("CSRF token: " + csrf_token)
'''


# username: 177954
# password: 4P."f7ybqKrStjE

# https://www.reddit.com/r/anime/comments/14gx4rj/konosuba_darkness_ideal_man/

import requests

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


cookies = {
    'loid': loid_cookie,
    'session_tracker': session_tracker_cookie,
    'csv': '2',
    'edgebucket': edgebucket_cookie,
    'USER': username,
    'token_v2': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJleUpoYkdjaU9pSlNVekkxTmlJc0ltdHBaQ0k2SWxOSVFUSTFOanB6UzNkc01ubHNWMFZ0TWpWbWNYaHdUVTQwY1dZNE1YRTJPV0ZGZFdGeU1ucExNVWRoVkd4amRXTlpJaXdpZEhsd0lqb2lTbGRVSW4wLmV5SnpkV0lpT2lKMWMyVnlJaXdpWlhod0lqb3hOamczTmpZeU1qYzVMalExTlRFeE5Td2lhV0YwSWpveE5qZzNOVGMxT0RjNUxqUTFOVEV4TlN3aWFuUnBJam9pYUVsaFMycGFlVjlDVlRCeloydHNNMko2T0VWUFVVZFlSbEpyUVZsbklpd2lZMmxrSWpvaU9YUk1iMFl3YzI5d05WSktaMEVpTENKc2FXUWlPaUowTWw5bE1YYzJOWFU1Wm13aUxDSmhhV1FpT2lKME1sOWxNWGMyTlhVNVptd2lMQ0pzWTJFaU9qRTJPRGMxTnpVd05UTXpNek1zSW5OamNDSTZJbVZLZUd0clpFZFBPVU5CU1doa0xVWmhOVjluWmpWVlgyMDBNVlpQYTA1WGNGRkljMXBPTlMxWmVYVmtTbTUyVmtFdFpGUTBabEZmV1VreFZVbE5Ra2RDUVVacFUzUjVZbEZaUVd0dFJFOWFVV2RFVFU1RWNISnBVMUZSTkVWc2NVeEhPRWxSUW0xaWExRXhXbUZOWTJGWE0zZG5Ra3RwWTBVM1pWWkljR015YjJGVlltazFOR1IyTm5CNVRHcDVjRTlWWm13elRtcHRURmQ0VURsRVRXSnhNREp3VjA1YVZHMWpVakZ3V0ZGWFRGOXZXazg1VXpNNWRWVjZYMU5oTUZJNFQwdHhka2RDYjNsTldUaGZTRnBYVFZwcFIzWm1lRzV3Y2pCYVJqQjNjVGN6VEZGWGNHWTJja2MzT1d0WFZEQkVTelJmVW5oMmRrUmhWRWRZU21WdGNEZFNYM1F6TVZNdGFrRlFZMTlNT1U1eFFrZGhkamRZY25KMFYySjBYekZSTlZWNmFXcFNWMHA2TkU1Q2VUVmpkbXRsZG5kVVlrNWxiR1kwTTFwclRFdzBXbU5rVFdKbWJYTTJUMjVLZURSMFEyNDRabFZpUVVGRVgxOHhPRk15UmtVaUxDSnlZMmxrSWpvaVpuTnJaakZhUXpoZllrMU5UMVJsVkZGWlZEUnpaVFJDZUhNMGRrbHJOMjFDWlZOUE1XdFZlbkl6VlNJc0ltWnNieUk2TW4wLk1ia0xicmF1QllrdFdSMk1rUXlta0xiMEU2d2dGZHRRYU9EekFHMW5vT1AtWGVianFLSmt2cU5KZl9iZjJLVWZIZVhsUHp3YzZLZF94VnVvSmR0Z1NCWDZFQk5VWFBMb1o2VEUzc2hzdEhMdkZCZnV0SU84TDJJRnhnUmZnUDl0UHZUY2NHUjFLNVY2QkpBOXdzZEx3WFNqZTVveG9tMTBySEpaVG10eFBqaWt2Rm55MGlDd245Y3BlZVBkbnZ1bXdYbFJHMVJnRWdEQnQxRnl6Z3pYV1d2UlAzS0ZPb2lHeDlGTkhFQmVkRDdtZXlmelVIZFBkekF5WHRqSE95dzhiWmNwQ0V6OTQwVU54aWZLUEtkU2xNd1N1cXZsVUlyQUJVaUJfYXp1ZURiS01CVnFROWRHby1Sc2Fsbk1maTVPakwxeDI5ZElMYjlGV1o5YXhsd0d3QSIsImV4cCI6MTY4NzY2MjE1OSwibG9nZ2VkSW4iOnRydWUsInNjb3BlcyI6WyIqIiwiZW1haWwiLCJwaWkiXSwiY2lkIjoiOXRMb0Ywc29wNVJKZ0EifQ.2gRmdDrXR-5ByaDnVpcHQ3YvzWsp8R94TQiJ7djuQ28',
    'reddit_session': reddit_session_cookie,
    'pc': '8g',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://old.reddit.com/',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://old.reddit.com',
    'Connection': 'keep-alive',
    'Cookie': f'loid={loid_cookie}; session_tracker={session_tracker_cookie}; csv=2; edgebucket={edgebucket_cookie}; USER=eyJwcmVmcyI6eyJ0b3BDb250ZW50RGlzbWlzc2FsVGltZSI6MCwiZ2xvYmFsVGhlbWUiOiJSRURESVQiLCJuaWdodG1vZGUiOnRydWUsImNvbGxhcHNlZFRyYXlTZWN0aW9ucyI6eyJmYXZvcml0ZXMiOmZhbHNlLCJtdWx0aXMiOmZhbHNlLCJtb2RlcmF0aW5nIjpmYWxzZSwic3Vic2NyaXB0aW9ucyI6ZmFsc2UsInByb2ZpbGVzIjpmYWxzZX0sInRvcENvbnRlbnRUaW1lc0Rpc21pc3NlZCI6MH19; recent_srs=t5_2vm97^%^2C; token_v2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJleUpoYkdjaU9pSlNVekkxTmlJc0ltdHBaQ0k2SWxOSVFUSTFOanB6UzNkc01ubHNWMFZ0TWpWbWNYaHdUVTQwY1dZNE1YRTJPV0ZGZFdGeU1ucExNVWRoVkd4amRXTlpJaXdpZEhsd0lqb2lTbGRVSW4wLmV5SnpkV0lpT2lKMWMyVnlJaXdpWlhod0lqb3hOamczTmpZeU1qYzVMalExTlRFeE5Td2lhV0YwSWpveE5qZzNOVGMxT0RjNUxqUTFOVEV4TlN3aWFuUnBJam9pYUVsaFMycGFlVjlDVlRCeloydHNNMko2T0VWUFVVZFlSbEpyUVZsbklpd2lZMmxrSWpvaU9YUk1iMFl3YzI5d05WSktaMEVpTENKc2FXUWlPaUowTWw5bE1YYzJOWFU1Wm13aUxDSmhhV1FpT2lKME1sOWxNWGMyTlhVNVptd2lMQ0pzWTJFaU9qRTJPRGMxTnpVd05UTXpNek1zSW5OamNDSTZJbVZLZUd0clpFZFBPVU5CU1doa0xVWmhOVjluWmpWVlgyMDBNVlpQYTA1WGNGRkljMXBPTlMxWmVYVmtTbTUyVmtFdFpGUTBabEZmV1VreFZVbE5Ra2RDUVVacFUzUjVZbEZaUVd0dFJFOWFVV2RFVFU1RWNISnBVMUZSTkVWc2NVeEhPRWxSUW0xaWExRXhXbUZOWTJGWE0zZG5Ra3RwWTBVM1pWWkljR015YjJGVlltazFOR1IyTm5CNVRHcDVjRTlWWm13elRtcHRURmQ0VURsRVRXSnhNREp3VjA1YVZHMWpVakZ3V0ZGWFRGOXZXazg1VXpNNWRWVjZYMU5oTUZJNFQwdHhka2RDYjNsTldUaGZTRnBYVFZwcFIzWm1lRzV3Y2pCYVJqQjNjVGN6VEZGWGNHWTJja2MzT1d0WFZEQkVTelJmVW5oMmRrUmhWRWRZU21WdGNEZFNYM1F6TVZNdGFrRlFZMTlNT1U1eFFrZGhkamRZY25KMFYySjBYekZSTlZWNmFXcFNWMHA2TkU1Q2VUVmpkbXRsZG5kVVlrNWxiR1kwTTFwclRFdzBXbU5rVFdKbWJYTTJUMjVLZURSMFEyNDRabFZpUVVGRVgxOHhPRk15UmtVaUxDSnlZMmxrSWpvaVpuTnJaakZhUXpoZllrMU5UMVJsVkZGWlZEUnpaVFJDZUhNMGRrbHJOMjFDWlZOUE1XdFZlbkl6VlNJc0ltWnNieUk2TW4wLk1ia0xicmF1QllrdFdSMk1rUXlta0xiMEU2d2dGZHRRYU9EekFHMW5vT1AtWGVianFLSmt2cU5KZl9iZjJLVWZIZVhsUHp3YzZLZF94VnVvSmR0Z1NCWDZFQk5VWFBMb1o2VEUzc2hzdEhMdkZCZnV0SU84TDJJRnhnUmZnUDl0UHZUY2NHUjFLNVY2QkpBOXdzZEx3WFNqZTVveG9tMTBySEpaVG10eFBqaWt2Rm55MGlDd245Y3BlZVBkbnZ1bXdYbFJHMVJnRWdEQnQxRnl6Z3pYV1d2UlAzS0ZPb2lHeDlGTkhFQmVkRDdtZXlmelVIZFBkekF5WHRqSE95dzhiWmNwQ0V6OTQwVU54aWZLUEtkU2xNd1N1cXZsVUlyQUJVaUJfYXp1ZURiS01CVnFROWRHby1Sc2Fsbk1maTVPakwxeDI5ZElMYjlGV1o5YXhsd0d3QSIsImV4cCI6MTY4NzY2MjE1OSwibG9nZ2VkSW4iOnRydWUsInNjb3BlcyI6WyIqIiwiZW1haWwiLCJwaWkiXSwiY2lkIjoiOXRMb0Ywc29wNVJKZ0EifQ.2gRmdDrXR-5ByaDnVpcHQ3YvzWsp8R94TQiJ7djuQ28; reddit_session={reddit_session_cookie}; pc=8g',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'DNT': '1',
    'Sec-GPC': '1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'dir': '-1',
    'id': 't3_14gx4rj',
    'sr': 'anime',
}

data = 'id=t3_14gx4rj&dir=-1&vh=AG0Pu9uYgVJCwC0Duz0iArx0bCA0envanggNZBsyBYDYM4oHYP^%^2FbWNN8QuJ^%^2Ff4wzvHI7z07dliNuN8HnjbnHvzrbtZPJFUKd1OGbOcFfiA^%^2FURjLCkOujjaJ31MWOf45Y8vl6ycQ1Z5IRmr^%^2FX^%^2Fs0wYd8QXeSZPzR0frPx94rOITc^%^3D&isTrusted=true&vote_event_data=^%^7B^%^22page_type^%^22^%^3A^%^22listing^%^22^%^2C^%^22sort^%^22^%^3A^%^22best^%^22^%^7D&rank=1&uh=6vcpxy7npcf936d9b13fe67c04cd2b2d71bc3fa081d444038d&renderstyle=html'

response = requests.post('https://old.reddit.com/api/vote', params=params, cookies=cookies, headers=headers, data=data)

print(response.status_code)
print(response.text)