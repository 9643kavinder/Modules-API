from fastapi import APIRouter, HTTPException, status
from ..repository import maths

router = APIRouter(
    prefix="/maths",
    tags=['Maths']
)


@router.get('/fibonacci')
def fibonacci(num: int):
    # check is n is less than 0
    if num <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="Number should be greater than 0.")
    return maths.get_fibonacci(num)


@router.get('/factorial')
def factorial(num: int):
    if num < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="Number should be non-negative.")
    return maths.get_factorial(num)
