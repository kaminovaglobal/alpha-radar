from fastapi import APIRouter, Depends
from .dependencies import get_current_user

router = APIRouter()

@router.post("/register")
def register():
    return {"message": "registered"}

@router.post("/login")
def login():
    return {"token": "sample_token"}

@router.get("/profile")
def profile(user=Depends(get_current_user)):
    return {"user": user}