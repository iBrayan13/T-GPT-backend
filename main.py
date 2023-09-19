from fastapi import FastAPI
from src.routes import ChatRouters

# Creating app
app = FastAPI()

# Including routers
app.include_router(ChatRouters.router, prefix= "/chat")