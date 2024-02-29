from datetime import datetime, timezone, timedelta
from typing import Annotated

from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from config import TOKEN_EXP_IN_MINUTES, SECRET_JWT_KEY
from database import User, get_session
from starlette import status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


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
                         expire_delta: int | None = None) -> str:
        if not expire_delta:
            expire_delta = TOKEN_EXP_IN_MINUTES
        expire = datetime.now(timezone.utc) + timedelta(expire_delta)
        payload = payload.copy()
        payload["exp"] = expire
        jwt_token = jwt.encode(payload, SECRET_JWT_KEY, "HS256")
        return jwt_token

    @staticmethod
    def create_access_token_by_user(user: User) -> str:
        payload = {"user_id": user.id, "login": user.login}
        access_token = AuthService.create_jwt_token(payload)
        return access_token

    @staticmethod
    async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)],
                               session: AsyncSession = Depends(get_session)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_JWT_KEY, algorithms=["HS256"])
            user_id: str = payload.get("user_id")
            if user_id is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        query = await session.execute(select(User).where(User.id == user_id))
        user: User = query.scalars().first()
        if user is None:
            raise credentials_exception
        return user
