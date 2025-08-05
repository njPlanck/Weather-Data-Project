Weather Data Ingestion Pipeline
A production-grade ETL pipeline to extract live weather data from the WeatherStack API, load it into a PostgreSQL database, and enable visualization with Apache Superset. The entire workflow is containerized with Docker and orchestrated using Apache Airflow for reliability and scalability.

### Features
Automated ETL: Fetches data from the WeatherStack API.

Data Storage: Loads structured data into a PostgreSQL table.

Orchestration: Manages and schedules data jobs with Apache Airflow.

Visualization: Supports data analysis and dashboard creation via Apache Superset.

Containerized: Fully portable and reproducible environment using Docker Compose.

###Tech Stack
Language: Python

Databases: PostgreSQL

Orchestration: Apache Airflow

Deployment: Docker, Docker Compose

APIs: WeatherStack (REST)

BI: Apache Superset

### Quickstart
Clone the repository:

Bash

git clone https://github.com/njPlanck/Weather-Data-Project.git
cd weather_pipeline
Configure API and DB credentials:

Update extract_weather.py and weather_etl_dag.py with your credentials or use environment variables.

Launch services with Docker Compose:

Bash

docker-compose up --build
Initialize the database schema:

Bash

docker exec -it <postgres_container> psql -U postgres -d weather_data -f /db/schema.sql
Access Services:

Airflow UI: http://localhost:8080 (admin/admin)

Superset UI: http://localhost:8088 (admin/admin)

# Project Structure
weather_pipeline/
├── dags/
│ └── weather_etl_dag.py # Airflow DAG for orchestration
├── scripts/
│ └── extract_weather.py # Python script for data extraction
├── db/
│ └── schema.sql # SQL schema for the PostgreSQL table
└── docker-compose.yml # Main Docker configuration