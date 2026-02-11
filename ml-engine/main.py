from fastapi import FastAPI, HTTPException
from app.core.engine import get_content_recommendations
from app.schemas.recommendation import RecommendationResponse
from typing import List

app = FastAPI(title="CinePulse ML Engine", version="1.0")

@app.get("/")
def health_check():
    return {"status": "active", "model": "TF-IDF Content Filtering"}


@app.get("/recommend/{movie_title}", response_model=List[RecommendationResponse])
def recommend(movie_title: str):
    """
    Returns a list of recommended movies based on the content of the provided movie title.
    """
    recommendations = get_content_recommendations(movie_title)
    
    if not recommendations:
        raise HTTPException(status_code=404, detail="Movie not found or no recommendations available")
        
    return recommendations

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)