from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.session import get_session

router = APIRouter()

@router.get("/health")
def health(db: Session = Depends(get_session)):
    try:
        db.execute(text("SELECT 1"))
        db_status = "successful"
    except Exception:
        db_status = "failed"

    return {
        "status": "ok",
        "db_connection": db_status
    }
