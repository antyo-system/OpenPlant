![Status](https://img.shields.io/badge/status-in%20progress-yellow)

# Open Process Engine (OpenPlant)

A modular, open-source process calculation engine. It functions as a lightweight Aspen kernel: reading JSON flowsheets, validating structures, solving mass/energy balances, and returning structured JSON results ready for UI, AI, or exporter integrations.

## Documentation
For deep dives into the project, refer to our core documentation:
- [Product Requirements (PRD)](docs/PRD.md)
- [System Architecture](docs/ARCHITECTURE.md)
- [API Reference](docs/API_REFERENCE.md)

## Development Philosophy
We build using a strict 5-step algorithm to strip complexity:
1. **Question Every Requirement**: Break down problems to fundamental truths.
2. **Delete Parts**: Eliminate unnecessary steps. If you aren't adding back 10% later, you haven't deleted enough.
3. **Simplify**: Streamline what remains.
4. **Accelerate**: Speed up the cycle time.
5. **Automate Last**: Only automate after the first four steps.

## Goals (MVP Scope v0.1)
- **Single Source of Truth** for process calculations.
- **Unit Operations**: Mixer (mass balance), Heater/Cooler (energy balance), Pump (ΔP & power).
- **Validation**: VSCode-style errors, warnings, and fix suggestions.
- **Output**: Consistently structured JSON + logs.
- **Database**: PostgreSQL reference data (components, properties, templates).

## Tech Stack
- Python 3.11+
- FastAPI (API)
- SQLAlchemy + Alembic (DB)
- PostgreSQL (via Docker)
- Pydantic (Schemas)

## Quickstart

### 1. Run PostgreSQL Database
```bash
cp .env.example .env
docker compose up -d db
```

### 2. Install and Migrate
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -U pip
pip install -e ".[dev]"
alembic upgrade head
python scripts/seed_reference_data.py
```

### 3. Solve Demo Flowsheet (CLI)
```bash
python scripts/run_flowsheet.py flowsheets/demo_mixer_heater_pump.json
```
*Outputs are saved to `results/demo_mixer_heater_pump.result.json` and persisted in the DB.*

### 4. Run API Server
```bash
uvicorn app.main:app --reload
```
*Test endpoints: `GET /health` or `POST /solve` (body: flowsheet JSON).*

## Roadmap
- Flash separator (VLE + basic K-values)
- Shortcut distillation (Fenske/Underwood/Gilliland)
- Advanced thermodynamics (Cp(T), rho(T,P), Antoine)
- Standard exporters (Excel/PDF/Word)
- UI connector & AI suggestions

## License
MIT
