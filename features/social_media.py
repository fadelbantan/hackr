import time, random, string, sys
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn

TYPEWRITER_SPEED = 0.005

def _typewriter(text, speed=TYPEWRITER_SPEED):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")
    sys.stdout.flush()

def _random_password(length=10):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

def _basic_progress(description, total):
    """Create a basic progress bar"""
    return Progress(
        SpinnerColumn(style="magenta"),
        TextColumn("[bold cyan]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
        TimeRemainingColumn(),
    )

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
            break # when a valid username is received

    # Initialization progress bar
    print("\nInitializing...\n")
    with _basic_progress("Initializing", 100) as progress:
        task = progress.add_task("Initializing", total=100)
        for _ in range(100):
            time.sleep(0.025)
            progress.update(task, advance=1)
    print()
    time.sleep(0.8)

    # confirmation after receiving username
    ans = input(f"Is the username @{username} correct? (y/n): ").strip().lower()
    if not ans or ans[0] != "y":
        return socials_cmd()
    
    # Executing timer
    print("\nExecuting exploits...\n")
    with _basic_progress("Executing", 80) as progress:
        task = progress.add_task("Executing", total=80)
        for _ in range(80):
            time.sleep(0.065)
            progress.update(task, advance=1)
    print()
    time.sleep(0.7)

    print()
    sys.stdout.write("\033[1;31m[socials]\033[0;32m ")
    sys.stdout.flush()
    _typewriter(f"enumerating public profiles for @{username} (X, Instagram, Facebook, LinkedIn)", speed=TYPEWRITER_SPEED)
    time.sleep(0.10)

    # Alive progress bars for each phase of the sweep
    progress_phases = [
        ("Facebook", 98, 0.05),
        ("Instagram", 45, 0.03),
        ("Snapchat", 83, 0.098),
        ("X", 95, 0.022),
    ]
    for title, total, delay in progress_phases:
        with _basic_progress(title, total) as progress:
            task = progress.add_task(title, total=total)
            for _ in range(total):
                time.sleep(delay)
                progress.update(task, advance=1)

    
    # execution lines
    lines = [
        ("[network]", "negotiating TLS context and cipher suite"),
        ("[auth]", "validating session token and cookie parameters"),
        ("[proxy]", "tunneling traffic through edge nodes"),
        ("[cache]", "parsing public media endpoints"),
        ("[analysis]", "correlating request patterns and metadata"),
        ("[intel]", "enumerating public handles across X/IG/FB/LinkedIn directories"),
        ("[signals]", "cloning follower and connection graphs for anomaly scoring"),
        ("[metadata]", "harvesting bio links, geotags, and contact breadcrumbs"),
        ("[archive]", "diffing Wayback/CommonCrawl captures for deleted posts"),
        ("[forensics]", "extracting EXIF/device hints from recent media uploads"),
        ("[alerts]", "cross-referencing breach corpora for matching emails or handles"),
    ]

    print()
    for stub, text in lines:
        sys.stdout.write(f"\033[1;31m{stub}\033[0;32m ")
        sys.stdout.flush()
        _typewriter(text, speed=TYPEWRITER_SPEED)
        time.sleep(random.uniform(0.08, 0.18))
    time.sleep(0.6)

    # Final report progress bar
    print()
    sys.stdout.write("\033[1;31m[report]\033[0;32m ")
    sys.stdout.flush()
    _typewriter("consolidating findings and drafting exposure summary", speed=TYPEWRITER_SPEED)
    with _basic_progress("Generating report", 100) as progress:
        task = progress.add_task("Generating report", total=100)
        for _ in range(100):
            time.sleep(0.05)
            progress.update(task, advance=1)
    print()
    time.sleep(1.3)

    # Final report
    domain = ["gmail", "hotmail", "mail", "outlook", "icloud"]
    password = _random_password(10)
    email = f"{username}.{random.randint(1,999)}@{random.choice(domain)}.com"

    sys.stdout.write("\033[33m") # Switch to yellow
    sys.stdout.flush()
    print("\n======    HACK REPORT   ======")
    print(f"Username : {username}")
    print(f"Email    : {email}")
    print(f"Password : {password}")
    print("===============================\n")
    sys.stdout.write("\033[32m") # Back to green
    sys.stdout.flush()
    time.sleep(0.8)

    # prompt what to do next
    return {"username": username, "email": email, "password": password}
