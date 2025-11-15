import time
from rich.console import Console

DEFAULT_STYLE = "green"

# Shared console instance so every module keeps the same styling defaults.
console = Console(style=DEFAULT_STYLE)

def typewriter(text: str, speed: float = 0.005):
    """Render text with a simple typewriter effect using the default console style."""
    for ch in str(text):
        console.print(ch, end="", markup=False, highlight=False, flush=True)
        time.sleep(speed)
    console.print()
