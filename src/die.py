from src.utils import roll_die


def guess_number(*, number: int) -> str:
    """This returns `You won!` if you guessed the
    number correctly otherwise `You lost`."""
    actual_number = roll_die()
    result = "You won!" if actual_number == number else "You lost"
    return result
