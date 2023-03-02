
from  fastapi import APIRouter

from ..controller.categorycontroller import categoryService

router = APIRouter(prefix="/category",tags=["category"])

## !http://Localhost:5000/users
@router.get('/')
async def getAllCategory():
    return categoryService.get_allCategory()

# !http://Localhost:5000/users/me
@router.get('/me')
async def getSinglecategory():
    return categoryService.getCategory()

     

