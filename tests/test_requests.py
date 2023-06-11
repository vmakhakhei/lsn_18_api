from requests import Response
from pytest_voluptuous import S
from schemas.reqresin import list_users_schema, post_user_schema, get_user_schema


def test_get_users_page_number(reqres):
    response: Response = reqres.get('/users?page=2')
    assert response.status_code == 200
    assert response.json()["page"] == 2


def test_get_users_per_page(reqres):
    response: Response = reqres.get('/users?page=2')
    per_page = response.json()["per_page"]
    data_len = len(response.json()["data"])
    assert data_len == per_page


def test_get_users_validate_schema(reqres):
    response: Response = reqres.get('/users?page=2')

    assert S(list_users_schema) == response.json()


def test_get_user_validate_schema(reqres):
    response: Response = reqres.get('/users/2')

    assert S(get_user_schema) == response.json()


def test_post_user_validate_schema(reqres):
    response: Response = reqres.post('/users', data={"name": "morpheus", "job": "leader"})

    assert S(post_user_schema) == response.json()


def test_post_user_status_code(reqres):
    response: Response = reqres.post('/users', data={"name": "morpheus", "job": "leader"})

    assert response.status_code == 201


def test_create_user_validate_input_data(reqres):
    response: Response = reqres.post(
        '/users', data={"name": "uladzislau", "job": "leader"}
    )

    assert response.json()["name"] == "uladzislau"
    assert response.json()["job"] == "leader"


def test_user_not_found(reqres):
    response: Response = reqres.get('/users/23')

    assert response.status_code == 404


def test_update_user_data(reqres):
    response: Response = reqres.post(
        '/users/2', data={"name": "morpheus", "job": "zion resident"}
    )
    assert response.json()["name"] == "morpheus"


def test_delete_user(reqres):
    response: Response = reqres.delete('/users/2')

    assert response.status_code == 204
