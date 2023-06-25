# base imports
import colorama
import os

# custom imports
from utils import *
from api import *

mgr = Manager('converted.txt')
mgr.proxies = ProxyManager()

# to load your proxies, use the following code:
mgr.proxies.load_single("http://Q1v6UZojLIqT:4HjzRVMhbj@176.9.154.70:25007")
# https://user:password@proxyip:port
# http://Q1v6UZojLIqT:4HjzRVMhbj:176.9.154.70:25007

def main():
    Clear()
    Logo()
    choice = Options()

    if choice == "1":
        Upvote(mgr)
    elif choice == "2":
        Downvote(mgr)
    elif choice == "3":
        Upvote(mgr, comment=True)
    elif choice == "4":
        Downvote(mgr, comment=True)
    elif choice == "5":
        LoadAccounts(mgr)
    elif choice == "6":
        ViewAccounts(mgr)
    elif choice == "7":
        ConvertAccounts(mgr)
    elif choice == "8":
        Exit()

while True:
    main()
