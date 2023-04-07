import numpy as np


def roll_die() -> int:
    """This returns an integer between 1 and 6 (inclusive)."""
    number = np.random.choice(a=np.arange(1, 7), size=1)[0]
    return number
