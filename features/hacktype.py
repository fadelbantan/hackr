import sys, random, time, select
try:
    import tty, termios
except ImportError:
    tty = termios = None

# Load the large synthetic payload. Provide a small safe fallback if unavailable.
try:
    from data.hacktype_code import DEFAULT_CODE as LARGE_DEFAULT_CODE
except Exception:
    LARGE_DEFAULT_CODE = """#!/usr/bin/env python3\n# Fallback minimal payload\nprint('fallback payload active')\n"""


def _load_fake_code():
    # Return the large code snippet used by hacktype mode.
    return LARGE_DEFAULT_CODE


def _clear_screen():
    # Use ANSI full reset clear for a blank (black) screen.
    sys.stdout.write("\033c")
    sys.stdout.flush()

def hacktype_cmd(username=None, flags=None):
    """
    Hacktype mode: mash keys to generate code.
    
    Flags:
        --fast: faster typing (4-7 chars per keypress)
        --slow: slower typing (1-3 chars per keypress)
    """
    code = _load_fake_code()
    idx = 0
    
    # Parse flags
    fast = False
    slow = False
    
    if flags:
        flags_lower = [f.lower() for f in flags]
        fast = "--fast" in flags_lower
        slow = "--slow" in flags_lower
    
    # Determine chunk size based on speed flags
    if fast:
        chunk_min, chunk_max = 4, 7
        speed_desc = "FAST"
    elif slow:
        chunk_min, chunk_max = 1, 3
        speed_desc = "SLOW"
    else:
        chunk_min, chunk_max = 2, 5
        speed_desc = "NORMAL"
    
    _clear_screen()
    # Single instruction line only.
    print("Press ESC to exit.\n")

    # Single cbreak loop for ESC/Ctrl+C detection and typing
    fd = sys.stdin.fileno() if tty and termios else None
    old_settings = termios.tcgetattr(fd) if fd is not None else None
    try:
        if fd is not None:
            tty.setcbreak(fd)
        while True:
            r, _, _ = select.select([sys.stdin], [], [], None)
            if not r:
                continue
            ch = sys.stdin.read(1)
            if ch == '\x03': # Ctrl+C
                print("\nExiting hacktype mode...\n")
                break
            if ch == '\x1b': # ESC
                # Peek small window for sequence continuation
                r2, _, _ = select.select([sys.stdin], [], [], 0.02)
                if not r2:
                    print("\nExiting hacktype mode...\n")
                    break
                # Consume sequence bytes (ignore arrows etc.)
                while True:
                    r3, _, _ = select.select([sys.stdin], [], [], 0.0)
                    if not r3:
                        break
                    _ = sys.stdin.read(1)
                continue
            # Normal key prints chunk
            chunk_size = random.randint(chunk_min, chunk_max)
            chunk = code[idx: idx + chunk_size]
            if not chunk:
                idx = 0
                time.sleep(0.05)
                continue
            idx += len(chunk)
            sys.stdout.write(chunk)
            sys.stdout.flush()
    finally:
        if fd is not None and old_settings is not None:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
