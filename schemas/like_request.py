from pydantic import BaseModel

class LikeRequest(BaseModel):
    userId: int
    breedImgId: int