import os, sys, time, random, string, re, runpy
from alive_progress import alive_bar

TYPEWRITER_SPEED = 0.005

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

# local typewriter function
def _typewriter(text, speed=TYPEWRITER_SPEED): 
    for ch in str(text):
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")
    sys.stdout.flush()

# main command
def website_cmd(target: str = None):
    # Initialization progress bar 
    print("\nInitializing...\n")
    with alive_bar(100) as bar:
        for _ in range(100):
            time.sleep(0.025)
            bar()
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
        ("dns sweep", 90, 0.03),
        ("cert telemetry", 70, 0.04),
        ("service census", 80, 0.035),
        ("exposure diff", 85, 0.032),
    ]
    for title, total, delay in recon_phases:
        with alive_bar(total, title=f"{title:<16}") as bar:
            for _ in range(total):
                time.sleep(delay)
                bar()
    print()

    # execution lines
    script_lines = [
        f"[dns] passive DNS / WHOIS sweep on {display} (RiskIQ, SecurityTrails mirrors)",
        "[cert] certificate transparency delta via crt.sh and Google CT (SAN churn, issuers)",
        "[tls] handshake capture and cipher/cert audit (SSL Labs style scoring)",
        "[services] banner harvesting and fingerprinting from cached Shodan/Censys hits",
        "[tech] stack fingerprint (Wappalyzer/BuiltWith signatures, response headers)",
        "[crawl] parse robots.txt + sitemap.xml; seed crawl queue with exposed paths",
        "[archive] diff Wayback/CommonCrawl snapshots for removed directories and files",
        "[content] shallow crawl for config leaks, .env/.git remnants, backup artifacts",
        f"[code] hunt {display} references in public repos/CI logs for leaked tokens",
        "[storage] probe public S3/GCS/Azure listings tied to discovered subdomains",
        "[vuln] normalize software versions and cross-reference CVEs (NVD/CPE lookup)",
        "[intel] correlate breach corpora for shared emails, subdomains, SSL subjects",
        "[report] compile recon dossier with exposure score + remediation checklist"
    ]

    for ln in script_lines:
        _typewriter(ln, speed=TYPEWRITER_SPEED)
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
            if j >= 8:
                print("... (truncated) ...")
                break
            print(line)
        print()
        time.sleep(1)

    if len(db_blocks) > sample_count:
        print("[dim](... additional data truncated ...)[/dim]\n")

    # Run staged progress bars
    stage_phases = [
        ("surface mapping", 94, 0.03),
        ("endpoint fuzzing", 69, 0.04),
        ("artifact assembly", 83, 0.035),
    ]
    print("Running concurrent stages (simulated):\n")
    for title, total, delay in stage_phases:
        with alive_bar(total, title=f"{title:<18}") as bar:
            for _ in range(total):
                time.sleep(delay)
                bar()
    print()

    # short finalization progress bar
    print("\nDownloading hacked database from", target)
    with alive_bar(100) as bar:
        for _ in range(100):
            time.sleep(0.045)
            bar()
    print()

    print("Decrypting downloaded data...")
    with alive_bar(100) as bar:
        for _ in range(100):
            time.sleep(0.024)
            bar()
    print("\n[+] Decryption successful\n")

    # Final report
    owner = _random_owner()
    passphrase = _random_pass(10)
    print("======    WEB APP DETAILS    ======")
    print(f"Website : {display}")               
    print(f"Owner   : {owner}")                 
    print(f"Passphrase: {passphrase}")          
    print("===================================\n")

    return {"target": display, "owner": owner, "passphrase": passphrase}
