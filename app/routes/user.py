from fastapi import APIRouter, Depends, HTTPException, status, Path
from fastapi.responses import JSONResponse

from app.schemas.user import UserModel
from app.models.user_dao import UserDao

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.post("/register")
def register(user: UserModel):
    
    exists = UserDao.get_user_by_email(user.email)
    
    if exists:
        
        raise HTTPException(
            detail={'msg': 'User already exists'},
            status_code=status.HTTP_409_CONFLICT
        )
    
    success = UserDao.register_user_db(user)
    
    if not success:
        
        raise HTTPException(
            detail={'msg': 'User not created'},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
    return JSONResponse(
        content={'msg': 'user created'},
        status_code=status.HTTP_200_OK
    )
    
    