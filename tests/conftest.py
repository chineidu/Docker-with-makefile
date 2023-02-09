from typing import Generator

import pytest
from fastapi.testclient import TestClient

from src.my_app import app


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}


@pytest.fixture()
def response_data() -> dict:
    """This returns the mock response data."""
    _response = {
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
    return _response

