# System Architecture: Open Process Engine (OpenPlant)

## 1. High-Level Architecture
OpenPlant is designed as a stateless calculation kernel accessible via a REST API (FastAPI) or CLI. All process state is passed via the JSON flowsheet or persisted in the PostgreSQL database.

## 2. Tech Stack
- **Language**: Python 3.11+ (Strict typing, avoiding `Any`)
- **API Framework**: FastAPI (>=0.110)
- **Database**: PostgreSQL
- **ORM & Migrations**: SQLAlchemy (>=2.0) and Alembic (>=1.13)
- **Validation**: Pydantic (>=2.5)
- **Linting & Formatting**: Ruff (>=0.5)
- **Testing**: Pytest (>=8.0)

## 3. Directory Structure
- `app/api/` - FastAPI endpoints and routing.
- `app/core/` - Global configurations, settings, and environment variables.
- `app/db/` - SQLAlchemy models, DB sessions, and connection pooling.
- `app/engine/` - Core solver logic, flowsheet parsing, and the calculation kernel.
- `app/engine/units/` - Specific logic for unit operations (e.g., Mixer, Heater, Pump).
- `app/exporters/` - Export logic to convert calculation results into various formats.
- `app/schemas/` - Pydantic schemas defining the API contract, JSON flowsheet structure, and validation rules.
- `flowsheets/` - Example and active JSON flowsheet definitions.
- `migrations/` - Alembic database migration scripts.
- `scripts/` - CLI utilities (seeding data, running local flowsheet tests).
- `tests/` - Pytest suites for unit operations, engine, and API.

## 4. State Management & Data Flow
1. **Stateless Engine**: The calculation engine itself does not hold state between requests. 
2. **Input**: A flowsheet is defined via a structured JSON containing `streams`, `units`, and their interconnections.
3. **Validation**: The JSON is parsed and validated by Pydantic and custom validators (`FlowsheetValidator`). Errors are captured as structured logs.
4. **Execution**: The solver iterates over the unit operations, resolving mass and energy balances.
5. **Output**: The result is a structured JSON containing solved streams, unit duties, and validation logs. This is returned to the user and persisted in PostgreSQL for record-keeping.

## 5. Security & Configuration
- **No Hardcoded Secrets**: All keys and credentials must use environment variables loaded via Pydantic Settings (`.env`).
