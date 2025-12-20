from datetime import datetime
from typing import Dict, Any

from sqlalchemy import delete
from sqlalchemy.orm import Session

from app.db import models
from app.schemas.flowsheet import Flowsheet
from app.engine.validator import ValidationReport


def save_flowsheet(session: Session, fs: Flowsheet) -> None:
    session.merge(
        models.Flowsheet(
            id=fs.id,
            name=fs.name,
            data=fs.model_dump(),
            created_at=datetime.utcnow(),
        )
    )

    session.execute(delete(models.Stream).where(models.Stream.flowsheet_id == fs.id))
    session.execute(delete(models.Unit).where(models.Unit.flowsheet_id == fs.id))

    for s in fs.streams:
        session.add(
            models.Stream(
                id=s.id,
                flowsheet_id=fs.id,
                data=s.model_dump(),
            )
        )

    for u in fs.units:
        session.add(
            models.Unit(
                id=u.id,
                flowsheet_id=fs.id,
                type=u.type,
                params=u.params,
            )
        )


def save_validation_logs(session: Session, fs_id: str, report: ValidationReport) -> None:
    for item in report.items:
        session.add(
            models.ValidationLog(
                flowsheet_id=fs_id,
                level=item.level,
                code=item.code,
                message=item.message,
                suggestion=item.suggestion,
            )
        )


def save_result(session: Session, fs_id: str, result: Dict[str, Any]) -> None:
    session.add(
        models.Result(
            flowsheet_id=fs_id,
            data=result,
        )
    )
