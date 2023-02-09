from unittest import mock
import pytest

from src.die import guess_number


def test_roll_die() -> None:
    """This tests the roll dice function."""
    # Given
    expected_result = 4
    mock_roll_dice = mock.Mock(name="roll_dice", return_value=4)

    # When
    result = mock_roll_dice()

    # Then
    assert expected_result == result
    mock_roll_dice.assert_called()


# Call the function from the location of guess_number()
# i.e the location where another function is using it.
@mock.patch("src.die.roll_die")
def test_guess_number(mock_roll_die) -> None:
    """This tests the roll dice function."""
    # Given
    expected_result = "You won!"
    number = 4
    mock_roll_die.return_value = number

    # When
    result = guess_number(number=number)

    # Then
    assert expected_result == result
    mock_roll_die.assert_called()


@pytest.mark.parametrize("input_, output", [(1, "You lost"), (2, "You lost"), (4, "You won!")])
@mock.patch("src.die.roll_die")
def test_guess_number_2(mock_roll_die, input_, output) -> None:
    """This tests the roll dice function."""
    # Given
    expected_result = output
    number = 4
    mock_roll_die.return_value = number

    # When
    result = guess_number(number=input_)

    # Then
    assert expected_result == result
    mock_roll_die.assert_called()


@mock.patch("")
def test_get_employees_data(response_data:dict) -> None:
    """This tests the get_employees_data function."""
    # Given
    status_code = 200
    status = "success"
    data_size = 2

    # When
    result = mock_get_employees_data()

    # Then
    assert mock_get_employees_data.json() == response_data
    assert mock_get_employees_data.status_code == 200
    assert mock_get_employees_data.json()["status"] == status
    assert len(mock_get_employees_data.json()["data"]) == data_size
