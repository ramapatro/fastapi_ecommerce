from  fastapi import APIRouter

from ..controller.cartcontroller import cartService

router = APIRouter(prefix="/cart",tags=["cart"])

## !http://Localhost:5000/users
@router.get('/')
async def getAllCart():
    return cartService.get_allCart()

# !http://Localhost:5000/users/me
@router.get('/me')
async def getSingleCart():
    return cartService.getUser()

     

