import os, sys, time, random, string, threading, re, runpy
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
    """Import DATABASES from a Python file."""
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

# typewriter used for script lines
def _typewriter(text, speed=TYPEWRITER_SPEED): 
    for ch in str(text):
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")
    sys.stdout.flush()

# concurrency helpers for 3 timers
def _timer_worker(name, duration, state_dict):
    """Worker that sleeps and updates a state dict percent over time."""
    start = time.perf_counter()
    while True:
        elapsed = time.perf_counter() - start
        pct = min(100, int((elapsed / max(0.0001, duration)) * 100))
        state_dict[name] = pct
        if pct >= 100:
            break
        time.sleep(0.05)
    state_dict[name] = 100

# main command
def website_cmd(target: str = None):
    # Initialization before asking for target (when not omitted)
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

    # Gathering information timer
    print(f"\nGathering information on {target}\n")
    with alive_bar(100) as bar:
        for _ in range(100):
            time.sleep(0.040)
            bar()
    print()

    # Run a few script lines using typewriter
    script_lines = [
        f"[payload] prepare_probe --target {display}",
        "[script] exploit_fingerprints --mode quick",
        "[script] harvest_public_posts --limit 40",
        "[payload] enumerate_endpoints --depth 3",
        "[util] fingerprint_server --aggressive"
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
            "/var/log/auth.log\nOct 25 12:00:00 sshd[123]: Accepted password for admin from 10.0.0.1"
        ]

    print("\nSimulated database samples (preview):\n")

    # pick 5 random unique blocks each time
    sample_count = min(5, len(db_blocks))
    selected_blocks = random.sample(db_blocks, sample_count)

    for block in selected_blocks:
        block = block.strip()
        for j, line in enumerate(block.splitlines()):
            if j >= 6:
                print("... (truncated) ...")
                break
            print(line)
        print()
        time.sleep(1)

    if len(db_blocks) > sample_count:
        print("[dim](... additional data truncated ...)[/dim]\n")

    # Run three timers concurrently (simulated stages)
    timers = {
        "Stage-A: handshake": 1.7, # durations in seconds
        "Stage-B: brute": 2.4,
        "Stage-C: assemble": 2.6
    }
    state = {name: 0 for name in timers.keys()}
    threads = []
    for name, dur in timers.items():
        t = threading.Thread(target=_timer_worker, args=(name, dur, state), daemon=True)
        threads.append(t)
        t.start()

    # Display live textual progress for the three timers (main thread polls)
    print("Running concurrent stages:\n")
    try:
        while True:
            # render status lines
            lines = []
            done = True
            for name in timers.keys():
                pct = state.get(name, 0)
                lines.append(f"{name:20s} [{pct:3d}%]")
                if pct < 100:
                    done = False
            print("\r" + "   ".join(lines), end="")
            if done:
                break
            time.sleep(0.12)
        print()
    except KeyboardInterrupt:
        print("\nInterrupted concurrent stages.")

    # short finalization (download + decrypt imitation)
    print("\nDownloading Hacked DataBase from", target)
    with alive_bar(100) as bar:
        for _ in range(100):
            time.sleep(0.045)
            bar()
    print()

    print("Decrypting Downloaded Data...")
    with alive_bar(100) as bar:
        for _ in range(100):
            time.sleep(0.024)
            bar()
    print("\n[+] Decryption Successful\n")

    # Final report
    owner = "AC71ON"
    passphrase = _random_pass(10)
    print("=== WEB APP DETAILS (SIMULATED) ===")
    print(f"Website : {display}")
    print(f"Owner   : {owner}")
    print(f"Passphrase: {passphrase}")
    print("===================================\n")

    return {"target": display, "owner": owner, "passphrase": passphrase}
