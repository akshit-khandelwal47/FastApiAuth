from fastapi import FastAPI
from routes.auth import auth
from routes.orders import order_route

app = FastAPI()



app.include_router(auth)
app.include_router(order_route)


