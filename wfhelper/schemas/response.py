from typing import Any, Optional
from pydantic import BaseModel
from http import HTTPStatus


class ResponseSchema(BaseModel):
    code: int = HTTPStatus.OK.value
    status: str = HTTPStatus.OK.phrase
    message: Optional[str] = None
    data: Optional[Any] = None
