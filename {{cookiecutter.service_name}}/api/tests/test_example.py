from api.schemas import User

BASE_API_URL = "/api"
TARGET_URL = f"{BASE_API_URL}/users"


def test_create_user(client):
    response = client.post(
        TARGET_URL,
        json={"username": "test", "email": "test@gmail.com", "password": "test"},
    )
    assert response.status_code == 201, response.text
    assert response.json() == User(**response.json()).model_dump()


def test_get_user(client):
    response_create = client.post(
        TARGET_URL,
        json={"username": "test", "email": "test@gmail.com", "password": "test"},
    )
    assert response_create.status_code == 201, response_create.text
    user_data = User(**response_create.json()).model_dump()
    assert response_create.json() == user_data

    response_get = client.get(f"{TARGET_URL}/{user_data.get('id')}")
    assert response_get.status_code == 200, response_get.text
    assert response_get.json() == user_data


def test_update_user(client):
    # Create the user first
    response_create = client.post(
        TARGET_URL,
        json={"username": "test", "email": "test@gmail.com", "password": "test"},
    )
    assert response_create.status_code == 201, response_create.text
    user_data = User(**response_create.json()).model_dump()
    assert response_create.json() == user_data

    # Update user's email
    response_update = client.put(
        f"{TARGET_URL}/{user_data.get('id')}",
        json={"email": "new_test@gmail.com"},
    )
    assert response_update.status_code == 200, response_update.text
    updated_user_data = User(**response_update.json()).model_dump()
    assert response_update.json() == updated_user_data
    assert (
        updated_user_data["email"] == "new_test@gmail.com"
    )  # confirm the email has been updated


def test_delete_user(client):
    # Create the user first
    response_create = client.post(
        TARGET_URL,
        json={"username": "test", "email": "test@gmail.com", "password": "test"},
    )
    assert response_create.status_code == 201, response_create.text
    user_data = User(**response_create.json()).model_dump()
    assert response_create.json() == user_data

    # Delete the user
    response_delete = client.delete(f"{TARGET_URL}/{user_data.get('id')}")
    assert response_delete.status_code == 204  # No content

    # Try to get the user again
    response_get = client.get(f"{TARGET_URL}/{user_data.get('id')}")
    assert response_get.status_code == 404  # User not found
