"""Assert that hello.py prints the expected greeting."""

import subprocess
import sys
from pathlib import Path

EXPECTED = "hello from agent-sandbox"

result = subprocess.run(
    [sys.executable, str(Path(__file__).parent / "hello.py")],
    capture_output=True,
    text=True,
    check=True,
)
output = result.stdout.strip()

assert output == EXPECTED, f"expected {EXPECTED!r}, got {output!r}"
print(f"PASS: hello.py output == {EXPECTED!r}")
