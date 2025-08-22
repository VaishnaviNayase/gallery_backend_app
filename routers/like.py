from fastapi import APIRouter, HTTPException
from db_helpers.db_connection import get_db
from schemas.like_request import LikeRequest

router = APIRouter()

@router.post("/")
def like_image(req: LikeRequest):
    userId = req.userId
    breedImgId = req.breedImgId
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO likes (userId, breedImgId) VALUES (%s, %s) ON CONFLICT DO NOTHING;",
            (userId, breedImgId)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()
    return {"message": "Image liked successfully"}


@router.delete("/")
def unlike_image(req: LikeRequest):
    userId = req.userId
    breedImgId = req.breedImgId
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute(
            "DELETE FROM likes WHERE userId=%s AND breedImgId=%s;",
            (userId, breedImgId)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()
    return {"message": "Image unliked successfully"}