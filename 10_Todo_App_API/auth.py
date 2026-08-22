from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

# JWT Security Configurations
SECRET_KEY = "my-secret-key"
ALGORITHM = "HS256"

# Password hashing context using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme extracting bearer tokens from the request Authorization header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# Hash plain-text password using bcrypt
def hash_password(password):
    return pwd_context.hash(password)


# Verify plain-text password against stored hash
def verify_password(plain_pass, hash_pass):
    return pwd_context.verify(plain_pass, hash_pass)


# Generate JWT token with expiration payload
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


# Dependency to validate access token and extract target username
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid Token")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid Token")