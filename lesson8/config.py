import os

from dotenv import load_dotenv

if not os.getenv("DOCKER"):
    load_dotenv(".env")

DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")
print(DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST)
SQL_ECHO = True if os.getenv("SQL_ECHO") in ("True", "true", "1") else False

TOKEN_EXP_IN_MINUTES = int(os.getenv("TOKEN_EXP_IN_MINUTES"))

SECRET_JWT_KEY = os.getenv("SECRET_JWT_KEY")
