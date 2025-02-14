from fastapi import APIRouter


router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def create_user():
    return {"status": "ok"}