from pathlib import Path
from my_app.main import app as app

import my_app

PACKAGE_ROOT = Path(my_app.__file__).absolute().parent
ROOT_DIR = PACKAGE_ROOT.parent.parent

# Import the VERSION
with open(ROOT_DIR / "VERSION", "r") as file:
    __version__ = file.read().strip()
