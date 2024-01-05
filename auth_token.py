from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from schema import Settings

ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = "HS256"
settings = Settings()

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=ALGORITHM)
    return encoded_jwt


