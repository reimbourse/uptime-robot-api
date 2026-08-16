from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_async_session
from src.schemas.user import UserCreate, UserRead, UserLogin, Token
from src.models.user import User
from src.services.auth import AuthService

router = APIRouter(prefix='/auth', tags=['Auth'])

@router.post('/register', response_model=UserRead)
async def register(data: UserCreate, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(User).where(User.email == data.email))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail='Email already registered')
    hashed_password = AuthService.hash_password(data.password)
    new_user = User(username=data.username,
                    email=data.email,
                    hashed_password=hashed_password)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

@router.post('/login', response_model=Token)
async def login(data: UserLogin, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(User).where(data.email == User.email))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=400, detail='Invalid email or password')
    if not AuthService.check_password(data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail='Invalid email or password')
    token = AuthService.create_access_token(user_id=user.id)

    return {'access_token': token, 'token_type': 'bearer'}
