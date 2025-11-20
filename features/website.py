import os, time, random, string, re, runpy, sys
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn

TYPEWRITER_SPEED = 0.005

def _typewriter(text, speed=TYPEWRITER_SPEED):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")
    sys.stdout.flush()

# simple regex validator
def _is_valid_target(t):
    if not t:
        return False
    t = t.strip()
    pattern = r"^(https?://)?([A-Za-z0-9\-]+\.)+[A-Za-z]{2,6}(/.*)?$"
    return re.match(pattern, t) is not None

# load database blocks from data/databases.py
def load_databases(path="data/databases.py"):    
    if not os.path.exists(path):
        return []
    try:
        mod = runpy.run_path(path)
        dbs = mod.get("DATABASES", [])
        return [str(x).strip() for x in dbs if x]
    except Exception as e:
        print(f"[!] Could not load databases: {e}")
        return []

# random pass generator
def _random_pass(length=10):
    chars = string.ascii_lowercase + string.digits
    return "".join(random.choice(chars) for _ in range(length))

def _random_owner():
    first = ["Helios", "Orion", "Axiom", "Nova", "Cipher", "Atlas", "Vertex"]
    last = ["Ops", "Guard", "Labs", "Security", "Core", "Systems", "Grid"]
    return random.choice(first) + random.choice(last)

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

# main command
def website_cmd(target: str = None):
    # Initialization progress bar 
    print("\nInitializing...\n")
    with _basic_progress("Initializing", 100) as progress:
        task = progress.add_task("Initializing", total=100)
        for _ in range(100):
            time.sleep(0.025)
            progress.update(task, advance=1)
    print()

    # Prompt for target if not omitted
    while True:
        if not target:
            target = input("Enter website or domain (e.g. example.com): ").strip()

        if not target:
            print("No target provided. Try again.\n")
            target = None
            continue

        if not _is_valid_target(target):
            print("Target looks invalid. Expected domain or URL.\n")
            target = None
            continue
        # valid input, exit loop
        break

    # normalize display
    display = target
    if display.startswith("http://") or display.startswith("https://"):
        display = display.split("://", 1)[1].rstrip("/")

    # Gathering information timer with multi-phase indicators
    print(f"\nGathering information on {target}\n")
    recon_phases = [
        ("dns sweep", 90, 0.02),
        ("cert telemetry", 70, 0.02),
        ("service census", 80, 0.02),
        ("exposure diff", 85, 0.02),
    ]
    for title, total, delay in recon_phases:
        with _basic_progress(title, total) as progress:
            task = progress.add_task(title, total=total)
            for _ in range(total):
                time.sleep(delay)
                progress.update(task, advance=1)
    print() # execution lines
    script_lines = [
        ("[dns]", f"passive DNS / WHOIS sweep on {display} (RiskIQ, SecurityTrails mirrors)"),
        ("[cert]", "certificate transparency delta via crt.sh and Google CT (SAN churn, issuers)"),
        ("[tls]", "handshake capture and cipher/cert audit (SSL Labs style scoring)"),
        ("[services]", "banner harvesting and fingerprinting from cached Shodan/Censys hits"),
        ("[tech]", "stack fingerprint (Wappalyzer/BuiltWith signatures, response headers)"),
        ("[crawl]", "parse robots.txt + sitemap.xml; seed crawl queue with exposed paths"),
        ("[archive]", "diff Wayback/CommonCrawl snapshots for removed directories and files"),
        ("[content]", "shallow crawl for config leaks, .env/.git remnants, backup artifacts"),
        ("[code]", f"hunt {display} references in public repos/CI logs for leaked tokens"),
        ("[storage]", "probe public S3/GCS/Azure listings tied to discovered subdomains"),
        ("[vuln]", "normalize software versions and cross-reference CVEs (NVD/CPE lookup)"),
        ("[intel]", "correlate breach corpora for shared emails, subdomains, SSL subjects"),
        ("[report]", "compile recon dossier with exposure score + remediation checklist"),
    ]

    for stub, text in script_lines:
        sys.stdout.write(f"\033[1;31m{stub}\033[0;32m ")
        sys.stdout.flush()
        _typewriter(text, speed=TYPEWRITER_SPEED)
        time.sleep(random.uniform(0.05, 0.15))

    # Load fake DBs from external file and show a small preview
    db_blocks = load_databases()
    if not db_blocks:
        db_blocks = [
            "/etc/passwd\nroot:x:0:0:root:/root:/bin/bash\nuser:x:1000:1000:User:/home/user:/bin/bash",
            "/home/admin/notes.txt\nAPI_KEY=abcd-efgh-ijkl\npassword_hint=summer2021",
        ]

    print("\nDatabase samples:\n")

    # pick 5 random unique blocks each time
    sample_count = min(5, len(db_blocks))
    selected_blocks = random.sample(db_blocks, sample_count)

    for block in selected_blocks:
        block = block.strip()
        for j, line in enumerate(block.splitlines()):
            if j >= 10:
                print("... (truncated) ...")
                break
            print(line)
        print()
        time.sleep(1)

    if len(db_blocks) > sample_count:
        sys.stdout.write("\033[2m(... additional data truncated ...)\033[0;32m\n\n")
        sys.stdout.flush()
    # Run staged progress bars
    stage_phases = [
        ("surface mapping", 94, 0.03),
        ("endpoint fuzzing", 69, 0.04),
        ("artifact assembly", 83, 0.035),
    ]
    print("Running concurrent stages (simulated):\n")
    for title, total, delay in stage_phases:
        with _basic_progress(title, total) as progress:
            task = progress.add_task(title, total=total)
            for _ in range(total):
                time.sleep(delay)
                progress.update(task, advance=1)
    print()

    # short finalization progress bar
    print("\nDownloading hacked database from", target)
    with _basic_progress("Downloading", 100) as progress:
        task = progress.add_task("Downloading", total=100)
        for _ in range(100):
            time.sleep(0.045)
            progress.update(task, advance=1)
    print()

    print("Decrypting downloaded data...")
    with _basic_progress("Decrypting", 100) as progress:
        task = progress.add_task("Decrypting", total=100)
        for _ in range(100):
            time.sleep(0.024)
            progress.update(task, advance=1)
    print()
    sys.stdout.write("\033[1;31m[+]\033[0;32m ")
    sys.stdout.flush()
    _typewriter("Decryption successful", speed=TYPEWRITER_SPEED)

    # Final report
    owner = _random_owner()
    passphrase = _random_pass(10)
    sys.stdout.write("\033[33m") # Switch to yellow
    sys.stdout.flush()
    print("======    WEB APP DETAILS    ======")
    print(f"Website : {display}")               
    print(f"Owner   : {owner}")                 
    print(f"Passphrase: {passphrase}")          
    print("===================================\n")
    sys.stdout.write("\033[32m") # Back to green
    sys.stdout.flush()

    return {"target": display, "owner": owner, "passphrase": passphrase}
