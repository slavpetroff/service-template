from sqlalchemy import Column, Integer, String, Boolean

from api.models import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    is_active = Column(Boolean(), default=True)
