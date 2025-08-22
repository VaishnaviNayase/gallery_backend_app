from fastapi import FastAPI
from routers import users, likes, recent_viewed

app = FastAPI(title="Dog Gallery API")

@app.get("/")
def root():
    return {"message": "Dog Gallery API running "}

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(likes.router, prefix="/like", tags=["Like"])
app.include_router(likes.router, prefix="/likes", tags=["Likes"])
app.include_router(recent_viewed.router, prefix="/viewed", tags=["Recently Viewed"])