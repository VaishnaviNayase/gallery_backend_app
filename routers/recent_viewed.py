from fastapi import APIRouter, HTTPException
from db_helpers.db_connection import get_db
from schemas.recent_viewed_request import RecentViewedRequest
from psycopg2.extras import RealDictCursor

router = APIRouter()

@router.post("/")
def add_recent_view(view: RecentViewedRequest):
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("""
            INSERT INTO recentlyViewed (userId, breedId)
            VALUES (%s, %s)
            ON CONFLICT (userId, breedId)
            DO UPDATE SET viewed = CURRENT_TIMESTAMP
            RETURNING userId, breedId, viewed;
        """, (view.userId, view.breedId))
        result = cur.fetchone()
        conn.commit()
        return {"recent_view": result}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()


@router.get("/")
def get_recent_views(userId: int):
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("""
            SELECT breedId, viewed
            FROM recentlyViewed
            WHERE userId = %s
            ORDER BY viewed DESC
            LIMIT %s;
        """, (userId,5))
        views = cur.fetchall()
        return {"recent_views": views}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()