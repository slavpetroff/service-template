# API Documentation

This document provides an overview of the API endpoints available in the microservice.

---

## Endpoints

### 1. `GET /`

- **Description**: Retrieves information about the microservice.
- **Response**:
  - Status Code: 200 OK
  - Body:
    ```json
    {
        "message": "Welcome to the Microservice API"
    }
    ```

### 2. `POST /users`

- **Description**: Creates a new user.
- **Request Body**:
  - `username` (string): The username of the user.
  - `email` (string): The email address of the user.
- **Response**:
  - Status Code: 201 Created
  - Body:
    ```json
    {
        "id": 1,
        "username": "example_user",
        "email": "user@example.com"
    }
    ```

### 3. `GET /users/{user_id}`

- **Description**: Retrieves information about a specific user.
- **Path Parameters**:
  - `user_id` (integer): The unique identifier of the user.
- **Response**:
  - Status Code: 200 OK
  - Body:
    ```json
    {
        "id": 1,
        "username": "example_user",
        "email": "user@example.com"
    }
    ```

### 4. `PUT /users/{user_id}`

- **Description**: Updates information about a specific user.
- **Path Parameters**:
  - `user_id` (integer): The unique identifier of the user.
- **Request Body**:
  - `username` (string): The updated username of the user.
  - `email` (string): The updated email address of the user.
- **Response**:
  - Status Code: 200 OK
  - Body:
    ```json
    {
        "id": 1,
        "username": "updated_user",
        "email": "updated@example.com"
    }
    ```

### 5. `DELETE /users/{user_id}`

- **Description**: Deletes a specific user.
- **Path Parameters**:
  - `user_id` (integer): The unique identifier of the user.
- **Response**:
  - Status Code: 204 No Content

---

This document provides a summary of the available endpoints, their descriptions, request parameters, response formats, and status codes. Adjust the content based on your microservice's specific API endpoints and functionalities.
