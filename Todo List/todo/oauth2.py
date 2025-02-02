from fastapi import Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from . import token, database, models
from jose import jwt, JWTError
from sqlalchemy.orm import Session
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(data: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    
    try:
        # Verify the token and get the email
        token_data = token.verify_token(data, credentials_exception)
        
        # Get user from database using the email
        user = db.query(models.User).filter(models.User.email == token_data.email).first()
        if user is None:
            raise credentials_exception
        return user
        
    except JWTError:
        raise credentials_exception
    