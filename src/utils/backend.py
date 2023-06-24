def Upvote(mgr, post_id=None, amount=None):
    import random
    import colorama
    # ask user for the post id
    if post_id == None: post_id = input(colorama.Fore.MAGENTA + "Post ID: ").strip()
    # ask user for amount of accounts out of the loaded accounts to use
    if amount == None:
        amount = 1000000000
        while int(amount) > len(mgr.accounts):
            amount = input(colorama.Fore.MAGENTA + f"Amount of accounts to use (Max {len(mgr.accounts)}): ").strip()
            if int(amount) > len(mgr.accounts):
                print(colorama.Fore.RED + f"Amount is higher than the amount of accounts loaded ({len(mgr.accounts)})")
    
    # pick amount random accounts from the loaded accounts
    accounts = random.sample(list(mgr.accounts), int(amount))

    # loop through the accounts and upvote the post
    for account in accounts:
        try:
            mgr.get_api(account).submission(post_id).upvote()
            print(colorama.Fore.GREEN + f"Upvoted post {post_id} with account {account}")
        except Exception as e:
            print(colorama.Fore.RED + f"Failed to upvote post {post_id} with account {account} ({e})")


        

def LoadAccounts(mgr):
    pass

def ViewAccounts(mgr):
    pass

def Exit():
    pass

if __name__ == '__main__':
    # run main.py
    import os
    os.system('python src/main.py')