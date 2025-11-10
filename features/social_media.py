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
    time.sleep(0.8)

    # confirmation after receiving username
    ans = input(f"Is the username @{username} correct? (y/n): ").strip().lower()
    if not ans or ans[0] != "y":
        return socials_cmd()
    
    # Executing timer
    print("\nExecuting exploits...\n")
    with alive_bar(80) as bar:
        for _ in range(80):
            time.sleep(0.065)
            bar()
    print()
    time.sleep(0.7)

    # typewriter function
    def _typewriter(text, speed=TYPEWRITER_SPEED):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        sys.stdout.write("\n")
        sys.stdout.flush()


    _typewriter(f"[socials] enumerating public profiles for @{username} (X, Instagram, Facebook, LinkedIn)\n", speed=TYPEWRITER_SPEED)
    time.sleep(0.10)

    # Alive progress bars for each phase of the sweep
    progress_phases = [
        ("Facebook  ", 98, 0.05),
        ("Instagram ", 45, 0.03),
        ("Snapchat  ", 83, 0.098),
        ("X         ", 95, 0.022),
    ]
    for title, total, delay in progress_phases:
        with alive_bar(total, title=f"{title:<16}") as bar:
            for _ in range(total):
                time.sleep(delay)
                bar()

    
    # execution lines
    lines = [
        "\n[network] negotiating TLS context and cipher suite",
        "[auth] validating session token and cookie parameters",
        "[proxy] tunneling traffic through edge nodes",
        "[cache] parsing public media endpoints",
        "[analysis] correlating request patterns and metadata",
        "[intel] enumerating public handles across X/IG/FB/LinkedIn directories",
        "[signals] cloning follower and connection graphs for anomaly scoring",
        "[metadata] harvesting bio links, geotags, and contact breadcrumbs",
        "[archive] diffing Wayback/CommonCrawl captures for deleted posts",
        "[forensics] extracting EXIF/device hints from recent media uploads",
        "[alerts] cross-referencing breach corpora for matching emails or handles",
        
    ]

    # print each line with typewriter function
    for ln in lines:
        _typewriter(ln, speed=TYPEWRITER_SPEED)
        time.sleep(random.uniform(0.08, 0.18))
    time.sleep(0.6)

    # Final report progress bar
    print("\n[report] consolidating findings and drafting exposure summary\n")
    with alive_bar(100) as bar:
        for _ in range(100):
            time.sleep(0.05)
            bar()
    print()
    time.sleep(1.3)

    # Final report
    domain = ["gmail", "hotmail", "mail", "outlook", "icloud"]
    password = _random_password(10)
    email = f"{username}.{random.randint(1,999)}@{random.choice(domain)}.com"

    print("\n======    HACK REPORT   ======")
    print(f"Username : {username}")
    print(f"Email    : {email}")
    print(f"Password : {password}")
    print("===============================\n")
    time.sleep(0.8)

    # prompt what to do next
    return {"username": username, "email": email, "password": password}
