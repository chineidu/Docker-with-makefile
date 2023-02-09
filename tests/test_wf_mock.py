from unittest import mock
import pytest

from src.die import guess_number, roll_die
from src.employees import get_employees_data


data = {
    "status": "success",
    "data": [
        {
            "id": 1,
            "employee_name": "Tiger Nixon",
            "employee_salary": 320800,
            "employee_age": 61,
            "profile_image": "",
        },
        {
            "id": 2,
            "employee_name": "Garrett Winters",
            "employee_salary": 170750,
            "employee_age": 63,
            "profile_image": "",
        },
    ],
}


def test_roll_die() -> None:
    """This tests the roll dice function."""
    # Given
    expected_result = 4
    # Mock "roll_die"
    mock_roll_dice = mock.Mock(name="roll_dice", return_value=4)
    roll_die = mock_roll_dice

    # When
    result = roll_die()

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
    expected_result, number = output, 4
    mock_roll_die.return_value = number

    # When
    result = guess_number(number=input_)

    # Then
    assert expected_result == result
    mock_roll_die.assert_called()


@mock.patch("src.employees.requests.get")
def test_get_employees_data(mock_requests_get: mock.Mock) -> None:
    """This tests the get_employees_data function."""
    # Given# Mock `requests.get`
    mock_resp = mock.Mock(
        name="mock response",
        **{"status_code": 200, "json.return_value": data},
    )
    mock_requests_get.return_value = mock_resp
    status_code, status = 200, "success"
    data_size, url = 2, "https://dummy.restapiexample.com/api/v1/employees"

    # When
    result = get_employees_data()

    # Then
    assert result.json() == data
    assert result.status_code == status_code
    assert result.json()["status"] == status
    assert len(result.json()["data"]) == data_size
    mock_requests_get.assert_called_with(url)
