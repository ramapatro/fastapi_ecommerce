from  fastapi import APIRouter

from ..controller.productController import ProductService

router = APIRouter(prefix="/products",tags=["products"])

# !http://Localhost:5000/users
@router.get('/')
async def getAllProducts():
    return ProductService.get_AllProducts()

# !http://Localhost:5000/users/me
@router.get('/me')
async def getSingleProducts():
    return ProductService.getProduct()

     

