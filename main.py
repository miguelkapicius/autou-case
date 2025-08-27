from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# uvicorn main:app --reload

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

from app.api.routes import router  # noqa: E402

app.include_router(router)


