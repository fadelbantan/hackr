#!/usr/bin/env python3

import sys, time, os
from pyfiglet import Figlet
from features.social_media import socials_cmd


# Main Header using Figlet library
def print_header(name="HACKR"):
    f = Figlet(font="ansi_shadow")
    print(f.renderText("hackr"))

# Very fast temporarily for better responses.
# TODO: Make speed slower later
def typewriter(text, speed=0.002):
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
socials <username>   : Simulate enumerating public social links for <username>.
                       If <username> is omitted, you will be prompted to enter one.
help                 : Show this help text.
exit, quit           : Exit the program.
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
        elif cmd in ('quit', 'exit'):
            print("Exiting hackr. Goodbye.")
            break
        elif cmd == "social":
            socials_cmd(target)
        else:
            # Placeholder for future commands 
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
