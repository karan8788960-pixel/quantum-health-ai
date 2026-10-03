from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import hash_password, verify_password, create_access_token, get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])

USERS = {
    "doctor": {"password": hash_password("doctor123"), "role": "doctor"},
    "researcher": {"password": hash_password("researcher123"), "role": "researcher"},
    "admin": {"password": hash_password("admin123"), "role": "admin"},
    "patient": {"password": hash_password("patient123"), "role": "patient"},
}


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = USERS.get(form_data.username)
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token(subject=form_data.username)
    return {"access_token": token, "token_type": "bearer", "role": user["role"]}


@router.get("/me")
async def me(current_user: dict = Depends(get_current_user)):
    return {"username": current_user.get("sub"), "role": USERS.get(current_user.get("sub"), {}).get("role", "patient")}
