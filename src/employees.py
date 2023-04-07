import requests
from typing import Any


def get_employees_data() -> dict[str, Any]:
    """This returns a dict containing employees info."""
    url = "https://dummy.restapiexample.com/api/v1/employees"
    response = requests.get(url)
    return response # type: ignore
