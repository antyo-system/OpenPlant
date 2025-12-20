from dataclasses import dataclass, field
from typing import List, Dict
from app.schemas.flowsheet import Flowsheet
@dataclass
class ValidationItem:
    code: str
    level: str  # "error" | "warning"
    message: str
    suggestion: str = ""
@dataclass
class ValidationReport:
    items: List[ValidationItem] = field(default_factory=list)
    @property
    def has_errors(self) -> bool:
        return any(i.level == "error" for i in self.items)
    def model_dump(self) -> Dict:
        return {
            "has_errors": self.has_errors,
            "items": [i.__dict__ for i in self.items],
        }
def validate_flowsheet(fs: Flowsheet) -> ValidationReport:
    r = ValidationReport()
    stream_ids = {s.id for s in fs.streams}
    if not fs.units:
        r.items.append(ValidationItem(
            code="FS_EMPTY_UNITS",
            level="error",
            message="Flowsheet has no units.",
            suggestion="Add at least one unit operation."
        ))
    # Stream comp sums
    for s in fs.streams:
        comp_sum = sum(s.comp.values())
        if abs(comp_sum - 1.0) > 1e-6:
            r.items.append(ValidationItem(
                code="STREAM_COMP_SUM",
                level="error",
                message=f"Stream '{s.id}' composition sum is {comp_sum:.6f}, expected 1.0.",
                suggestion="Normalize comp fractions so total equals 1.0."
            ))
        if s.T_K <= 0:
            r.items.append(ValidationItem(
                code="STREAM_TEMP",
                level="error",
                message=f"Stream '{s.id}' has invalid T_K={s.T_K}.",
                suggestion="Use absolute temperature in Kelvin (>0)."
            ))
        if s.P_Pa <= 0:
            r.items.append(ValidationItem(
                code="STREAM_PRESSURE",
                level="error",
                message=f"Stream '{s.id}' has invalid P_Pa={s.P_Pa}.",
                suggestion="Use absolute pressure in Pa (>0)."
            ))
    # Unit inlet/outlet existence
    for u in fs.units:
        for sid in u.inlets + u.outlets:
            if sid not in stream_ids:
                r.items.append(ValidationItem(
                    code="UNIT_STREAM_REF",
                    level="error",
                    message=f"Unit '{u.id}' references missing stream '{sid}'.",
                    suggestion="Add the stream or fix the id in unit inlets/outlets."
                ))
        if u.type == "mixer":
            if len(u.inlets) < 2:
                r.items.append(ValidationItem(
                    code="MIXER_INLETS",
                    level="error",
                    message=f"Mixer '{u.id}' needs at least 2 inlets.",
                    suggestion="Add more inlet streams."
                ))
            if len(u.outlets) != 1:
                r.items.append(ValidationItem(
                    code="MIXER_OUTLETS",
                    level="error",
                    message=f"Mixer '{u.id}' must have exactly 1 outlet.",
                    suggestion="Set mixer outlets to exactly one stream."
                ))
        if u.type in ("heater", "cooler"):
            if len(u.inlets) != 1 or len(u.outlets) != 1:
                r.items.append(ValidationItem(
                    code="HEATER_PORTS",
                    level="error",
                    message=f"{u.type.title()} '{u.id}' must have 1 inlet and 1 outlet.",
                    suggestion="Use exactly one inlet and one outlet stream."
                ))
            if "dT_K" not in u.params:
                r.items.append(ValidationItem(
                    code="HEATER_PARAM_DT",
                    level="warning",
                    message=f"{u.type.title()} '{u.id}' missing params.dT_K (temperature change).",
                    suggestion="Add params.dT_K, e.g. +20 for heater or -20 for cooler."
                ))
        if u.type == "pump":
            if len(u.inlets) != 1 or len(u.outlets) != 1:
                r.items.append(ValidationItem(
                    code="PUMP_PORTS",
                    level="error",
                    message=f"Pump '{u.id}' must have 1 inlet and 1 outlet.",
                    suggestion="Use exactly one inlet and one outlet stream."
                ))
            if "dP_Pa" not in u.params:
                r.items.append(ValidationItem(
                    code="PUMP_PARAM_DP",
                    level="error",
                    message="Pump missing params.dP_Pa (pressure increase).",
                    suggestion="Add params.dP_Pa, e.g. 200000 for +2 bar."
                ))
    return r
