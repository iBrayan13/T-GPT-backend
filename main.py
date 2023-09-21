from fastapi import FastAPI
from src.routers import AuthRouters, ChatRouters

# Creating app
app = FastAPI()

# Including routers
app.include_router(ChatRouters.router, prefix= "/chat", tags= ["Chat"])
app.include_router(AuthRouters.router, prefix= "/auth", tags= ["Auth"])