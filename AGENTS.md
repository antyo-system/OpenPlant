# AGENTS.md

## Role
Senior Python Backend and Chemical Engineering Software Developer.

## Project Overview
- **[APP_NAME]**: Open Process Engine (OpenPlant)
- **[ONE_LINE_DESCRIPTION]**: A lightweight, modular "n8n for Chemical Engineers" that reads JSON flowsheets, solves balances via Process Units, and executes Smart Units (AI Agents), returning structured JSON.
- **[FEATURE_LIST]**:
  - Portable, versionable JSON-based flowsheet input.
  - "Stream is King": All nodes communicate via strict chemical thermodynamic streams.
  - Hybrid Node Architecture: Mix classic Process Units (Mixer, Heater) with Smart Units (AI Analyzers, API Notifiers).
  - Robust flowsheet validation with VSCode-like errors and fix suggestions.
  - Zero-config ultra-lightweight SQLite database (1000x lighter than typical simulators, UMKM friendly).
- **[EXAMPLE_COMPONENT_NAMES]**:
  - `MixerSolver` (app/engine/units/mixer.py)
  - `HeaterSolver` (app/engine/units/heater.py)
  - `FlowsheetValidator` (app/engine/validator.py)
- **[EXAMPLE_STATE_FIELDS]**:
  - `flowsheet_json`: The current flowsheet definition (nodes, streams, connections).
  - `calculation_results`: The solved mass and energy balances for each stream/unit.

## Tech Stack
- **Language**: Python 3.11+
- **API Framework**: FastAPI (>=0.110)
- **Database**: SQLite (Zero config, local file) with SQLAlchemy (>=2.0) and Alembic (>=1.13)
- **Validation**: Pydantic (>=2.5)
- **Linting & Formatting**: Ruff (>=0.5)
- **Testing**: Pytest (>=8.0)

## Development Philosophy
The five-step algorithm relies on a specific, unalterable order to strip complexity and solve bottlenecks:
1. **Question Every Requirement**: Break down problems to their fundamental, indisputable truths and reason up. Dismiss inherited assumptions and industry standards; instead, ask yourself, "What are the essential, proven facts?"
2. **Delete Parts or Processes**: Eliminate unnecessary parts, steps, or components. If you do not have to occasionally reinstate at least 10% of what you cut, you haven't deleted enough.
3. **Simplify and Optimize**: Streamline what remains. The goal here is to ensure you are never optimizing a process or component that shouldn't exist in the first place.
4. **Accelerate Cycle Time**: Speed up the remaining, streamlined process.
5. **Automate Last**: Apply automation or technology only after the first four steps are complete. Automating a broken or unnecessary process is counterproductive.

Build feature by feature.
For every feature:
1. Read this file first.
2. Keep the implementation simple.
3. Avoid overengineering.
4. Prefer readable code over clever code.
5. Build the smallest useful version first.
6. Refactor only when repetition appears.

## Architecture
- `app/api/` - FastAPI endpoints and routing.
- `app/core/` - Global configurations and settings.
- `app/db/` - SQLite database models and session management.
- `app/engine/` - Core solver logic and calculation kernel.
- `app/engine/units/` - Process Units and Smart Units logic (Mixer, Heater, Pump, AIAgent, etc.).
- `app/exporters/` - Export logic for structured results.
- `app/schemas/` - Pydantic schemas for data validation and serialization.
- `flowsheets/` - JSON flowsheet definitions.
- `migrations/` - Alembic database migration scripts.
- `scripts/` - CLI utilities (e.g., seeding data, running flowsheets).
- `tests/` - Pytest suites.

## Python & State Rules
- **TypeScript/Python rules**: Strict typing. Avoid `Any`. Rely on Pydantic for robust data validation.
- **State**: The engine is stateless; all state is passed via JSON flowsheets or persisted in SQLite.
- Output MUST always be structured JSON + logs.

## Secret Rules
- Never expose keys or database credentials in the codebase.
- Rely on environment variables via Pydantic Settings and `.env`.

## Decision Rules
- Ask before installing new libraries or expanding dependencies.
- Ask before modifying the core solver architecture or the flowsheet JSON contract.

## Communication
Be concise. Explain what changed and how to test it.

## Git & Version Control
- **Commit Messages**: Follow Conventional Commits format (`feat:`, `fix:`, `chore:`, `refactor:`, `docs:`). Messages must clearly describe *what* changed and *why*, suitable for professional open-source review.
- **Versioning**: Follow Semantic Versioning (SemVer) strictly:
  - **MAJOR (X.0.0)**: Core architecture changes or breaking JSON contract modifications.
  - **MINOR (0.X.0)**: New unit operations (e.g., Smart Units) or new endpoints.
  - **PATCH (0.0.X)**: Bug fixes or validation message improvements.

## Final Reminder
Before every feature:
- Read this file.
- Follow it strictly.
- Build clean, simple code.
