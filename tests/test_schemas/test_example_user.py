import pytest
from app.schemas import user_schemas

example_user = user_schemas.example_user

def test_user_create_schema_examples():
    model = user_schemas.UserCreate.schema()
    properties = model["properties"]

    assert properties["email"]["example"] == example_user["email"]
    assert properties["password"]["example"] == example_user["password"]

def test_login_request_schema_examples():
    model = user_schemas.LoginRequest.schema()
    properties = model["properties"]

    assert properties["email"]["example"] == example_user["email"]
    assert properties["password"]["example"] == example_user["password"]

def test_user_response_schema_examples():
    model = user_schemas.UserResponse.schema()
    properties = model["properties"]

    assert properties["email"]["example"] == example_user["email"]
    assert properties["nickname"]["example"] == example_user["nickname"]
    assert properties["id"]["example"] == example_user["id"]

def test_user_list_response_schema_example():
    model = user_schemas.UserListResponse.schema()
    example = model["properties"]["items"]["example"][0]

    assert example["email"] == example_user["email"]
    assert example["nickname"] == example_user["nickname"]
    assert example["id"] == example_user["id"]
