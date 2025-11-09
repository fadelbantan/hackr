import time, sys, random, string
from alive_progress import alive_bar

TYPEWRITER_SPEED = 0.005

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
        # prompt for username until it's valid
        while True:
            username = input("Enter username to hack: ").strip()
            if not username:
                print("Please enter a username (minimum 3 characters).")
                continue
            if len(username) < 3:
                print("Username must be at least 3 characters.")
                continue
            break  # when a valid username is received

            
    # Initialization progress bar
    print("\nInitializing...\n")
    with alive_bar(100) as bar:
        for _ in range(100):
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
    print("\nExecuting exploits...\n")
    with alive_bar(80) as bar:
        for _ in range(80):
            time.sleep(0.045)
            bar()
    print()
    time.sleep(0.7)

    # local typewriter function
    def _typewriter(text, speed=TYPEWRITER_SPEED):
        for ch in str(text):
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(speed)
        sys.stdout.write("\n")
        sys.stdout.flush()

    # execution lines 
    lines = [
        f"[socials] enumerating public profiles for @{username} (X, Instagram, Facebook, LinkedIn, GitHub)",
        "[socials] scraping profile metadata (bio, links, location, join date)",
        "[socials] harvesting recent public posts, replies and media (limit 50)",
        "[socials] extracting media metadata and EXIF via exiftool",
        "[socials] reverse-image checks (TinEye, Google Images) for cross-postings",
        "[socials] checking archived snapshots (Wayback, CommonCrawl) for deleted content",
        "[socials] indexing paste/archive mentions (Pastebin, GhostProject, archived dumps)",
        "[socials] resolving linked accounts and email hints (Hunter.io-style discovery)",
        "[socials] searching public code repos and CI logs for exposed tokens (GitHub, GitLab)",
        "[socials] mapping social graph and follower/connections clusters (Maltego/Graph style)",
        "[socials] checking third-party indexers and OSINT tools (SpiderFoot, theHarvester) for leads",
        "[socials] compiling concise social-profile intelligence report and exposure score"
    ]

    # print each line with typewriter function
    for ln in lines:
        _typewriter(ln, speed=TYPEWRITER_SPEED)
        time.sleep(random.uniform(0.08, 0.18))
    time.sleep(0.6)

    # Final report
    domain = ["gmail", "hotmail", "mail", "outlook", "icloud"]
    password = _random_password(10)
    email = f"{username}.{random.randint(1,999)}@{random.choice(domain)}.com"

    print("\n======   HACK REPORT   ======")
    print(f"Username : {username}")
    print(f"Email    : {email}")
    print(f"Password : {password}")
    print("===============================")
    time.sleep(0.8)

    # prompt what to do next
    return {"username": username, "email": email, "password": password}
