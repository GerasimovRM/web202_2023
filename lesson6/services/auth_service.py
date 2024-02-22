from datetime import datetime, timezone, timedelta

from fastapi import HTTPException
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from config import TOKEN_EXP_IN_MINUTES, SECRET_JWT_KEY
from database import User
from starlette import status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)

    @staticmethod
    async def authenticate_user(login: str,
                                plain_password: str,
                                session: AsyncSession):
        # user = await UserService.get_user_by_login(login, session)
        query = await session.execute(select(User).where(User.login == login))
        user: User = query.scalars().first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"User with login {login} not found")
        if not AuthService.verify_password(plain_password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail=f"Wrong password")
        return user

    @staticmethod
    def create_jwt_token(payload: dict,
                         expire_delta: int | None = None):
        if not expire_delta:
            expire_delta = TOKEN_EXP_IN_MINUTES
        expire = datetime.now(timezone.utc) + timedelta(expire_delta)
        payload = payload.copy()
        payload["exp"] = expire
        jwt_token = jwt.encode(payload, SECRET_JWT_KEY)
        return jwt_token

    @staticmethod
    async def create_access_token_by_user(user: User) -> str:
        payload = {"user_id": user.id}
        access_token = AuthService.create_jwt_token(payload)
        return access_token
