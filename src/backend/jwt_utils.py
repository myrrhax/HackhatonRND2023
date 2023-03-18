import jwt
import bcrypt
from settings import config
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


def sign_JWT(user_id: int, name: str):
    payload = {
        'user_id': user_id,
        'name': name
    }

    token = jwt.encode(payload, config.jwt_secret.get_secret_value(), algorithm=config.algorithm.get_secret_value())
    return token

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, 
                                   config.jwt_secret.get_secret_value(),
                                   algorithms=[config.algorithm.get_secret_value()])
        return decoded_token
    except:
        return {}
    
class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid