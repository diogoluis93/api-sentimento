from fastapi import HTTPException

def not_found_exception():
    raise HTTPException(status_code=404, detail="Termo não encontrado")