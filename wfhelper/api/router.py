from fastapi import APIRouter
from wfhelper.api.v1 import repo
from wfhelper.schemas import ResponseSchema

router = APIRouter()

# Include routers from API modules
router.include_router(repo.router)


@router.get("/healthcheck")
def healthcheck():
    resp = ResponseSchema()
    resp.message = "healthy"
    return resp
