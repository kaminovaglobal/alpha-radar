from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def grants():

    return [
        {
            "program":
            "Optimism Grant",

            "amount":
            50000
        }
    ]