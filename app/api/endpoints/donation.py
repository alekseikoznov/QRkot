from fastapi import APIRouter, Depends
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.schemas.donation import (DonationCreate,
                                  UserDonationDB,
                                  DonationDB)
from app.services.investing import get_projects_for_donation

router = APIRouter()


@router.post(
    '/',
    response_model=UserDonationDB,
    response_model_exclude_none=True,
)
async def create_new_donation(
        donation: DonationCreate,
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session),
):
    """Сделать пожертвование."""
    new_donation = await donation_crud.create(donation, session, user)
    donation_after_investing = await get_projects_for_donation(new_donation, session)
    return donation_after_investing


@router.get(
    '/my',
    response_model=List[UserDonationDB],
)
async def get_user_donations(
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session),
):
    """Вернуть список пожертвований пользователя, выполняющего запрос."""
    all_donations = await donation_crud.get_user_donations(user, session)
    return all_donations


@router.get(
    '/',
    dependencies=[Depends(current_superuser)],
    response_model_exclude_none=True,
    response_model=List[DonationDB],
)
async def get_all_donations(
        session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.

    Возвращает список всех пожертвований.
    """
    all_donations = await donation_crud.get_multi(session)
    return all_donations