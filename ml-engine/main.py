from fastapi import FastAPI, HTTPException
from app.core.engine import get_content_recommendations
from app.schemas.recommendation import RecommendationResponse
from typing import List

app = FastAPI(title="CinePulse ML Engine", version="1.0")