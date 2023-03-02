from  fastapi import APIRouter

from ..controller.usercontroller import UserService

router = APIRouter(prefix="/users",tags=["Users"])

# !http://Localhost:5000/users
@router.get('/')
async def getAllUsers():
    return UserService.get_allUser()

# !http://Localhost:5000/users/me
@router.get('/me')
async def getSingleUser():
    return UserService.getUser()

     

