from fastapi import FastAPI
from api.routers import maths, strings
app = FastAPI()

app.include_router(maths.router)
app.include_router(strings.router)


