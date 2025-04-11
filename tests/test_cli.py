import subprocess
import sys

from service import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "service", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
