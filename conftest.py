import pytest
from helper import BaseSession


@pytest.fixture(scope="session")
def reqres():
    reqres_session = BaseSession(base_url="https://reqres.in/api")
    return reqres_session
