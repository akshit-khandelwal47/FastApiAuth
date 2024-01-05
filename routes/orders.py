from fastapi import APIRouter,Depends,status
from fastapi.encoders import jsonable_encoder
from models import User,Order
from schema import OrderModel
from fastapi.exceptions import HTTPException
from database import Session,engine
from oauth2 import get_current_user

order_route = APIRouter(
    tags=["orders"],
    prefix="/orders"
)

session = Session(bind=engine)

@order_route.post('/order', status_code=status.HTTP_201_CREATED)
async def place_order(order:OrderModel,current_user: str = Depends(get_current_user)):

    """
        ## Placing an Order
        This requires following details 
        - product --> string
        - quantity --> integer

    """

    db_user = session.query(User).filter(User.username == current_user).first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )

    new_order = Order(
        quantity = order.quantity,
        product = order.product,
        user_id= db_user.id
    )

    session.add(new_order)
    session.commit()
    response ={
        "id":new_order.id,
        "product":new_order.product,
        "quantity":new_order.quantity
    }
    return jsonable_encoder(response)

@order_route.get('/allorders')
async def all_orders(current_user: str = Depends(get_current_user)):

    db_user = session.query(User).filter(User.username == current_user).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    
    db_orders = session.query(Order).all()

    return jsonable_encoder(db_orders)


@order_route.get('/orders/{id}')
async def get_order(id:int,current_user: str = Depends(get_current_user)):

    db_user = session.query(User).filter(User.username == current_user).first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    
    db_order_id = session.query(Order).filter(Order.id==id).first()

    return jsonable_encoder(db_order_id)

@order_route.get('/user/orders')
async def get_user_orders(current_user: str = Depends(get_current_user)):

    db_user = session.query(User).filter(User.username == current_user).first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )

    return jsonable_encoder(db_user.orders)


@order_route.put('/order/update/{order_id}')
async def update_order(order_id:int,order:OrderModel, current_user: str = Depends(get_current_user)):
    db_user = session.query(User).filter(User.username == current_user).first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    
    order_update = session.query(Order).filter(Order.id== order_id).first()

    if not order_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Order with id {order_id} not found"
        )

    order_update.quantity= order.quantity
    order_update.product = order.product

    session.commit()
    response ={
        "id":order_update.id,
        "product":order_update.product,
        "quantity":order_update.quantity
    }
    return jsonable_encoder(response)


@order_route.delete('/order/delete/{order_id}',status_code=status.HTTP_200_OK)
async def delete_order(order_id:int,current_user: str = Depends(get_current_user)):

    db_user = session.query(User).filter(User.username == current_user).first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    
    order_delete = session.query(Order).filter(Order.id==order_id).first()

    session.delete(order_delete)
    session.commit()

    response ={
        "id":order_delete.id,
        "product":order_delete.product,
        "quantity":order_delete.quantity
    }
    return jsonable_encoder(response)

