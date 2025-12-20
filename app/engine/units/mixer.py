from typing import Dict, Any
from app.engine.registry import register
@register("mixer")
def solve_mixer(*, unit: Dict[str, Any], streams: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    inlets = unit["inlets"]
    outlet = unit["outlets"][0]
    m_total = 0.0
    comp_acc: Dict[str, float] = {}
    T_acc = 0.0
    P_min = None
    for sid in inlets:
        s = streams[sid]
        m = s["mass_flow_kg_s"]
        m_total += m
        T_acc += m * s["T_K"]
        P_min = s["P_Pa"] if P_min is None else min(P_min, s["P_Pa"])
        for k, v in s["comp"].items():
            comp_acc[k] = comp_acc.get(k, 0.0) + m * v
    comp_out = {k: v / m_total for k, v in comp_acc.items()}
    T_out = T_acc / m_total
    streams[outlet]["mass_flow_kg_s"] = m_total
    streams[outlet]["comp"] = comp_out
    streams[outlet]["T_K"] = T_out
    streams[outlet]["P_Pa"] = float(P_min)
    return {
        "unit_id": unit["id"],
        "type": "mixer",
        "status": "solved",
        "kpis": {
            "mass_flow_out_kg_s": m_total,
            "T_out_K": T_out,
            "P_out_Pa": float(P_min),
        }
    }
