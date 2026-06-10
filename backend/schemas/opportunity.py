from pydantic import BaseModel


class OpportunityResponse(
    BaseModel
):
    title: str
    category: str
    score: int