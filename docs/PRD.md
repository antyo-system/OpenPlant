# Product Requirements Document (PRD): Open Process Engine (OpenPlant)

## 1. Project Overview
**Open Process Engine (OpenPlant)** is a modular, open-source process calculation engine designed to act as an "n8n for Chemical Engineers". It blends classic chemical engineering rigor with modern AI agent workflows. It reads JSON flowsheets, solves mass and energy balances per unit operation, and outputs structured JSON results. It is built to be 1000x lighter than legacy simulators, making it accessible to chemical engineers and UMKM (Small-Medium Enterprise) entrepreneurs alike.

## 2. Goals & Objectives
- **Single Source of Truth**: Serve as the core calculation engine for process engineering.
- **Stream is King**: Maintain strict chemical engineering domains. All data moving between nodes (whether Process Units or Smart AI Units) MUST be a thermodynamic stream.
- **Portability**: Utilize JSON for flowsheet definitions to ensure they are portable and versionable.
- **Robust Validation**: Provide VSCode-like errors and warnings for process definitions.
- **Hybrid Modularity**: Implement a modular solver architecture combining `ProcessUnits` (Mixers, Reactors) and `SmartUnits` (AI Predictors, API Callers).
- **Ultra-Lightweight**: Zero-config SQLite database backend (no Docker needed).

## 3. Scope (MVP v0.1)

### 3.1 Unit Operations (Process Units)
The MVP will support the following foundational unit operations:
- **Mixer**: Solves mass balances.
- **Heater/Cooler**: Solves simple energy balances.
- **Pump**: Estimates pressure drop (ΔP) and basic power requirements.

### 3.2 Reference Data Tables (SQLite)
- `components`: Chemical components library.
- `property_correlations`: Property models.
- `equipment_templates`: Baseline configurations for equipment.

### 3.3 Engine Tables (Database)
- `flowsheets`, `streams`, `units`, `calculations`, `results`, `validation_logs`

## 4. User Scenarios
- **Chemical Engineer**: Runs a complex flowsheet simulation via API and gets rigorous thermodynamic results.
- **UMKM Entrepreneur**: Uses the drag-and-drop UI (future) to map out their coffee roasting process, utilizing AI Smart Nodes to predict roast quality based on temperature streams.
- **AI Agent**: Reads validation errors from the engine and automatically suggests JSON fixes to the user.

## 5. Roadmap & Future Features
- **Smart Units (V5 Vision)**: Integrate LLM agents as functional unit operations within the flowsheet.
- **Flash Separator**: Incorporate Vapor-Liquid Equilibrium (VLE) and simple K-values.
- **Advanced Thermodynamics**: Add temperature-dependent heat capacities (Cp(T)) and Antoine equations.
- **UI Integration**: Develop a full User Interface connector with AI-driven suggestions (React + Vanilla CSS).
