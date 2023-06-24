import praw
import colorama
import os
from utils import *

os.system('cls' if os.name == 'nt' else 'clear')

mgr = Manager('accounts.txt')

def main():
    Logo()
    choice = Options()

    if choice == "1":
        Upvote(mgr)
    elif choice == "2":
        LoadAccounts(mgr)
    elif choice == "3":
        ViewAccounts(mgr)
    elif choice == "4":
        Exit()

main()
