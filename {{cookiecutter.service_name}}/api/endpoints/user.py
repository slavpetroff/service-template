from fastapi import Depends, HTTPException

from api.respositories.user import UserRepository, get_user_repository
from api.schemas import User, UserCreate, UserUpdate
from fastapi import APIRouter

router = APIRouter()


@router.get("/{user_id}", response_model=User)
async def get_user(
    user_id: int,
    user_repo: UserRepository = Depends(get_user_repository),
):
    user = user_repo.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=User, status_code=201)
async def create_user(
    user: UserCreate,
    user_repo: UserRepository = Depends(get_user_repository),
):
    new_user = user_repo.create(
        **user.model_dump(exclude_unset=True, exclude_none=True)
    )
    return new_user


@router.put("/{user_id}", response_model=User)
async def update_user(
    user_id: int,
    user: UserUpdate,
    user_repo: UserRepository = Depends(get_user_repository),
):
    user_dict = user.model_dump(exclude_none=True, exclude_unset=True)
    db_user = user_repo.update(user_id, **user_dict)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/{user_id}", status_code=204)
async def delete_user(
    user_id: int,
    user_repo: UserRepository = Depends(get_user_repository),
):
    if not user_repo.filter(id=user_id):
        raise HTTPException(status_code=404, detail="User not found")

    user_repo.delete(user_id)
