from fastapi import APIRouter
from app.services.test import get_version, get_time, get_principal

router = APIRouter(prefix="/test", tags=["test"])

@router.get("/version")
def test_version():
    return get_version()

@router.get("/time")
def test_time():
    return get_time()

@router.get("/principal")
def test_principal():
    return get_principal()
