from fastapi import FastAPI
from src.routers import ChatRouters

# Creating app
app = FastAPI()

# Including routers
app.include_router(ChatRouters.router, prefix= "/chat")