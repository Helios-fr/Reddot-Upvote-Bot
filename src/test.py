import praw
from utils import manager

mgr = manager.Manager('converted.txt')

for account in mgr.accounts:
    print(f"Logging into {account}...")
    print(f"Username: {mgr.accounts[account]['username']}")
    print(f"Password: {mgr.accounts[account]['password']}")
    print(f"App ID: {mgr.accounts[account]['app_id']}")
    print(f"App Secret: {mgr.accounts[account]['app_secret']}")


    reddit = praw.Reddit(
        client_id=mgr.accounts[account]['app_id'],
        client_secret=mgr.accounts[account]['app_secret'],
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
        username=mgr.accounts[account]['username'],
        password=mgr.accounts[account]['password']
    )

    # get the ost by id
    post = reddit.submission(id='14gbl23')

    post.upvote()

