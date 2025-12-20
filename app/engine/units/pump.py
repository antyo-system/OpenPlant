from typing import Dict, Any
from app.engine.registry import register
@register("pump")
def solve_pump(*, unit: Dict[str, Any], streams: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    inlet = unit["inlets"][0]
    outlet = unit["outlets"][0]
    params = unit.get("params", {})
    dP = float(params["dP_Pa"])
    eff = float(params.get("efficiency", 0.7))
    rho = float(params.get("rho_kg_m3", 1000.0))  # placeholder
    s_in = streams[inlet]
    m = float(s_in["mass_flow_kg_s"])
    # volumetric flow (m3/s) = m/rho
    Q = m / rho
    # hydraulic power (W) = dP * Q, shaft power = /eff
    P_hyd_W = dP * Q
    P_shaft_W = P_hyd_W / max(eff, 1e-6)
    streams[outlet] = {
        **s_in,
        "id": outlet,
        "P_Pa": float(s_in["P_Pa"]) + dP,
    }
    return {
        "unit_id": unit["id"],
        "type": "pump",
        "status": "solved",
        "kpis": {
            "dP_Pa": dP,
            "Q_m3_s": Q,
            "efficiency": eff,
            "hydraulic_power_W": P_hyd_W,
            "shaft_power_W": P_shaft_W,
            "P_out_Pa": streams[outlet]["P_Pa"],
        }
    }
