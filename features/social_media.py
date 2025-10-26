import time, sys, random, string
from alive_progress import alive_bar


def _random_password(length=10):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

def socials_cmd(username=None):
    # if a username was provided as an argument, validate it
    if username is not None:
        username = username.strip()
        if len(username) < 3:
            print("Error: username must be at least 3 characters.")
            return None
    else:
        # prompt for username until it's valid or the user aborts
        while True:
            username = input("Enter username to hack: ").strip()
            if not username:
                print("No username provided. Aborting.")
                return None
            if len(username) < 3:
                print("Username must be at least 3 characters.")
                # loop again to reprompt
                continue
            break  # got a valid username
            
    # Initialization progress bar
    print("\nInitializing...\n")
    with alive_bar(100) as bar:
        for i in range(100):
            time.sleep(0.025)
            bar()
    print()
    time.sleep(0.6)

    # confirmation after receiving username
    ans = input(f"Is the username @{username} correct? (y/n): ").strip().lower()
    if not ans or ans[0] != "y":
        print("Cancelled.")
        return
    
    # Executing timer
    print("\nExecuting...\n")
    with alive_bar(80) as bar:
        for _ in range(80):
            time.sleep(0.045)
            bar()
    print()
    time.sleep(0.7)

    # local typewriter function
    def _typewriter(text, speed=0.04):
        for ch in str(text):
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(speed)
        sys.stdout.write("\n")
        sys.stdout.flush()

    # dummy script lines 
    lines = [
        f"[payload] prepare_profile_enum --target {username}",
        "[script] exploit_fingerprints --mode quick",
        "[script] harvest_public_posts --limit 50",
        "[util] collect_metadata --format json",
        "[payload] enumerate_connections --depth 2",
        "[analyze] sentiment_pipeline --batch 1",
        "[probe] open_ports --fast-scan",
        "[decode] media_cache --extract-metadata",
        "[chain] build_graph --min-score 0.7",
        "[search] leaked_credentials --source dark-web",
        "[brute] candidate_passwords --threads 8",
        "[merge] results --dedupe",
        "[persist] store_cache --encrypted",
        "[notify] alert_engine --level low",
        "[cleanup] shred_temp_files --passes 1"
    ]

    # print each line with typewriter function
    for ln in lines:
        _typewriter(ln, speed=0.04)
        time.sleep(random.uniform(0.08, 0.18))
    time.sleep(0.6)

    # Final report
    domain = ["gmail", "hotmail", "mail", "outlook", "icloud"]
    password = _random_password(10)
    email = f"{username}.{random.randint(1,999)}@{random.choice(domain)}.com"

    print("\n=== HACK REPORT (SIMULATED) ===")
    print(f"Username : {username}")
    print(f"Email    : {email}")
    print(f"Password : {password}")
    print("===============================")
    time.sleep(0.8)

    # prompt what to do next
    while True:
        choice = input("\nWould you like to execute another attack? [y/n]: ").strip().lower()
        if not choice or choice[0] == 'y':
            return None    # go back to REPL (main)
        if choice[0] == 'n':
            return "exit"  # signal REPL to exit
        print("Please enter 'y' for another attack or 'n' to exit.")
