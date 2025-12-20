from typing import Dict, Any
from app.schemas.flowsheet import Flowsheet
from app.engine.validator import ValidationReport
from app.engine.registry import get_solver
# import unit modules to register them
from app.engine.units import mixer, heater, pump  # noqa: F401
def solve_flowsheet(fs: Flowsheet, report: ValidationReport) -> Dict[str, Any]:
    # Index streams by id (mutable dict results)
    streams: Dict[str, Dict[str, Any]] = {
        s.id: s.model_dump() for s in fs.streams
    }
    unit_results = []
    warnings = [i.__dict__ for i in report.items if i.level == "warning"]
    for u in fs.units:
        solver = get_solver(u.type)
        out = solver(unit=u.model_dump(), streams=streams)
        unit_results.append(out)
    return {
        "flowsheet_id": fs.id,
        "warnings": warnings,
        "streams": streams,
        "unit_results": unit_results,
    }
