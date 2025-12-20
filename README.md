# Open Process Engine (Workflow 1)
Mini Aspen kernel yang modular dan terbuka: baca flowsheet JSON, validasi, solve neraca, hasil terstruktur (JSON), siap disambungkan ke UI/AI/exporter.
## Goals (MVP 1-3 minggu)
- Single Source of Truth untuk perhitungan proses.
- Flowsheet berbasis JSON (portable, versionable).
- Validator seperti VSCode errors untuk proses: error/warning + fix suggestion.
- Solver modular per unit operation.
- Output selalu structured JSON + logs.
- Database referensi di PostgreSQL.
## MVP Scope (v0.1)
Unit operations:
- Mixer (mass balance)
- Heater/Cooler (energy balance sederhana)
- Pump (?P + power estimate sederhana)
Reference data tables (seed minimal):
- components
- property_correlations (placeholder)
- steam_tables (placeholder)
- equipment_templates (placeholder)
Engine tables:
- flowsheets, streams, units, calculations, results, validation_logs
## Tech
- Python 3.11+
- FastAPI (API)
- SQLAlchemy + Alembic (DB)
- PostgreSQL (docker-compose)
- Pydantic (schemas)
## Quickstart
### 1) Run Postgres
`ash
cp .env.example .env
docker compose up -d db
`
### 2) Install and migrate
`ash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -U pip
pip install -e ".[dev]"
alembic upgrade head
python scripts/seed_reference_data.py
`
### 3) Solve demo flowsheet (CLI)
`ash
python scripts/run_flowsheet.py flowsheets/demo_mixer_heater_pump.json
`
Output akan masuk ke:
- results/demo_mixer_heater_pump.result.json
- DB: results + validation_logs
### 4) Run API
`ash
uvicorn app.main:app --reload
`
Try:
- GET /health
- POST /solve (body: flowsheet JSON)
## Flowsheet JSON contract
High-level:
- streams: daftar stream (composition, T, P, flow)
- units: daftar unit op (type, inlets, outlets, params)
- connections: optional (bisa implicit dari inlets/outlets)
See: flowsheets/demo_mixer_heater_pump.json
## Roadmap (next)
- Flash separator (VLE + K-values sederhana)
- Shortcut distillation (Fenske/Underwood/Gilliland)
- Better properties (Cp(T), rho(T,P), Antoine)
- Exporter beneran: Excel/PDF/Word
- UI connector + AI suggestions
## License
MIT.
