from fastapi import FastAPI
from routers import users, likes, recent_viewed
import os
app = FastAPI(title="Dog Gallery API")

@app.get("/")
def root():
    return {"message": "Dog Gallery API running "}

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(likes.router, prefix="/like", tags=["Like"])
app.include_router(likes.router, prefix="/likes", tags=["Likes"])
app.include_router(recent_viewed.router, prefix="/viewed", tags=["Recently Viewed"])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
