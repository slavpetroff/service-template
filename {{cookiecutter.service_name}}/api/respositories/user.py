from fastapi import Depends
from sqlalchemy.orm import Session

from api.core.database.connection import get_session
from api.models.user import UserModel
from api.respositories.common import BaseRepository


class UserRepository(BaseRepository):
    """
    Repository class for a User model
    """

    def __init__(self, db_session: Session):
        super(UserRepository, self).__init__(UserModel, db_session)

    def get_user_by_email(self, email):
        return self.filter(email=email)

    def get_user_by_username(self, username):
        return self.filter(username=username)

    def get_user_by_pk(self, pk):
        return self.get(pk)


def get_user_repository(session: Session = Depends(get_session)) -> UserRepository:
    """
    Dependency to get a User repository instance

    :param session: SQLAlchemy session
    :return: User repository instance
    """
    return UserRepository(session)
