from pydantic import BaseModel, Field
from typing import List, Tuple

class TextInput(BaseModel):
    text: str = Field(..., json_schema_extra={"example": "Hoje o dia está ótimo"})

class TextAnalysisResult(BaseModel):
    word_count: int
    top_words: List[Tuple[str, int]]
    sentiment: str