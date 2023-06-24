import praw
import colorama
import os
from utils import *

os.system('cls' if os.name == 'nt' else 'clear')

def main():
    Logo()
    choice = Options()

mgr = Manager('accounts.txt')

# id = KEKQZGzx776gn9JhwTfBtw
# secret = 	tMBzrgwQHg7XEegMBFXnqpx0h5jAGQ

# get the reddit instance
for account in mgr.accounts:
    reddit = mgr.get_api(account)

    # Fetch the post to upvote
    post = reddit.submission(id='14g1cwy')

    # Upvote the post
    post.upvote()

main()
