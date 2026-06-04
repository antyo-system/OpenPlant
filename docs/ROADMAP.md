# Roadmap & To-Do List (MVP v0.1)

This document tracks the phases and specific tasks required to complete the OpenPlant MVP.

## Phase 1: Project Scaffolding & Database Setup
*Goal: Establish the foundation, database connection, and reference data.*

- [x] **Initialize Database Models**: Create SQLAlchemy models for `components`, `property_correlations`, `steam_tables`, `equipment_templates`.
- [x] **Initialize Engine Models**: Create SQLAlchemy models for `flowsheets`, `streams`, `units`, `calculations`, `results`, `validation_logs`.
- [x] **Alembic Setup**: Generate the initial Alembic migration (`alembic revision --autogenerate`) and apply it.
- [x] **Seed Data Script**: Complete `scripts/seed_reference_data.py` to insert basic chemical components (e.g., Water, Methane).
- [x] **API Health Check**: Ensure `GET /health` is fully functional and verifies database connectivity.

## Phase 2: Core Engine & JSON Contract
*Goal: Build the robust JSON flowsheet parser and the core solver kernel.*

- [x] **Pydantic Schemas**: Define strict schemas in `app/schemas/` for Streams, Units, and the overall Flowsheet.
- [x] **Flowsheet Validator**: Implement `app/engine/validator.py` to catch structural errors and provide VSCode-style warnings/fix suggestions.
- [x] **Solver Kernel Loop**: Implement the main execution loop in `app/engine/solver.py` that reads the JSON, topological-sorts the units, and prepares state.

## Phase 3: Unit Operations (MVP Models)
*Goal: Implement the actual chemical engineering mathematics for the MVP units.*

- [x] **Base Unit Class**: *(DELETED)* We skipped creating an OOP Abstract Base Class. Following **Step 2 & 3 (Delete & Simplify)** of our philosophy, the engine uses a stateless functional `@register` registry (`app/engine/registry.py`). It's simpler and avoids unnecessary boilerplate.
- [x] **Mixer Solver**: Implement mass balance logic (combine multiple inlet streams into one outlet).
- [x] **Heater/Cooler Solver**: Implement simple energy balance logic (temperature change given heat duty, or heat duty given temperature change).
- [x] **Pump Solver**: Implement simple pressure drop (ΔP) and basic power estimation calculations.

## Phase 4: Integration & Output
*Goal: Connect the engine to the API and CLI, ensuring standardized JSON outputs.*

- [ ] **Solve API Endpoint**: Implement `POST /solve` in FastAPI. It must parse the JSON, trigger the Engine, and return the structured result + logs.
- [ ] **CLI Script**: Finalize `scripts/run_flowsheet.py` to allow local testing and saving results to `results/`.
- [ ] **End-to-End Test**: Run `demo_mixer_heater_pump.json` successfully from start to finish via API and CLI.

---

## Future Phases (Post-MVP)
*To be prioritized only after MVP v0.1 is 100% complete and tested.*

- [ ] **Thermodynamics Engine**: Implement real Cp(T) and Antoine vapor pressure equations.
- [ ] **Flash Separator**: VLE calculations with K-values.
- [ ] **Distillation Column**: Shortcut FUG method.
- [ ] **Exporters**: Build modules to export JSON results to Excel/PDF.
