from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from src.routers import AuthRouters, ChatRouters
from decouple import config

# Creating app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins= config("ORIGINS"),
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"]
)

# Including routers
app.include_router(ChatRouters.router, prefix= "/chat", tags= ["Chat"])
app.include_router(AuthRouters.router, prefix= "/auth", tags= ["Auth"])