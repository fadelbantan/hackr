import os
import sys, time
from pyfiglet import Figlet

# Main Header using Figlet library
def print_header(name="HACKR"):
    f = Figlet(font="ansi_shadow")
    print(f.renderText("hackr"))


# Very fast temporarily for better responses.
# TODO: Make speed faster
def typewriter(text, speed=0.002):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")
    sys.stdout.flush()

# Read-Eval-Print Loop
def repl(username):

    prompt = f"hackr@{username} $ "
    print()





def main():
    
    name = input("Enter username: ").strip() or "HACKR"
    