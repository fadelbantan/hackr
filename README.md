```bash
██╗  ██╗ █████╗  ██████╗██╗  ██╗██████╗ 
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔══██╗
███████║███████║██║     █████╔╝ ██████╔╝
██╔══██║██╔══██║██║     ██╔═██╗ ██╔══██╗
██║  ██║██║  ██║╚██████╗██║  ██╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
```

**hackr** is a terminal hacker simulator mocking movie hacking scenes.  
It’s a safe, offline way to play with “hacking” flows while actually learning more about the command line, scripting, and how real tools *could* work under the hood.

---

## Features

- **Movie-style terminal experience**  
  Typewriter effects, animated progress bars, and styled text to mimic cinematic hacking.

- **Website "hacking" simulation**  
  A guided flow that pretends to enumerate a target website (e.g. `example.com`) using fake but realistic-sounding steps.

- **Social media "OSINT" simulation**  
  Simulated lookup of public social media and username-related info, with randomised output.

- **Modular command system**  
  Commands like `socials` and `website` are implemented as separate features, making it easy to add more.

- **Harmless by design**  
  No real attacks, scanning, or network calls. Everything is simulated for fun and learning.

---


## Installation

```bash
# Clone the repository
git clone https://github.com/fadelbantan/hackr.git
cd hackr

# (Optional) Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Finally
./hackr.sh
```
---
## Tech Stack

- **Language:** Python 3
- **CLI UI:**
  - `pyfiglet` for ASCII art banners
  - `alive-progress` for animated progress bars
  - (Optional) `rich` or standard ANSI escape codes for coloring
- **Structure:**
  - `main.py` entry point
  - Commands separated into `features/` modules (e.g. `social_media.py`, `website.py`)

---

## Why I Built hackr

My interest in tech started with **cyber security and hacking**.

I was fascinated by terminals full of fast-scrolling text, progress bars, and the idea of breaking into systems (ethically). That curiosity pulled me into learning more about how computers actually work: networks, operating systems, and security concepts.

From there, I discovered **software development**.

I realised that all the tools, scanners, and “hacker” utilities I admired were just software someone had written. If I could build those tools myself, I’d understand both sides: how to attack and how to defend.

**hackr** is my way of connecting those two stages of my journey:

- It looks and feels like a hacker terminal.
- Under the hood, it’s a real software project that helped me learn:
  - Python
  - Structuring a CLI app
  - Working with libraries for UI, text rendering, and progress bars
  - Basic simulated OSINT / scanning flows

