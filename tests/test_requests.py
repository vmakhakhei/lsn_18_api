import requests
from requests import Response
from pytest_voluptuous import S

from schemas.reqresin import list_users_schema, post_user_schema, get_user_schema


def test_get_users_page_number():
    url = "https://reqres.in/api/users?page=2"
    response: Response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["page"] == 2


def test_get_users_per_page():
    url = "https://reqres.in/api/users?page=2"
    response: Response = requests.get(url)
    per_page = response.json()["per_page"]
    data_len = len(response.json()["data"])
    assert data_len == per_page


def test_get_users_validate_schema():
    url = "https://reqres.in/api/users?page=2"

    response: Response = requests.get(url)

    assert S(list_users_schema) == response.json()


def test_get_user_validate_schema():
    url = "https://reqres.in/api/users/2"

    response: Response = requests.get(url)

    assert S(get_user_schema) == response.json()


def test_post_user_validate_schema():
    url = "https://reqres.in/api/users"

    response: Response = requests.post(url, data={"name": "morpheus", "job": "leader"})

    assert S(post_user_schema) == response.json()


def test_post_user_status_code():
    url = "https://reqres.in/api/users"

    response: Response = requests.post(url, data={"name": "morpheus", "job": "leader"})

    assert response.status_code == 201


def test_create_user_validate_input_data():
    url = "https://reqres.in/api/users"

    response: Response = requests.post(
        url, data={"name": "uladzislau", "job": "leader"}
    )

    assert response.json()["name"] == "uladzislau"
    assert response.json()["job"] == "leader"


def test_user_not_found():
    url = "https://reqres.in/api/users/23"
    response: Response = requests.get(url)

    assert response.status_code == 404


def test_update_user_data():
    url = "https://reqres.in/api/users/2"
    response: Response = requests.post(
        url, data={"name": "morpheus", "job": "zion resident"}
    )
    assert response.json()["name"] == "morpheus"


def test_delete_user():
    url = "https://reqres.in/api/users/2"
    response: Response = requests.delete(url)

    assert response.status_code == 204
