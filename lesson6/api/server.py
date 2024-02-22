from fastapi import FastAPI

from .controllers import test_controller
from .controllers import items_controller


app = FastAPI(docs_url="/")
app.include_router(items_controller)
app.include_router(test_controller)
