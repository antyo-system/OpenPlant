# Product Requirements Document (PRD): Open Process Engine (OpenPlant)

## 1. Project Overview
**Open Process Engine (OpenPlant)** is a modular, open-source process calculation engine designed to act as a mini Aspen kernel. It reads JSON flowsheets, solves mass and energy balances per unit operation, and outputs structured JSON results. It is built to be easily integrated with UI, AI agents, and custom exporters.

## 2. Goals & Objectives
- **Single Source of Truth**: Serve as the core calculation engine for process engineering.
- **Portability**: Utilize JSON for flowsheet definitions to ensure they are portable and versionable.
- **Robust Validation**: Provide VSCode-like errors and warnings for process definitions, including actionable fix suggestions.
- **Modularity**: Implement a modular solver architecture for individual unit operations.
- **Structured Output**: Ensure outputs are consistently formatted in structured JSON along with execution logs.
- **Reference Data**: Maintain a robust PostgreSQL-backed database for components, properties, and equipment templates.

## 3. Scope (MVP v0.1)

### 3.1 Unit Operations
The MVP will support the following foundational unit operations:
- **Mixer**: Solves mass balances.
- **Heater/Cooler**: Solves simple energy balances.
- **Pump**: Estimates pressure drop (ΔP) and basic power requirements.

### 3.2 Reference Data Tables
- `components`: Chemical components library.
- `property_correlations`: Property models (placeholder for MVP).
- `steam_tables`: Steam property data (placeholder for MVP).
- `equipment_templates`: Baseline configurations for equipment (placeholder for MVP).

### 3.3 Engine Tables (Database)
- `flowsheets`, `streams`, `units`, `calculations`, `results`, `validation_logs`

## 4. User Scenarios
- **Engineer (CLI User)**: Runs a flowsheet via a CLI script (`python scripts/run_flowsheet.py`) and checks the `results.json`.
- **System Integrator (API User)**: Sends a POST request with a flowsheet JSON to the `/solve` endpoint and parses the resulting JSON.
- **AI Agent**: Reads validation errors from the engine and automatically suggests JSON fixes to the user.

## 5. Roadmap & Future Features
- **Flash Separator**: Incorporate Vapor-Liquid Equilibrium (VLE) and simple K-values.
- **Shortcut Distillation**: Implement Fenske/Underwood/Gilliland equations.
- **Advanced Thermodynamics**: Add temperature-dependent heat capacities (Cp(T)), density (rho(T,P)), and Antoine equations for vapor pressure.
- **Advanced Exporters**: Export results to Excel, PDF, and Word.
- **UI Integration**: Develop a full User Interface connector with AI-driven suggestions.
