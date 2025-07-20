from pydantic import BaseModel, EmailStr
from typing import Optional, Dict

class User(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

class FakeDB:
    _users: Dict[str, User] = {}

    @classmethod
    def add_user(cls, user_id: str, user: User):
        cls._users[user_id] = user

    @classmethod
    def get_user(cls, user_id: str):
        return cls._users.get(user_id)

    @classmethod
    def update_user(cls, user_id: str, user: User):
        cls._users[user_id] = user
