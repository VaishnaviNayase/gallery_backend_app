from pydantic import BaseModel

class RecentViewedRequest(BaseModel):
    userId: int
    breedId: int