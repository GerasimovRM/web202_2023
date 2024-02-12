from typing import Optional, List

from sqlalchemy.orm import Session

from database import Language


class LanguageService:
    @staticmethod
    def get_language_by_id(language_id: int,
                           session: Session) -> Optional[Language]:
        return session.query(Language).get(language_id)

    @staticmethod
    def get_all_languages(session: Session) -> List[Language]:
        return session.query(Language).all()
