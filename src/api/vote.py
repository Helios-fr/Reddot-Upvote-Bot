def upvote_post(user, post_id, proxy=None):
    import requests
    from .auth import get_access_token

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
        'Authorization': f'Bearer {get_access_token(user, proxy)}',
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

    proxies = {'http': proxy, 'https': proxy} if proxy else None

    response = requests.post('https://oauth.reddit.com/api/vote', params=params, headers=headers, data=data, proxies=proxies)

    if response.status_code == 401:
        raise Exception("403 Forbidden")


def downvote_post(user, post_id, proxy=None):
    import requests
    from .auth import get_access_token

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
        'Authorization': f'Bearer {get_access_token(user, proxy)}',
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

    proxies = {'http': proxy, 'https': proxy} if proxy else None

    response = requests.post('https://oauth.reddit.com/api/vote', params=params, headers=headers, data=data, proxies=proxies)

    if response.status_code == 401:
        raise Exception("403 Forbidden")
