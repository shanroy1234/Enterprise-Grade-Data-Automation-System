from fastapi import APIRouter
from app.auth import create_token

router=APIRouter(prefix='/admin')

@router.get('/token')
def token():
    return {'token':create_token({'role':'admin'})}
