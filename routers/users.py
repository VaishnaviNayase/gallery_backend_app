from fastapi import APIRouter, HTTPException
from db_helpers.db_connection import get_db

router = APIRouter()

@router.get("/login")
def login(email: str):
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM users WHERE email='{email}';" )
        user = cur.fetchone()

        if not user:
            cur.execute(
                f"INSERT INTO users (email) VALUES ('{email}') RETURNING userId, email;"
            )
            user = cur.fetchone()
            conn.commit()

        user_id, user_email = user[0], user[1]  # unpack tuple

    except Exception as e:
        print(f"Error during login: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
    finally:
        cur.close()
        conn.close()    
    
    return {"message": "Login successful", "userId": user_id, "email": user_email}
