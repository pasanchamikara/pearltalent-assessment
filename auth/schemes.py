from fastapi import Depends, HTTPException, Header
from fastapi.security import HTTPBasic, HTTPBasicCredentials, APIKeyHeader, OAuth2PasswordBearer

basic_auth = HTTPBasic()
api_key_scheme = APIKeyHeader(name="X-API-Key", auto_error=False)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def password_auth(credentials: HTTPBasicCredentials = Depends(basic_auth)):
    if credentials.username != "user" or credentials.password != "pass":
        raise HTTPException(status_code=401, detail="Invalid basic auth")

def api_key_auth(api_key: str = Depends(api_key_scheme)):
    if api_key != "test-key":
        raise HTTPException(status_code=401, detail="Invalid API Key")

def oauth2_auth(token: str = Depends(oauth2_scheme)):
    if token != "valid-token":
        raise HTTPException(status_code=401, detail="Invalid OAuth2 token")