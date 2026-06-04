# Roadmap & To-Do List (MVP v0.1)

This document tracks the phases and specific tasks required to complete the OpenPlant MVP.

## Phase 1: Project Scaffolding & Database Setup (COMPLETED)
*Goal: Establish the foundation, database connection, and reference data.*
- [x] **Lightweight Database**: Replace PostgreSQL with zero-config SQLite.
- [x] **Initialize Engine Models**: Create SQLAlchemy models for flowsheets, streams, units.
- [x] **Seed Data Script**: Complete `scripts/seed_reference_data.py`.

## Phase 2: Core Engine & JSON Contract (COMPLETED)
*Goal: Build the robust JSON flowsheet parser and the core solver kernel.*
- [x] **Pydantic Schemas**: Define strict schemas in `app/schemas/` for Streams, Units, and the overall Flowsheet.
- [x] **Flowsheet Validator**: Implement `app/engine/validator.py` to catch structural errors.
- [x] **Solver Kernel Loop**: Implement the main execution loop in `app/engine/solver.py`.

## Phase 3: Unit Operations (COMPLETED)
*Goal: Implement the actual chemical engineering mathematics for the MVP units.*
- [x] **Mixer Solver**: Implement mass balance logic.
- [x] **Heater/Cooler Solver**: Implement simple energy balance logic.
- [x] **Pump Solver**: Implement simple pressure drop (ΔP).

## Phase 4: Integration & Output (COMPLETED)
*Goal: Connect the engine to the API and CLI, ensuring standardized JSON outputs.*
- [x] **Solve API Endpoint**: Implement `POST /solve` in FastAPI.
- [x] **CLI Script**: Finalize `scripts/run_flowsheet.py` to allow local testing.
- [x] **End-to-End Test**: Run `demo_mixer_heater_pump.json` successfully via CLI.

---

## Future Phases (Post-MVP)
*To be prioritized only after MVP v0.1 is 100% complete and tested.*

### Phase 5: The "Smart Unit" (AI Agent Integration)
- [ ] **Smart Unit Base**: Introduce a mechanism to register `SmartUnits` (e.g., AI LLM Nodes, Sensor Integrations).
- [ ] **Data Translation**: Ensure AI outputs conform strictly to thermodynamic `Stream` structures.

### Phase 6: Web UI Connector
- [ ] **Modern Web App**: Build a React + Vanilla CSS frontend using React Flow for drag-and-drop node interactions.

### Phase 7: Advanced Chemical Logic
- [ ] **Flash Separator**: VLE calculations with K-values.
- [ ] **Advanced Thermodynamics**: Implement real Cp(T) and Antoine vapor pressure equations.
