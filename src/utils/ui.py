def Clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def Logo():
    import colorama
    colorama.init()
    print(colorama.Fore.CYAN + "  _    _                 _       ____        _    ")
    print(colorama.Fore.CYAN + " | |  | |               | |     |  _ \      | |   ")
    print(colorama.Fore.CYAN + " | |  | |_ ____   _____ | |_ ___| |_) | ___ | |_  ")
    print(colorama.Fore.CYAN + " | |  | | '_ \ \ / / _ \| __/ _ \  _ < / _ \| __| ")
    print(colorama.Fore.CYAN + " | |__| | |_) \ V / (_) | ||  __/ |_) | (_) | |_  ")
    print(colorama.Fore.CYAN + "  \____/| .__/ \_/ \___/ \__\___|____/ \___/ \__| ")
    print(colorama.Fore.CYAN + "        | |                                       ")
    print(colorama.Fore.CYAN + "        |_|  By Nyx https://pastebin.com/sJAzRdyK ")
    print()

def Options():
    import colorama
    import os

    colorama.init()
    print(colorama.Fore.CYAN + "1. Upvote a post     2. Downvote a post")
    print(colorama.Fore.CYAN + "3. Upvote a comment  4. Downvote a comment")
    print(colorama.Fore.CYAN + "5. Load accounts     6. View accounts")
    print(colorama.Fore.CYAN + "7. Convert accounts  8. Exit")
    print()

    try:
        choice = input(colorama.Fore.MAGENTA + "Choice: ").strip()
    except EOFError:
        print(colorama.Fore.RED + "Please use the docker command to run the script found on the github page.")
        os._exit(0)

    if choice not in ("1", "2", "3", "4", "5", "6", "7", "8"):
        Clear()
        Logo()
        print(colorama.Fore.RED + f"Invalid choice! ({choice})")
        Options()

    return choice



if __name__ == '__main__':
    Logo()
    Options()