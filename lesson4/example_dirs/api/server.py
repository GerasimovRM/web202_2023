from fastapi import FastAPI
from .controllers import items_controller


app = FastAPI()
app.include_router(items_controller)