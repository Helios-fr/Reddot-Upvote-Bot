import praw
import colorama
import os
from utils import *

mgr = Manager('../converted.txt')

def main():
    Clear()
    Logo()
    choice = Options()

    if choice == "1":
        Upvote(mgr)
    elif choice == "2":
        ConvertAccounts(mgr)
    elif choice == "3":
        LoadAccounts(mgr)
    elif choice == "4":
        ViewAccounts(mgr)
    elif choice == "5":
        Exit()

while True:
    main()
