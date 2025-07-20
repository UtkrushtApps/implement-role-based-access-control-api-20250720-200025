from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.schemas.user import UserCreate, UserProfile, UserProfileUpdate
from app.models.user import FakeDB, User

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    # For simplicity, always return the same fake user from the DB
    user = FakeDB.get_user('user1')
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication")
    return user

@app.post("/user/profile", response_model=UserProfile)
def create_profile(profile: UserCreate):
    user = User(**profile.dict())
    FakeDB.add_user('user1', user)
    return user

@app.get("/user/profile", response_model=UserProfile)
def get_profile(current_user: User = Depends(get_current_user)):
    return current_user

@app.put("/user/profile", response_model=UserProfile)
def update_profile(update: UserProfileUpdate, current_user: User = Depends(get_current_user)):
    update_data = update.dict(exclude_unset=True)
    updated_user = current_user.copy(update=update_data)
    FakeDB.update_user('user1', updated_user)
    return updated_user
