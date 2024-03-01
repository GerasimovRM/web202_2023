from typing import Optional, List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import session_factory, get_session, User
from model import PhoneOut
from services import AuthService
from services.phone_service import PhoneService

router = APIRouter(prefix="/phone", tags=["phone"])


@router.get("/", response_model=List[PhoneOut])
async def get_all_phones(current_user: User = Depends(AuthService.get_current_user),
                         session: AsyncSession = Depends(get_session)):
    return await PhoneService.get_all_phones_by_user(current_user.id, session)



