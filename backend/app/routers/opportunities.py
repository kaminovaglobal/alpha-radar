from fastapi import APIRouter

# This variable name must match exactly what you are trying to import in main.py
router = APIRouter()

@router.get("/")
def get_opportunities():
    return [
        {
            "title": "Monad Testnet",
            "category": "AIRDROP",
            "score": 92
        }
    ]