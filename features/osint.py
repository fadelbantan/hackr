import re, time, random, string, sys
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn

TYPEWRITER_SPEED = 0.005

def _typewriter(text, speed=TYPEWRITER_SPEED):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")
    sys.stdout.flush()

_common_passwords = [
    "passwordpassword", "123456", "mypuppymaxwell", "letmein", "iloveyou",
    "admin", "welcome", "lovely", "passw0rd", "summer2021"
]

def _random_password(length=10):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

def _valid_email(e):
    return bool(re.match(r"^[^@\s]+@[^@\s]+\.[A-Za-z]{2,}$", e.strip()))

def _valid_phone(p):
    # simple: digits and + allowed, require 7-15 digits
    digits = re.sub(r"\D", "", p)
    return 7 <= len(digits) <= 15

def _random_address():
    streets = ["Price Sultan Rd", "Heraa St", "Al Amal", "King Rd", "An Nuzhah Ds", "1st St", "Industrial Village"]
    cities = ["Jeddah", "Al Khobar", "Dammam", "Riyadh", "Medina"]
    return f"{random.randint(10,999)} {random.choice(streets)}, {random.choice(cities)}, Saudi Arabia"

def _random_phone():
    return f"+966{random.randint(500000000, 599999999)}"

def _random_email_from_name(name):
    local = re.sub(r"\s+", ".", name.strip().lower())
    domain = random.choice(["mail.com","outlook.uk.co","icloud.com","hotmail.co"])
    return f"{local}.{random.randint(1,999)}@{domain}"

def _basic_progress(description, total):
    """Create a basic progress bar with temp1 style"""
    return Progress(
        SpinnerColumn(style="magenta"),
        TextColumn("[bold cyan]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
        TimeRemainingColumn(),
    )

# Main function
def osint_cmd(mode: str = None, value: str = None):
    """
    mode: one of "name", "email", "phone" (case-insensitive)
    value: optional string for the selected mode
    """

    # choose mode
    accepted = ("name", "email", "phone")
    if mode:
        mode = mode.strip().lower()
    while mode not in accepted:
        mode = input("Search by [name/email/phone] (or 'q' to cancel): ").strip().lower()
        if mode in ("q", "quit", "exit"):
            print("Cancelled.")
            return None
        if mode not in accepted:
            print("Please choose one of: name, email, phone.")
            mode = None

    # prompt for value (with validation)
    while True:
        if value:
            value = value.strip()
        else:
            value = input(f"Enter {mode}: ").strip()

        if not value:
            print("Empty input. Enter a value or 'q' to cancel.")
            value = None
            continue

        if value.lower() in ("q", "quit", "exit"):
            print("Cancelled.")
            return None

        if mode == "email" and not _valid_email(value):
            print("That doesn't look like an email. Try again or 'q' to cancel.")
            value = None
            continue

        if mode == "phone" and not _valid_phone(value):
            print("Phone looks invalid (need 7-15 digits). Try again or 'q' to cancel.")
            value = None
            continue

        if mode == "name" and len(value) < 2:
            print("Name must be at least 2 characters. Try again or 'q' to cancel.")
            value = None
            continue

        break  # valid input

    # cinematic initialization
    print("\nInitializing OSINT modules...\n")
    with _basic_progress("Initializing", 80) as progress:
        task = progress.add_task("Initializing", total=80)
        for _ in range(80):
            time.sleep(0.02)
            progress.update(task, advance=1)
    time.sleep(0.25)

    # gathering info
    print(f"\nGathering public traces for {value} ({mode})\n")
    with _basic_progress("Scanning", 120) as progress:
        task = progress.add_task("Scanning", total=120)
        for _ in range(120):
            time.sleep(0.02)
            progress.update(task, advance=1)
    time.sleep(0.2)

    # execution lines
    tw_speed = 0.03

    if mode == "email":
        script_lines = [
            ("[osint]", f"querying public data sources for '{value}'"),
            ("[osint]", "MX / SPF / DKIM and domain reputation check"),
            ("[osint]", "TLS certificate and crt.sh / CAA lookup"),
            ("[osint]", "searching breach DBs (HaveIBeenPwned, DeHashed, compiled leaks)"),
            ("[osint]", "indexing paste sites, archived dumps and Google cache"),
            ("[osint]", "harvesting linked accounts and account reuse patterns"),
            ("[osint]", "checking role vs personal address and inbox exposure"),
            ("[osint]", "extracting headers and SMTP fingerprinting where available"),
            ("[osint]", "assessing risk score (exposure, reuse, domain age)"),
            ("[osint]", "compiling email-centric intelligence summary"),
        ]

    elif mode == "phone":
        script_lines = [
            ("[osint]", f"querying public data sources for '{value}'"),
            ("[osint]", "E.164 normalization and libphonenumber carrier lookup"),
            ("[osint]", "identifying number type (mobile / landline / VOIP)"),
            ("[osint]", "reverse-lookup on public directories and Truecaller-style sources"),
            ("[osint]", "searching paste sites and leaked SMS/OTP archives"),
            ("[osint]", "checking ad-broker records and classifieds for posted numbers"),
            ("[osint]", "correlating number to social profiles and message handles"),
            ("[osint]", "geolocation heuristics from national prefix and exchange"),
            ("[osint]", "number reputation / spam-scoring lookup"),
            ("[osint]", "compiling phone-centric intelligence summary"),
        ]

    else:  # name
        script_lines = [
            ("[osint]", f"querying public data sources for '{value}'"),
            ("[osint]", "scraping social profiles and metadata (Instagram, LinkedIn, X, Facebook, GitHub)"),
            ("[osint]", "harvesting known usernames/aliases and cross-posts"),
            ("[osint]", "extracting media EXIF, image hashes (pHash) and geotags via exiftool"),
            ("[osint]", "searching breach collections, paste sites and indexed archives"),
            ("[osint]", "performing Google dorking and cached page analysis"),
            ("[osint]", "enumerating related domains, blogs and personal pages"),
            ("[osint]", "mapping social graph and follower/following connections"),
            ("[osint]", "checking code repos and public commits for secrets or tokens"),
            ("[osint]", "compiling person-centric intelligence report"),
        ]

    for stub, text in script_lines:
        sys.stdout.write(f"\033[1;31m{stub}\033[0;32m ")
        sys.stdout.flush()
        _typewriter(text, speed=tw_speed)
        time.sleep(random.uniform(0.06, 0.18))

    time.sleep(0.25)

    # build simulated result based on input mode
    if mode == "name":
        name = value.title()
        phone = _random_phone()
        email = _random_email_from_name(name)
    elif mode == "email":
        email = value
        local = (value.split("@",1)[0] if "@" in value else "user")
        # attempt to build a name from local part
        name_guess = re.sub(r"[\d._\-]+", " ", local).strip().title() or "Unknown"
        name = name_guess
        phone = _random_phone()
    else:  # phone
        phone = value
        name = random.choice(["Ahmed Al-Faisal", "Sara Al-Qahtani", "Mohammed Al-Rashid", "Laila A."])
        email = _random_email_from_name(name)

    address = _random_address()
    common_pw = random.sample(_common_passwords, 3)
    gen_pw = _random_password(10)

    # final reveal
    print() 
    sys.stdout.write("\033[1;31m[+]\033[0;32m ")
    sys.stdout.flush()
    _typewriter("OSINT snapshot obtained", speed=TYPEWRITER_SPEED)
    time.sleep(0.12)

    sys.stdout.write("\033[33m") # Switch to yellow
    sys.stdout.flush()
    print("Name     :", name)
    print("Phone    :", phone)
    print("Email    :", email)
    print("Address  :", address)
    print()
    sys.stdout.write("\033[32m") # Back to green
    sys.stdout.flush()
    _typewriter("Common passwords found (top matches):", speed=TYPEWRITER_SPEED)
    for p in common_pw:
        _typewriter(f" - {p}", speed=TYPEWRITER_SPEED)
        time.sleep(0.08)

    _typewriter(f"\nGenerated plausible password: {gen_pw}\n", speed=TYPEWRITER_SPEED)

    # small wrap delay then return results
    time.sleep(0.6)
    return {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
        "common_passwords": common_pw,
        "suggested_password": gen_pw
    }
