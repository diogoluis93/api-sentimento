from fastapi import APIRouter
from .models import TextInput, TextAnalysisResult
from .services import analyze_text_service
from .cache import search_term
from .exceptions import not_found_exception

router = APIRouter()

@router.post("/analyze-text", response_model=TextAnalysisResult)
async def analyze_text(input: TextInput):
    return analyze_text_service(input)

@router.get("/search-term", response_model=TextAnalysisResult)
async def search(term: str):
    result = search_term(term.lower())
    if not result:
        not_found_exception()
    return result