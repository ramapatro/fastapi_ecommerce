import strawberry
import uvicorn
from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from strawberry.fastapi import GraphQLRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from application.routes import productRoutes,userRoutes,cartRoutes,categoryRoutes

description = """
ChimichangApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""
tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello sup"
schema = strawberry.Schema(Query)
graphql_app= GraphQLRouter(schema)
    
app = FastAPI(title="E_commerce",description="check all thing about E_commerce",version=2.0,
              openapi_tags=tags_metadata,openapi_url='/supE_commerce.json',
              docs_url='/docs',
              contact={
        "name": "supriya",
        "url": "http://supriya.netlify.app/",
        "email": "dp@x-force.example.com",},
        license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",})

## mount in the browser
app.mount("/static",StaticFiles(directory="dist"),name="static")
templates= Jinja2Templates(directory="templates")


# @app.get('/')
# async def users():
#     return {
#         "status":200,
#         "hello":"this is subhalaxmi"
#     }
##endpoint(restapi)
@app.get("/index",response_class=HTMLResponse)
async def gethome(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})
@app.get("/contact",response_class=HTMLResponse)
async def getacontact(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})
@app.get("/about",response_class=HTMLResponse)
async def getabout(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})



app.include_router(productRoutes.router)
app.include_router(userRoutes.router)
app.include_router(cartRoutes.router)
app.include_router(categoryRoutes.router)
##endpoints(graphqlapi)
app.include_router(graphql_app,prefix="/graphql")

#custom part and setup
if __name__ == '__main__':
    uvicorn.run(app="main:app",port=5000,reload=True,workers=1)

    