# Rising Ahead Data Engineering Assignment

## Tech Stack
- Python
- Dagster
- PostgreSQL
- Docker
- Pandas
- SQLAlchemy

## Project Structure

connectors/
pipeline/
data/
screenshots/

## How to Run

### Start PostgreSQL
docker compose up -d

### Install dependencies
pip install -r requirements.txt

### Run Dagster
py -m dagster dev -f pipeline/definitions.py

## Layers

### Bronze
Raw ingestion from CSV files.

### Silver
Cleaned and transformed datasets.

### Gold
Customer summary analytics dataset.

## Features
- Dagster assets
- PostgreSQL integration
- Change detection using row hash
- Dockerized setup
- Layered architecture

## Screenshots
See screenshots folder.

## Future Improvements
- Add schedules
- Add sensors
- Add asset checks
- Add unit tests
- Add incremental loading