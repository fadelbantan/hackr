#!/usr/bin/env python3

import sys, os
from pyfiglet import Figlet
from rich.console import Console
from features.social_media import socials_cmd
from features.website import website_cmd
from features.osint import osint_cmd

TYPEWRITER_SPEED = 0.005
DEFAULT_STYLE = "green"
console = Console(style=DEFAULT_STYLE)

# Clear terminal function
def clear_terminal():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        # Reset terminal state to clear screen
        sys.stdout.write("\033c") # https://en.cppreference.com/w/c/language/ascii.html
        sys.stdout.flush()

# Main Header using Figlet library
def print_header():
    f = Figlet(font="ansi_shadow")
    console.print("\n" + f.renderText(" hackr"), style="bold green")

# Help menu
def print_help():
    help_text = f"""
\033[1mhackr\033[0m
A hacking simulation to get the feel of the real thing.
Use the commands below to navigate through the different tools available.

\033[1mCOMMANDS\033[0m
socials, s <username> : Retrieve social media password for <username>.
                        If <username> is omitted, you will be prompted to enter one.

website, w <target>   : Perform website reconnaissance on <target> (e.g. example.com).
                        If <target> is omitted, you will be prompted to enter one.

osint, o [-n NAME | -e EMAIL | -p PHONE]
                      : Open-source intelligence lookup. Pass a flag to skip prompts.
                        Examples: `osint -n "John Doe"`, `osint -e user@mail.com`, `osint -p +966512345678`

help                  : Show this help menu.

clear, c              : Clear the terminal and redraw the main screen.

exit, quit, q         : Exit the program.
"""
    console.print(help_text)

# Read-Eval-Print Loop
def repl(username):
    prompt = f"[bold red]{username}@hackr[/bold red] $ [{DEFAULT_STYLE}]"
    console.print()
    while True:
        line = console.input(prompt).strip()
        # If enter is pressed without any input, start loop again
        if not line:
            continue

        # Split input in separate words in a list
        cmd_parts = line.split()
        # First word is the command
        cmd = cmd_parts[0].lower()

        if cmd == 'help':
            print_help()

        elif cmd == 'clear' or cmd == 'c':
            clear_terminal()
            print_header()
            console.print(f"Welcome back {username}, type 'help' for more information.\n")

        elif cmd == "quit" or cmd == "exit" or cmd == "q":
            console.print("Exiting hackr. Goodbye.")
            break

        elif cmd == "socials" or cmd == "s":
            arg = cmd_parts[1] if len(cmd_parts) > 1 else None
            if arg is not None and len(arg) < 3:
                console.print("Error: username must be at least 3 characters.")
                continue
            socials_cmd(arg)

        elif cmd == "website" or cmd == "w":
            arg = cmd_parts[1] if len(cmd_parts) > 1 else None
            website_cmd(arg)

        elif cmd == "osint" or cmd == "o":
            # preserve original behavior: accept a single arg if provided, otherwise let the feature prompt
            arg = cmd_parts[1] if len(cmd_parts) > 1 else None
            osint_cmd(mode=None, value=arg)

        else:
            console.print(f"[bold red][pending][/bold red] Command '{cmd}' awaiting implementation.", markup=True)


def main():
    name = console.input("Enter username: ").strip() or "root"
    clear_terminal()
    print_header()
    console.print(f"Welcome back {name}, type 'help' for more information.\n")
    repl(name)

if __name__ == "__main__":
    main()
