from fastapi import APIRouter
from wfhelper.services import RepoService
from wfhelper.schemas import ResponseSchema


router = APIRouter(prefix="/repo", tags=["repo"])

@router.get("/clone")
def git_clone():
    resp = ResponseSchema()
    RepoService.git_clone()
    return resp
