# base imports
import colorama
import os

# custom imports
from utils import *
from api import *

mgr = Manager('converted.txt')
mgr.proxies = ProxyManager()

# to load your proxies, use the following code:
# mgr.proxies.load_single("https://user:password@proxyip:port")

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
        LoadProxies(mgr)
    elif choice == "8":
        ViewProxies(mgr)
    elif choice == "9":
        ConvertAccounts(mgr)
    elif choice == "10":
        Exit()

while True:
    main()
