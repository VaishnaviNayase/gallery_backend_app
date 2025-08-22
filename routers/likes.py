from fastapi import APIRouter, HTTPException
from db_helpers.db_connection import get_db
from psycopg2.extras import RealDictCursor

router = APIRouter()

@router.get("/")
def get_liked_images(userId: int):
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("""
            SELECT l.likeId, b.imageURL
            FROM likes l
            JOIN breedImage b ON l.breedImgId = b.breedImgId
            WHERE l.userId = %s;
        """, (userId,))
        likes = cur.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()
    return {"liked_images": likes}