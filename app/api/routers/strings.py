from fastapi import APIRouter
from ..repository import strings

router = APIRouter(
    prefix="/strings",
    tags=['Strings']
)


@router.get('/length')
def length_of_string(item: str):
    return strings.get_length(item)


@router.get('/generate')
def generate_string(num: int, item: str):
    return strings.get_generated_string(num, item)
