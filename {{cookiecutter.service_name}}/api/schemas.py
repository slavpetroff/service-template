"""
This module contains the schemas for the API.

The schemas are used to validate the data (request body, query parameters, etc.)
and to serialize the data returned from the API.

"""

from typing import Optional

from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    """
    Schema for a user accepted by the API.
    """

    username: str = Field(..., min_length=1, max_length=50, strip_whitespace=True)
    email: str = Field(..., min_length=1, max_length=50, strip_whitespace=True)
    password: str = Field(..., min_length=1, max_length=50, strip_whitespace=True)


class User(BaseModel):
    """
    Schema for a user returned from the API.
    """

    id: int
    username: str
    email: str


class UserUpdate(BaseModel):
    """
    Schema for a user update accepted by the API.
    """

    username: Optional[str] = Field(
        None, min_length=1, max_length=50, strip_whitespace=True
    )
    email: Optional[str] = Field(
        None, min_length=1, max_length=50, strip_whitespace=True
    )
    password: Optional[str] = Field(
        None, min_length=1, max_length=50, strip_whitespace=True
    )


class UserDelete(BaseModel):
    """
    Schema for a user deletion accepted by the API.
    """

    id: int
