from fastapi import APIRouter, HTTPException
from app.schemas.flowsheet import Flowsheet
from app.engine.solver import solve_flowsheet
from app.engine.validator import validate_flowsheet
from app.db.session import SessionLocal
from app.db import crud

router = APIRouter()


@router.post("/solve")
def solve(fs: Flowsheet):
    report = validate_flowsheet(fs)

    with SessionLocal() as db:
        crud.save_flowsheet(db, fs)
        crud.save_validation_logs(db, fs.id, report)

        if report.has_errors:
            db.commit()
            raise HTTPException(status_code=422, detail=report.model_dump())

        result = solve_flowsheet(fs, report)
        crud.save_result(db, fs.id, result)
        db.commit()
        return result
