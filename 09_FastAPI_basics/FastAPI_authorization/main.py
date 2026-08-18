from fastapi import FastAPI, HTTPException
from auth import hash_password, verify_password, create_access_token

# Initialize FastAPI application instance
app = FastAPI()

# Simulated database containing user records with hashed passwords
fake_users_db = {
    "umar": {"username": "umar", "hashed_pass": hash_password("mypass123")}
}


@app.post("/login")
def login(username: str, password: str):
    # Retrieve user record from the simulated database
    user = fake_users_db.get(username)

    # Validate user existence and verify input password against stored hash
    if not user or not verify_password(password, user["hashed_pass"]):
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    # Generate access token with subject claim set to the authenticated username
    access_token = create_access_token(data={"sub": username})

    # Return bearer token response conforming to OAuth2 standards
    return {"access_token": access_token, "token_type": "bearer"}