from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.solve import router as solve_router
app = FastAPI(title="Open Process Engine", version="0.1.0")
app.include_router(health_router)
app.include_router(solve_router)
