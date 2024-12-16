import requests
import time
import os
import shutil
from colorama import Fore, Style, init
from itertools import cycle

init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_ascii_art_with_animation():
    art = r"""
                                            (                                      
                                            )\ )                                   
        (       (  (            )    )     ( (()/(    (      )               (  (    
        )\ (   ))\ )(   (    ( /(   (     ))\ /(_)) ( )(  ( /( `  )  `  )   ))\ )(   
    _ ((_))\ /((_|()\  )\ ) )(_))  )\  '/((_|_))   )(()\ )(_))/(/(  /(/(  /((_|()\  
    | | | ((_|_))  ((_)_(_/(((_)_ _((_))(_)) / __| ((_|(_|(_)_((_)_\((_)_\(_))  ((_) 
    | |_| (_-< -_)| '_| ' \)) _` | '  \() -_)\__ \/ _| '_/ _` | '_ \) '_ \) -_)| '_| 
    \___//__|___||_| |_||_|\__,_|_|_|_|\___||___/\__|_| \__,_| .__/| .__/\___||_|   
                                                            |_|   |_|              
    """
    console_width = shutil.get_terminal_size().columns
    colors = cycle([Fore.RED, Fore.LIGHTRED_EX])

    for _ in range(10):
        clear_console()
        color = next(colors)
        for line in art.splitlines():
            print(color + line.center(console_width))
        time.sleep(0.2)

    print(Fore.RED + "Made by Kyra".center(console_width))

def interactive_menu():
    while True:
        clear_console()
        print(Fore.RED + "Main Menu".center(shutil.get_terminal_size().columns, "-"))
        print(Fore.LIGHTRED_EX + "[1] Start Scraper")
        print(Fore.LIGHTRED_EX + "[2] Exit")
        choice = input(Fore.RED + "Choose an option: ")
        if choice == "1":
            return
        elif choice == "2":
            clear_console()
            print(Fore.RED + "Thanks for using my tool!".center(shutil.get_terminal_size().columns))
            time.sleep(2)
            exit()
        else:
            print(Fore.LIGHTRED_EX + "Invalid option!".center(shutil.get_terminal_size().columns))
            time.sleep(2)

def progress_bar(current, total, bar_length=40):
    percent = int(current / total * 100)
    bar = ('█' * int(bar_length * percent / 100)).ljust(bar_length)
    print(Fore.LIGHTRED_EX + f"[{bar}] {percent}% Complete", end="\r")

def get_scratch_usernames(seed_username, max_users=100):
    visited = set()
    to_visit = [seed_username]
    usernames = []

    while to_visit and len(usernames) < max_users:
        current_user = to_visit.pop(0)
        if current_user in visited:
            continue

        clear_console()
        print(Fore.LIGHTRED_EX + "Scraping Usernames")
        progress_bar(len(usernames) + 1, max_users)
        print(Fore.LIGHTRED_EX + f"\nCurrently scraping: {current_user}")

        url = f"https://api.scratch.mit.edu/users/{current_user}/followers"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            for user in data:
                username = user['username']
                if username not in visited and username not in to_visit:
                    to_visit.append(username)
                    usernames.append(username)

        visited.add(current_user)
        time.sleep(0.5)

    return usernames

def run_scraper():
    seed_username = input(Fore.LIGHTRED_EX + "Enter the starting username: ")
    max_users = int(input(Fore.LIGHTRED_EX + "Enter the maximum number of usernames to scrape: "))
    usernames = get_scratch_usernames(seed_username, max_users=max_users)

    with open("scratch_usernames.txt", "w") as f:
        for username in usernames:
            f.write(username + "\n")

    clear_console()
    print(Fore.LIGHTGREEN_EX + f"Scraping complete! {len(usernames)} usernames saved in 'scratch_usernames.txt'.")
    time.sleep(2)

def main():
    clear_console()
    display_ascii_art_with_animation()
    time.sleep(1)
    interactive_menu()
    run_scraper()

if __name__ == "__main__":
    main()
