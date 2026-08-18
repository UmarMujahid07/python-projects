from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext

# Configuration constants
SECRET_KEY = "my-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Initialize password hashing context with bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(data: dict) -> str:
    # Generates a signed JSON Web Token (JWT) with payload data
    # and an expiration timestamp.coded JWT string.
    to_encode = data.copy()

    # Use timezone-aware UTC datetime to prevent deprecation issues with utcnow()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    # Encode payload into a signed JWT token string
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

def hash_password(password: str) -> str:
    # Hashes a plain-text password using the configured bcrypt scheme.
    return pwd_context.hash(password)


def verify_password(plain_pass: str, hashed_pass: str) -> bool:
    # Verifies a plain-text password against a stored bcrypt hash.
    return pwd_context.verify(plain_pass, hashed_pass)