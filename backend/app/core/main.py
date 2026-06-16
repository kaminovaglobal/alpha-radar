from fastapi import FastAPI
from prometheus_client import Counter
from prometheus_client import generate_latest
from app.routers.opportunities import router as opportunities_router
# 1. Import your new auth router (adjust the path if your directory uses a different structure)
from auth.routes import router as auth_router

# Initialize the single, main FastAPI application instance
app = FastAPI(
    title="Alpha Radar API",
    version="1.0.0"
)

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Alpha Radar Running"
    }

# 2. Register the Opportunities Router
app.include_router(
    opportunities_router,
    prefix="/opportunities",
    tags=["Opportunities"]
)

# 3. Register the Authentication Router (Adding the new code)
app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)