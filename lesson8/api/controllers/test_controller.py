from typing import Optional, List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from starlette import status

from database import session_factory, Language, get_session, User
from model import LanguageIn, LanguageOut
from model.user.user_in import UserIn
from model.user.user_out import UserOut
from services import LanguageService
from services.auth_service import AuthService
from services.user_service import UserService

router = APIRouter(prefix="/test", tags=["test"])


@router.post("/", response_model=Optional[UserOut])
async def test(user_in: UserIn,
               session: AsyncSession = Depends(get_session)):
    new_user = await UserService.create_user(user_in, "123", session)
    return UserOut(**new_user.to_dict())


@router.get("/example_jwt", response_model=UserOut)
async def example_jwt(resourse_id: int,
        current_user: User = Depends(AuthService.get_current_user)):

    return UserOut(**current_user.to_dict())
