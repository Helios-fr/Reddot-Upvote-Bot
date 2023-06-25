def Upvote(mgr, post_ids=None, amount=None, comment=False):
    import random
    import colorama
    import time

    from api import upvote_post
    # ask user for the post id
    if post_ids == None: post_ids = input(colorama.Fore.MAGENTA + "Post ID's (separated by ', '): ").strip()
    post_ids = post_ids.split(', ')
    new = []
    for post_id in post_ids:
        if comment == False:
            if post_id.startswith('t3_'): post_id = post_id[3:]
            post_id = 't3_' + post_id
            new.append(post_id)
        else:
            if post_id.startswith('t1_'): post_id = post_id[3:]
            post_id = 't1_' + post_id
            new.append(post_id)
    post_ids = new
    
    # ask user for amount of accounts out of the loaded accounts to use
    if amount == None:
        amount = 1000000000
        while int(amount) > len(mgr.accounts):
            amount = input(colorama.Fore.MAGENTA + f"Amount of accounts to use (Max {len(mgr.accounts)}): ").strip()
            if int(amount) > len(mgr.accounts):
                print(colorama.Fore.RED + f"Amount is higher than the amount of accounts loaded ({len(mgr.accounts)})")
    
    # pick amount random accounts from the loaded accounts
    all_accounts = list(mgr.accounts)
    accounts = random.sample(all_accounts, int(amount))

    # remove the accounts from the list of all accounts
    all_accounts = [account for account in all_accounts if account not in accounts]

    # ask user for the delay between upvotes
    delay = input(colorama.Fore.MAGENTA + "Delay between upvotes (in seconds): ").strip()

    # loop through the accounts and upvote the post
    for account in accounts:
        user = mgr.get_api(account)
        for post_id in post_ids:
            try:
                upvote_post(user, post_id, proxy=mgr.proxies.random())
                print(colorama.Fore.GREEN + f"Upvoted post {post_id} with account {account}")
            except Exception as e:
                if "401" in str(e):
                    print(colorama.Fore.RED + f"Failed to upvote post {post_id} with account {account} (Account Suspended)")
                    accounts.append(all_accounts.pop(0)) 
                else:
                    print(colorama.Fore.RED + f"Failed to upvote post {post_id} with account {account} ({e})")
        time.sleep(int(delay))
    
    input(colorama.Fore.GREEN + "Finished upvoting, press enter to continue")

def Downvote(mgr, post_ids=None, amount=None, comment=False):
    import random
    import colorama
    import time

    from api import downvote_post
    # ask user for the post id
    if post_ids == None: post_ids = input(colorama.Fore.MAGENTA + "Post ID's (separated by ', '): ").strip()
    post_ids = post_ids.split(', ')
    new = []
    for post_id in post_ids:
        if comment == False:
            if post_id.startswith('t3_'): post_id = post_id[3:]
            post_id = 't3_' + post_id
            new.append(post_id)
        else:
            if post_id.startswith('t1_'): post_id = post_id[3:]
            post_id = 't1_' + post_id
            new.append(post_id)
    post_ids = new

    # ask user for amount of accounts out of the loaded accounts to use
    if amount == None:
        amount = 1000000000
        while int(amount) > len(mgr.accounts):
            amount = input(colorama.Fore.MAGENTA + f"Amount of accounts to use (Max {len(mgr.accounts)}): ").strip()
            if int(amount) > len(mgr.accounts):
                print(colorama.Fore.RED + f"Amount is higher than the amount of accounts loaded ({len(mgr.accounts)})")
    
    # pick amount random accounts from the loaded accounts
    all_accounts = list(mgr.accounts)
    accounts = random.sample(all_accounts, int(amount))

    # remove the accounts from the list of all accounts
    all_accounts = [account for account in all_accounts if account not in accounts]

    # ask user for the delay between upvotes
    delay = input(colorama.Fore.MAGENTA + "Delay between downvotes (in seconds): ").strip()

    # loop through the accounts and upvote the post
    for account in accounts:
        user = mgr.get_api(account, proxy=mgr.proxies.random())
        for post_id in post_ids:
            try:
                downvote_post(user, post_id, proxy=mgr.proxies.random())
                print(colorama.Fore.GREEN + f"Downvoted post {post_id} with account {account}")
            except Exception as e:
                if "401" in str(e):
                    print(colorama.Fore.RED + f"Failed to downvote post {post_id} with account {account} (Account Suspended)")
                    accounts.append(all_accounts.pop(0)) 
                else:
                    print(colorama.Fore.RED + f"Failed to downvote post {post_id} with account {account} ({e})")
        time.sleep(int(delay))
    
    input(colorama.Fore.GREEN + "Finished downvoting, press enter to continue")


def ConvertAccounts(mgr, file=None):
    import threading
    from queue import Queue
    from .convert import Convert
    import colorama

    if file is None:
        file = input(colorama.Fore.MAGENTA + "File to convert: ").strip()

    # Read the file and split at ":"
    account_strings = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            account_strings.append(line.strip())

    # Define a function to convert an individual account in a thread
    def convert_account(account, results_queue):
        try:
            converted_account = Convert(account.split(":")[0], account.split(":")[1], logging=True, proxy=mgr.proxies.random())
        except Exception as e:
            converted_account = f"{account} - {e}"
        results_queue.put(converted_account)

    # Create a queue to store the results
    results_queue = Queue()

    # Create a list to store the thread objects
    threads = []

    # Convert the accounts using threads
    for account in account_strings:
        thread = threading.Thread(target=convert_account, args=(account, results_queue))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Get the converted accounts from the queue
    converted_account_strings = []
    while not results_queue.empty():
        converted_account = results_queue.get()
        converted_account_strings.append(converted_account)

    # Write the converted accounts to a file
    with open('converted.txt', 'w') as f:
        for account in converted_account_strings:
            f.write(account + "\n")



def LoadAccounts(mgr, file=None):
    import colorama

    if file == None: file = input(colorama.Fore.MAGENTA + "File to load: ").strip()

    mgr.load(file, logging=True)

    input(colorama.Fore.GREEN + "Loaded accounts, press enter to continue")

def ViewAccounts(mgr, slow=None):
    import colorama
    import threading

    if slow == None: slow = input(colorama.Fore.MAGENTA + "Get the statistics of the user's upvotes/downvotes? (slow) (y/n): ").strip().lower() == "y"

    def check_account(username):
        api = mgr.get_api(username)
        
        upvotes = 0
        downvotes = 0
        for vote in api.user.me().upvoted():
            upvotes += 1
        for vote in api.user.me().downvoted():
            downvotes += 1
        
        print(colorama.Fore.CYAN + f"Username: {username} | Upvotes: {upvotes} | Downvotes: {downvotes}")
    
    if slow:
        threads = []
        for username in mgr.accounts:
            thread = threading.Thread(target=check_account, args=(username,))
            thread.start()
            threads.append(thread)
        
        # await all threads to finish
        for thread in threads:
            thread.join()
    else:
        for username in mgr.accounts:
            print(colorama.Fore.CYAN + f"Username: {username}")

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