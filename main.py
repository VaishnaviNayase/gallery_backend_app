from fastapi import FastAPI
from routers import users, likes, recent_viewed
from fastapi.middleware.cors import CORSMiddleware

import os
app = FastAPI(title="Dog Gallery API")
origins = [
        "*"
]
app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, OPTIONS, etc.)
        allow_headers=["*"],  # Allows all headers in requests
)
@app.get("/")
def root():
    return {"message": "Dog Gallery API running "}

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(likes.router, prefix="/like", tags=["Like"])
app.include_router(likes.router, prefix="/likes", tags=["Likes"])
app.include_router(recent_viewed.router, prefix="/viewed", tags=["Recently Viewed"])

