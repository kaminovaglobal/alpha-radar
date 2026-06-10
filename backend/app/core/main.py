from fastapi import FastAPI

app = FastAPI(
    title="Alpha Radar API",
    version="1.0.0"
)


@app.get("/")
def root():

    return {
        "message":
        "Alpha Radar Running"
    }

from fastapi import FastAPI

from app.routers.opportunities import router as opportunities_router

app = FastAPI()

app.include_router(
    opportunities_router,
    prefix="/opportunities",
    tags=["Opportunities"]
)