![Status](https://img.shields.io/badge/status-in%20progress-yellow)

# Open Process Engine (OpenPlant)

A modular, ultra-lightweight process calculation engine. Acting as an "n8n for Chemical Engineers", it combines classic chemical Process Units (Mixers, Heaters) with AI-powered Smart Units. It reads JSON flowsheets, solves rigorous mass/energy balances, and returns structured JSON results. 

Designed to be **1000x lighter** than traditional simulators, OpenPlant uses a zero-config SQLite architecture, making it perfect for both enterprise engineers and UMKM (Small-Medium Enterprises) entrepreneurs looking to automate their physical factories.

## Documentation
For deep dives into the project, refer to our core documentation:
- [Product Requirements (PRD)](docs/PRD.md)
- [System Architecture](docs/ARCHITECTURE.md)
- [API Reference](docs/API_REFERENCE.md)

## Development Philosophy
We build using a strict 5-step algorithm to strip complexity:
1. **Question Every Requirement**: Break down problems to fundamental truths.
2. **Delete Parts**: Eliminate unnecessary steps (e.g., we deleted PostgreSQL to make it run anywhere).
3. **Simplify**: Streamline what remains.
4. **Accelerate**: Speed up the cycle time.
5. **Automate Last**: Only automate after the first four steps.

## Goals (MVP Scope v0.1)
- **Single Source of Truth** for process calculations.
- **Stream is King**: All nodes (Process or AI) communicate via strict thermodynamic streams.
- **Unit Operations**: Mixer (mass balance), Heater/Cooler (energy balance), Pump (ΔP & power).
- **Validation**: VSCode-style errors, warnings, and fix suggestions.
- **Output**: Consistently structured JSON + logs.
- **Database**: Zero-config local SQLite (components, properties, templates).

## Tech Stack
- Python 3.11+
- FastAPI (API)
- SQLAlchemy + Alembic (SQLite DB)
- Pydantic (Schemas)

## Quickstart

### 1. Install and Migrate (Zero Docker required!)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -U pip
pip install -e ".[dev]"
alembic upgrade head
python scripts/seed_reference_data.py
```

### 2. Solve Demo Flowsheet (CLI)
```bash
python scripts/run_flowsheet.py flowsheets/demo_mixer_heater_pump.json
```
*Outputs are saved to `results/demo_mixer_heater_pump.result.json` and persisted in the DB.*

### 3. Run API Server
```bash
uvicorn app.main:app --reload
```
*Test endpoints: `GET /health` or `POST /solve` (body: flowsheet JSON).*

## Roadmap
- Hybrid Architecture: Introduce Smart Units (AI Agents) inside flowsheets.
- Flash separator (VLE + basic K-values).
- Advanced thermodynamics (Cp(T), rho(T,P), Antoine).
- UI connector (Modern Glassmorphism Web App).

## License
MIT
