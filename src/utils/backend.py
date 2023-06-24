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
            mgr.get_api(account).submission(id=post_id).upvote()
            print(colorama.Fore.GREEN + f"Upvoted post {post_id} with account {account}")
        except Exception as e:
            print(colorama.Fore.RED + f"Failed to upvote post {post_id} with account {account} ({e})")
    
    input(colorama.Fore.GREEN + "Finished upvoting, press enter to continue")

def ConvertAccounts(mgr, file=None):
    from .convert import Convert
    import colorama

    if file == None: file = input(colorama.Fore.MAGENTA + "File to convert: ").strip()
    # read the file and split at :
    account_strings = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            account_strings.append(line.strip())


    # convert the accounts
    converted_account_strings = []
    for account in account_strings:
        converted_account_strings.append(Convert(account.split(":")[0], account.split(":")[1], logging=True))
    
    # write the converted accounts to a file
    with open('converted.txt', 'w') as f:
        for account in converted_account_strings:
            f.write(account + "\n")

def LoadAccounts(mgr, file=None):
    import colorama

    if file == None: file = input(colorama.Fore.MAGENTA + "File to load: ").strip()

    mgr.load(file, logging=True)

    input(colorama.Fore.GREEN + "Loaded accounts, press enter to continue")

def ViewAccounts(mgr):
    import colorama

    for username in mgr.accounts:
        print(colorama.Fore.GREEN + f"{username}:{mgr.accounts[username]['password']}:{mgr.accounts[username]['app_id']}:{mgr.accounts[username]['app_secret']}")

    input(colorama.Fore.GREEN + "Press enter to continue")

def Exit():
    import colorama
    import os

    print(colorama.Fore.GREEN + "Exiting..." + colorama.Fore.RESET)
    os._exit(0)

if __name__ == '__main__':
    # run main.py
    import os
    os.system('python src/main.py')