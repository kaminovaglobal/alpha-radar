from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def jobs():

    return [
        {
            "title":
            "Security Researcher",

            "company":
            "Monad"
        }
    ]