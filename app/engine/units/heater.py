from typing import Dict, Any
from app.engine.registry import register
# MVP: Cp constant (kJ/kg.K) and deltaT param
DEFAULT_CP_KJ_KG_K = 4.18  # placeholder like water-ish
@register("heater")
@register("cooler")
def solve_heater(*, unit: Dict[str, Any], streams: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    inlet = unit["inlets"][0]
    outlet = unit["outlets"][0]
    params = unit.get("params", {})
    dT = float(params.get("dT_K", 0.0))
    cp = float(params.get("cp_kj_kg_k", DEFAULT_CP_KJ_KG_K))
    s_in = streams[inlet]
    m = float(s_in["mass_flow_kg_s"])
    T_out = float(s_in["T_K"]) + dT
    # duty (kW) = m(kg/s) * cp(kJ/kg.K) * dT(K)
    duty_kW = m * cp * dT
    streams[outlet] = {
        **s_in,
        "id": outlet,
        "T_K": T_out,
    }
    return {
        "unit_id": unit["id"],
        "type": unit["type"],
        "status": "solved",
        "kpis": {
            "dT_K": dT,
            "cp_kj_kg_k": cp,
            "duty_kW": duty_kW,
            "T_out_K": T_out,
        }
    }
