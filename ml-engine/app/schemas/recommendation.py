from pydantic import BaseModel
from typing import List

class MovieInput(BaseModel):
    title: str
    description: str  # We will use this for content filtering