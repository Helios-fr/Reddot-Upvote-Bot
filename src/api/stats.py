def get_verified(username, proxy=None):
    import requests
    import json

    if proxy != None:
        proxies = {
            "http": proxy,
            "https": proxy
        }



    url = f"https://www.reddit.com/user/{username}/about.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4464.5 Safari/537.36 Edg/91.0.866.0"
    }

    if proxy: r = requests.get(url, headers=headers, proxies=proxies)
    else: r = requests.get(url, headers=headers)

    data = json.loads(r.text)

    return data["data"]["has_verified_email"]

if __name__ == '__main__':
    print(get_verified("Necrownyx_"))