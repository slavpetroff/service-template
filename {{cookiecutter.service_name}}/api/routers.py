"""
This file contains the API routers.

The routers are used to define the API endpoints and the operations
that can be performed on them.
"""

from fastapi import APIRouter
from api.endpoints import user

router = APIRouter()

router.include_router(user.router, prefix="/users", tags=["users"])
