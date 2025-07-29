from fastapi import APIRouter, Path, Request, Depends, HTTPException
from providers.salesforce import SalesforceProvider
from providers.ups import UPSProvider
from auth.schemes import password_auth, api_key_auth, oauth2_auth

router = APIRouter()

provider_map = {
    "salesforce": SalesforceProvider(),
    "ups": UPSProvider()
}

auth_schemes = {
    "salesforce": password_auth,
    "ups": api_key_auth
}

@router.post("/integrate/{provider}")
async def integrate(
    provider: str = Path(...),
    request: Request = None,
    auth: None = Depends(oauth2_auth)  # Replace dynamically below
):
    if provider not in provider_map:
        raise HTTPException(status_code=400, detail="Unsupported provider")

    try:
        body = await request.json()
        action = body.get("action")
        parameters = body.get("parameters")

        if not action or not isinstance(parameters, dict):
            raise HTTPException(status_code=422, detail="Invalid input format")

        # Provider-specific auth
        auth_dependency = auth_schemes.get(provider)
        if auth_dependency:
            await auth_dependency()

        provider_instance = provider_map[provider]
        result = await provider_instance.handle(action, parameters)
        return {"status": "success", "data": result}

    except Exception as e:
        return {"status": "error", "message": str(e)}