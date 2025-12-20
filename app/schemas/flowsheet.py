from typing import Dict, List, Literal, Optional
from pydantic import BaseModel, Field
UnitType = Literal["mixer", "heater", "cooler", "pump"]
class StreamSpec(BaseModel):
    id: str
    name: Optional[str] = None
    # mass flow (kg/s) for MVP
    mass_flow_kg_s: float = Field(gt=0)
    # composition as mass fraction
    comp: Dict[str, float]
    T_K: float
    P_Pa: float
class UnitSpec(BaseModel):
    id: str
    type: UnitType
    inlets: List[str]
    outlets: List[str]
    params: Dict[str, float] = Field(default_factory=dict)
class Flowsheet(BaseModel):
    id: str
    name: Optional[str] = None
    streams: List[StreamSpec]
    units: List[UnitSpec]
