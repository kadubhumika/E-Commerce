from fastapi import Depends, HTTPException
from core.dependencies import get_current_user


async def admin_required(
        current_user=Depends(get_current_user)
):

    if current_user.role != "admin":

        raise HTTPException(
            status_code=403,
            detail="Admin only"
        )

    return current_user


async def customer_required(
        current_user=Depends(get_current_user)
):

    if current_user.role != "customer":

        raise HTTPException(
            status_code=403,
            detail="Customer only"
        )

    return current_user