#!/usr/bin/env python3

import sys, os
from pyfiglet import Figlet
from features.social_media import socials_cmd
from features.website import website_cmd
from features.osint import osint_cmd
from features.hacktype import hacktype_cmd
from data.colors import GREEN, RED, BOLD, CLEAR, PURPLE, BLUE

TYPEWRITER_SPEED = 0.005

# Clear terminal function
def clear_terminal():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        # Reset terminal state to clear screen
        sys.stdout.write("\033c")
        sys.stdout.flush()
    # Set green as default color
    sys.stdout.write(GREEN)
    sys.stdout.flush()

# Main Header using Figlet library
def print_header():
    try:
        f = Figlet(font="ansi_shadow")
        print("\n" + f.renderText(" hackr"))
    except Exception as exc:
        # Fall back to a simple title if Figlet fails (e.g., missing font/tty issues)
        print("\n**** hackr ****")
        sys.stdout.write(f"{RED}[warn]{CLEAR}{GREEN} unable to render banner: {exc}\n")
        sys.stdout.flush()
    
# Help menu
def print_help():
    help_text = f"""
{BOLD}{BLUE}hackr{PURPLE}
A hacking simulation to get the feel of the real thing.
Use the commands below to navigate through the different tools available.

{BOLD}{BLUE}COMMANDS{PURPLE}
socials, s <username> : Retrieve social media password for <username>.
                        If <username> is omitted, you will be prompted to enter one.

website, w <target>   : Perform website reconnaissance on <target> (e.g. example.com).
                        If <target> is omitted, you will be prompted to enter one.

osint, o [-n NAME | -e EMAIL | -p PHONE]
                      : Open-source intelligence lookup. Pass a flag to skip prompts.
                        Examples: `osint -n "John Doe"`, `osint -e user@mail.com`, `osint -p +966512345678`

hacktype, type, t [--fast | --slow]
                      : Fake code typing cinematic. Clears to blank screen.
                        Press ESC to return to main.
                        --fast: faster typing (4-7 chars/key), --slow: slower (1-3 chars/key)
                        Examples: `hacktype`, `hacktype --fast`, `type --slow`

help                  : Show this help menu.

clear, c              : Clear the terminal and redraw the main screen.

exit, quit, q         : Exit the program.
"""
    print(help_text)

# Read-Eval-Print Loop
def repl(username):
    print()
    while True:
        # username and 'hostname'
        sys.stdout.write(f"{BOLD}{RED}{username}@hackr{CLEAR}{GREEN} $ ")
        sys.stdout.flush()
        try:
            line = input().strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting hackr. Goodbye.")
            break
        # If enter is pressed without any input, start loop again
        if not line:
            continue

        # Split input in separate words in a list
        cmd_parts = line.split()
        # First word is the command
        cmd = cmd_parts[0].lower()

        try:
            if cmd == 'help':
                print_help()

            elif cmd == 'clear' or cmd == 'c':
                clear_terminal()
                print_header()
                print(f"Welcome back {username}, type 'help' for more information.\n")

            elif cmd == "quit" or cmd == "exit" or cmd == "q":
                print("Exiting hackr. Goodbye.")
                break

            elif cmd == "socials" or cmd == "s":
                # preserve original behavior: accept a single arg if provided, otherwise let the feature prompt
                arg = cmd_parts[1] if len(cmd_parts) > 1 else None
                if arg is not None and len(arg) < 3:
                    print("Error: username must be at least 3 characters.")
                    continue
                socials_cmd(arg)

            elif cmd == "website" or cmd == "w":
                arg = cmd_parts[1] if len(cmd_parts) > 1 else None
                website_cmd(arg)

            elif cmd == "osint" or cmd == "o":
                arg = cmd_parts[1] if len(cmd_parts) > 1 else None
                osint_cmd(mode=None, value=arg)

            elif cmd == "hacktype" or cmd == "type" or cmd == "t":
                # Extract flags (anything starting with --)
                flags = [part for part in cmd_parts[1:] if part.startswith("--")]
                # Enter sub-REPL interface for hacktype; on return refresh main screen
                hacktype_cmd(username, flags if flags else None)
                clear_terminal()
                print_header()
                print(f"Welcome back {username}, type 'help' for more information.\n")

            else:
                sys.stdout.write(f"{RED}[pending]{GREEN} Command '{cmd}' awaiting implementation.\n")
                sys.stdout.flush()
        except KeyboardInterrupt:
            print("\nInterrupted. Returning to main screen.\n")
            continue
        except Exception as e:
            sys.stdout.write(f"{RED}[error]{CLEAR}{GREEN} Command failed: {e}\n")
            sys.stdout.flush()


def main():
    # Set green color before any input
    sys.stdout.write(GREEN)
    # Flush output buffer to ensure color is applied immediately
    sys.stdout.flush()
    try:
        name = input("Enter username: ").strip() or "root"
    except (EOFError, KeyboardInterrupt):
        print("\nExiting hackr. Goodbye.")
        return
    clear_terminal()
    print_header()
    print(f"Welcome back {name}, type 'help' for more information.\n")
    repl(name)

if __name__ == "__main__":
    main()
