import json
import sys
from pathlib import Path

from app.schemas.flowsheet import Flowsheet
from app.engine.validator import validate_flowsheet
from app.engine.solver import solve_flowsheet
from app.db.session import SessionLocal
from app.db import crud


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/run_flowsheet.py <flowsheet.json>")
        raise SystemExit(1)

    fp = Path(sys.argv[1])
    fs = Flowsheet(**json.loads(fp.read_text(encoding="utf-8")))

    report = validate_flowsheet(fs)

    with SessionLocal() as db:
        crud.save_flowsheet(db, fs)
        crud.save_validation_logs(db, fs.id, report)

        if report.has_errors:
            db.commit()
            print(json.dumps(report.model_dump(), indent=2))
            raise SystemExit(2)

        result = solve_flowsheet(fs, report)
        crud.save_result(db, fs.id, result)
        db.commit()

    out_dir = Path("results")
    out_dir.mkdir(exist_ok=True)
    out_fp = out_dir / f"{fs.id}.result.json"
    out_fp.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(f"Solved. Output: {out_fp}")


if __name__ == "__main__":
    main()
