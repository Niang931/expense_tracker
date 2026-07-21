from app.core.database import connect_db
from app.core.jwt import decode_access_token
from app.internal.user import get_user_by_id
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

security = HTTPBearer(auto_error=False)


def extract_bearer_token(
    credential: HTTPAuthorizationCredentials = Depends(security),
):
    if credential is None:
        raise HTTPException(status_code=401, detail="Missing credentials")

    if credential.scheme.lower() != "bearer":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return credential.credentials


def get_current_user(
    cur = Depends(connect_db),
    token = Depends(extract_bearer_token),
):
    user_id = decode_access_token(token)

    user = get_user_by_id(cur, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user_id

