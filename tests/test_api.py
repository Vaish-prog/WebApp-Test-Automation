import requests


def test_get_user():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1

def test_create_user():
    response = requests.post(
        "https://postman-echo.com/post",
        json={
            "name": "Vaishnavi",
            "job": "QA Automation Tester"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["json"]["name"] == "Vaishnavi"
    assert data["json"]["job"] == "QA Automation Tester"

def test_invalid_user():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/999"
    )

    assert response.status_code == 404

def test_update_user():
    response = requests.put(
        "https://jsonplaceholder.typicode.com/users/1",
        json={
            "name": "Vaishnavi Updated",
            "job": "Senior QA Automation Tester"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Vaishnavi Updated"
    assert data["job"] == "Senior QA Automation Tester"


def test_delete_user():
    response = requests.delete(
        "https://jsonplaceholder.typicode.com/users/1"
    )

    assert response.status_code == 200