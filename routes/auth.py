from fastapi import APIRouter,status,Depends
from fastapi.encoders import jsonable_encoder
from schema import SignUpModel,Token
from database import Session,engine
from models import User
from fastapi.exceptions import HTTPException
from hashing import HashPassword
from fastapi.security import OAuth2PasswordRequestForm
from auth_token import create_token


auth = APIRouter(
    tags=["authentication"],
    prefix="/auth"
)

session = Session(bind=engine)

@auth.post('/signup', 
           status_code=status.HTTP_201_CREATED)
async def signup(user:SignUpModel):

    db_email = session.query(User).filter(User.email==user.email).first()
    
    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="User with email already exists")
    
    db_username = session.query(User).filter(User.username==user.username).first()
    
    if db_username is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="Username already exists")
    
    new_user = User(
        username = user.username,
        email =  user.email,
        password = HashPassword.bcrypt(user.password)
    )

    session.add(new_user)
    session.commit()
    response = {
        "username":new_user.username,
        "email": new_user.email,
    }
    return jsonable_encoder(response)


@auth.post('/login',response_model=Token ,status_code=status.HTTP_200_OK)
def login(request:OAuth2PasswordRequestForm= Depends()):
    db_user=session.query(User).filter(User.username==request.username).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not HashPassword.verify(db_user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")
    
    access_token = create_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

