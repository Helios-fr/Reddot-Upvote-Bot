def upvote_post(user, post_id):
    import requests

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://www.reddit.com/',
        'x-reddit-loid': user.cookie['loid'],
        'x-reddit-session': user.cookie['reddit_session'],
        'Origin': 'https://www.reddit.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'DNT': '1',
        'Sec-GPC': '1',
        'Authorization': f'Bearer {get_access_token(user)}',
        'Connection': 'keep-alive',
    }

    params = {
        'redditWebClient': 'desktop2x',
        'app': 'desktop2x-client-production',
        'raw_json': '1',
        'gilding_detail': '1',
    }

    data = {
        'id': post_id,
        'dir': '1',
        'api_type': 'json',
    }

    response = requests.post('https://oauth.reddit.com/api/vote', params=params, headers=headers, data=data)

def downvote_post(user, post_id):
    import requests

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://www.reddit.com/',
        'x-reddit-loid': user.cookie['loid'],
        'x-reddit-session': user.cookie['reddit_session'],
        'Origin': 'https://www.reddit.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'DNT': '1',
        'Sec-GPC': '1',
        'Authorization': f'Bearer {get_access_token(user)}',
        'Connection': 'keep-alive',
    }

    params = {
        'redditWebClient': 'desktop2x',
        'app': 'desktop2x-client-production',
        'raw_json': '1',
        'gilding_detail': '1',
    }

    data = {
        'id': post_id,
        'dir': '-1',
        'api_type': 'json',
    }

    response = requests.post('https://oauth.reddit.com/api/vote', params=params, headers=headers, data=data)