from pydantic import BaseModel
from typing import List

class MovieInput(BaseModel):
    title: str
    description: str  # We will use this for content filtering

class RecommendationResponse(BaseModel):
    movie_id: int
    title: str
    match_score: float  # How good is the recommendation?