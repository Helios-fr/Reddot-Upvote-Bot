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
    print(colorama.Fore.CYAN + "1. Upvote a post")
    print(colorama.Fore.CYAN + "2. Load accounts")
    print(colorama.Fore.CYAN + "3. View accounts")
    print(colorama.Fore.CYAN + "4. Exit")
    choice = input(colorama.Fore.MAGENTA + "Choice: ")
    if choice != "1" and choice != "2" and choice != "3" and choice != "4":
        # clear the screen on linux and windows
        os.system('cls' if os.name == 'nt' else 'clear')
        Logo()
        print(colorama.Fore.RED + "Invalid choice!")
        Options()

    return choice


if __name__ == '__main__':
    Logo()
    Options()