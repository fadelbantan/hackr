#!/usr/bin/env python3

import sys, time, os
from pyfiglet import Figlet
from features.social_media import socials_cmd
from features.website import website_cmd


# Main Header using Figlet library
def print_header(name="HACKR"):
    print("\n")
    f = Figlet(font="ansi_shadow")
    print(f.renderText(" hackr"))

# typewriter used for script lines
def typewriter(text, speed=0.02):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")
    sys.stdout.flush()

# Help menu
def print_help():
    help_text = f"""
\033[1mhackr\033[0m
terminal hacker simulator
A fun feel of hacking like in the movies, completely harmless and very fun!

\033[1mCOMMANDS\033[0m
socials, s <username> : Simulate enumerating public social links for <username>.
                        If <username> is omitted, you will be prompted to enter one.
website, w <target>   : Simulate web-app hacking flow against <target> (e.g. example.com).
                        If <target> is omitted, you will be prompted to enter one.                        
help                  : Show this help menu.
exit, quit, q         : Exit the program.
"""
    print(help_text)

# Read-Eval-Print Loop
def repl(username):

    prompt = f"hackr@{username} $ "
    print()
    while True:
        line = input(prompt).strip() # .strip() removes whitespace
        # If enter is pressed without any input, start loop again
        if not line:
            continue
        
        # Split input in separate words in a list
        cmd_parts = line.split()
        cmd = cmd_parts[0].lower()

        if cmd == 'help':
            print_help()
        elif cmd in ('quit', 'exit', 'q'):
            print("Exiting hackr. Goodbye.")
            break
        elif cmd == "socials" or cmd == "s":
            arg = cmd_parts[1] if len(cmd_parts) > 1 else None
            if arg is not None and len(arg) < 3:
                print("Error: username must be at least 3 characters.")
                continue
            result = socials_cmd(arg)
            if result == "exit":
                print("Exiting hackr. Goodbye.")
                break
            # returned to menu
            os.system("cls" if sys.platform.startswith("win") else "clear")
            print_header(username)
            print(f"Welcome back {username}, type 'help' for more information.\n")

        elif cmd in ("website", "w"):
            arg = cmd_parts[1] if len(cmd_parts) > 1 else None
            res = website_cmd(arg)
            if res == "exit":
                print("Exiting hackr. Goodbye.")
                break        


        # Placeholder for future commands 
        else:
            print(f"[stub] Command '{cmd}' received but not implemented yet.")


def main():
    name = input("Enter username: ").strip() or "user"
    # clear the terminal (cross-platform)
    os.system("cls" if sys.platform.startswith("win") else "clear")
    print_header(name)
    print(f"Welcome back {name}, type 'help' for more information.\n")
    repl(name)

if __name__ == "__main__":
    main()
