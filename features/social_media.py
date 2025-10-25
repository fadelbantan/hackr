import time, sys, random, string
from alive_progress import alive_bar


def _random_password(length=10):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

def socials_cmd(username=None):
    # if user didn't provide username with command
    if not username:
        username = input("Enter username to hack: ").strip()
        if not username:
            print("No username provided. Aborting.")
            return
    
    # Initialization progress bar
    print("\nInitializing...\n")
    with alive_bar(100) as bar:
        for i in range(100):
            time.sleep(0.005) # Short for testing TODO: increase later
            bar()
    print()

    # confirmation after receiving username
    ans = input(f"Proceed with simulated socials flow for '{username}'? (y/n): ").strip().lower()
    if not ans or ans[0] != "y":
        print("Cancelled.")
        return
    
    # Executing timer
    print("\nExecuting...\n")
    with alive_bar(60) as bar:
        for i in range(60):
            time.sleep(0.02)  # TODO: increase timer
            bar()
    print()

    # local typewriter function
    def _typewriter(text, speed=0.003):
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
        _typewriter(ln, speed=0.003) # TODO: make a little bit slower
        time.sleep(random.uniform(0.04, 0.15)) # short pause between lines

    # Final report
    password = _random_password(10)
    email = f"{username}.{random.randint(1,999)}@example.com"

    print("\n=== HACK REPORT (SIMULATED) ===")
    print(f"Username : {username}")
    print(f"Email    : {email}")
    print(f"Password : {password}")
    print("===============================")


    # prompt what to do next
    while True:
        choice = input("\nWould you like to execute another attack? [y/n]: ").strip().lower()
        if not choice or choice[0] == 'y':
            return None    # go back to REPL (main)
        if choice[0] == 'n':
            return "exit"  # signal REPL to exit
        print("Please enter 'y' for another attack or 'n' to exit.")