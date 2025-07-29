from fastapi import FastAPI
from routers import integrate

app = FastAPI(title="Proxy Integration Service")
app.include_router(integrate.router)