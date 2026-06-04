# System Architecture: Open Process Engine (OpenPlant)

## 1. High-Level Architecture
OpenPlant is designed as a stateless calculation kernel accessible via a REST API (FastAPI) or CLI. All process state is passed via the JSON flowsheet or persisted in an ultra-lightweight local SQLite database.

## 2. Tech Stack
- **Language**: Python 3.11+ (Strict typing)
- **API Framework**: FastAPI (>=0.110)
- **Database**: SQLite (Zero config, local)
- **ORM & Migrations**: SQLAlchemy (>=2.0) and Alembic (>=1.13)
- **Validation**: Pydantic (>=2.5)

## 3. Directory Structure
- `app/api/` - FastAPI endpoints and routing.
- `app/core/` - Global configurations.
- `app/db/` - SQLAlchemy models tailored for SQLite.
- `app/engine/` - Core solver logic and flowsheet parsing.
- `app/engine/units/` - Specific logic for Process Units and future Smart Units.
- `app/exporters/` - Export logic to convert calculation results.
- `app/schemas/` - Pydantic schemas defining the API contract.
- `flowsheets/` - Example JSON flowsheets.

## 4. State Management & Data Flow (Stream is King)
1. **Stateless Engine**: The calculation engine itself does not hold state between requests. 
2. **Input**: A flowsheet is defined via a structured JSON. 
3. **Stream Protocol**: All nodes (Process Units and AI Smart Units) MUST communicate using thermodynamic streams. The Stream is the universal language of the engine.
4. **Execution**: The solver iterates over the unit operations, resolving balances.
5. **Output**: The result is a structured JSON containing solved streams, unit duties, and validation logs, persisted to SQLite.
