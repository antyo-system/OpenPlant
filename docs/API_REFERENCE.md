# API Reference: Open Process Engine (OpenPlant)

## Base URL
Local development: `http://localhost:8000`

## 1. Health Check
Check if the API and database connections are healthy.

- **Endpoint**: `/health`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "status": "ok",
    "db_connection": "successful"
  }
  ```

## 2. Solve Flowsheet
Submits a JSON flowsheet to the calculation engine, runs the solver, and returns the calculated results and validation logs.

- **Endpoint**: `/solve`
- **Method**: `POST`
- **Request Body (JSON)**:
  Expects a standard Flowsheet JSON contract.
  ```json
  {
    "name": "Demo Flowsheet",
    "streams": [ ... ],
    "units": [ ... ],
    "connections": [ ... ]
  }
  ```
- **Response (JSON)**:
  Returns the solved flowsheet, stream properties, unit duties, and any validation errors/warnings encountered during execution.
  ```json
  {
    "flowsheet_id": "uuid",
    "status": "success",
    "calculation_results": { ... },
    "validation_logs": [ ... ]
  }
  ```

## 3. Reference Data (Planned)
Endpoints to fetch components and property correlations.
- `GET /components` - List available chemical components.
- `GET /equipment-templates` - List default equipment configurations.
