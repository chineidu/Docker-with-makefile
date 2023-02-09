import requests

url = "	https://dummy.restapiexample.com/api/v1/employees"

response = requests.get(url)


def get_employees_data() -> dict:
    """This returns a dict containing employees info."""
    url = "	https://dummy.restapiexample.com/api/v1/employees"
    response = requests.get(url)
    return response