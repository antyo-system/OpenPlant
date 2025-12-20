from typing import Callable, Dict
UnitSolver = Callable[..., dict]
_REGISTRY: Dict[str, UnitSolver] = {}
def register(unit_type: str):
    def deco(fn: UnitSolver):
        _REGISTRY[unit_type] = fn
        return fn
    return deco
def get_solver(unit_type: str) -> UnitSolver:
    if unit_type not in _REGISTRY:
        raise KeyError(f"No solver registered for unit_type='{unit_type}'")
    return _REGISTRY[unit_type]
