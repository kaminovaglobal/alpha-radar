from fastapi import APIRouter

from services.opportunity_service import get_all

router = APIRouter()


@router.get("/")
def get_opportunities():

    return get_all()