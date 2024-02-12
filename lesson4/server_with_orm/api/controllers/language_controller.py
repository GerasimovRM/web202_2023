from typing import Optional, List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import session_factory, Language
from model import LanguageIn, LanguageOut
from services import LanguageService

router = APIRouter(prefix="/language", tags=["language"])


@router.get("/{id}", response_model=Optional[LanguageOut])
async def get_language(language_id: int,
                       ):
    session: Session = session_factory()
    language = LanguageService.get_language_by_id(language_id, session)
    if language:
        return LanguageOut(**language.to_dict())
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Language with id {language_id} not found!")


@router.get("/", response_model=List[LanguageOut])
async def get_languages():
    session: Session = session_factory()
    languages = LanguageService.get_all_languages(session)
    return list(map(lambda x: LanguageOut(**x.to_dict()), languages))


# @router.get("/", response_model=List[languageOut])
# async def get_language():
#     return database["language"]

#
# @router.post("/", response_model=languageOut)
# async def create_language(language: languageIn):
#     global current_count
#     # здесь колхоз!
#     # db_language = languageOut(id=current_count,
#     #                   tax=language.tax,
#     #                   price=language.price,
#     #                   description=language.description,
#     #                   name=language.name)
#     db_language = languageOut(id=current_count,
#                       **language.model_dump())
#     current_count += 1
#     database["language"].append(db_language)
#     return db_language
#
#
# @router.put("/", response_model=languageOut)
# async def update_language(language: languageOut):
#     index, db_language = next(filter(lambda x: x[1].id == language.id, enumerate(database["language"])), (-1, None))
#     if not db_language:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="language not found")
#     database["language"][index] = language
#     return db_language
#
#
# @router.delete("/")
# async def update_language(id: int):
#     index, db_language = next(filter(lambda x: x[1].id == id, enumerate(database["language"])), (-1, None))
#     if not db_language:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="language not found")
#     database["language"].pop(index)
#     return {"status": "OK"}