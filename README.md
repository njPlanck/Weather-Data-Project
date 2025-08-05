# 🌦️ Weather Data Ingestion Pipeline

A production-grade data pipeline that extracts live weather data from the WeatherStack API, stores it in PostgreSQL, and enables visualization via Apache Superset. Orchestrated using Apache Airflow and Docker for reliability and scalability.

---

## 🔧 Tech Stack

- **Language**: Python
- **Database**: PostgreSQL
- **Scheduler**: Apache Airflow
- **API**: WeatherStack (REST)
- **Visualization**: Apache Superset
- **Deployment**: Docker, Docker Compose

---

## 📁 Project Structure

weather_pipeline/
├── dags/
│ └── weather_etl_dag.py # Airflow DAG
├── scripts/
│ └── extract_weather.py # Script to fetch and load data
├── db/
│ └── schema.sql # SQL schema for weather table
├── docker/
│ ├── docker-compose.yml # Multi-service container config
│ └── Dockerfile # (Optional) Custom images
├── superset/
│ └── superset_config.py # Superset config if needed
├── requirements.txt # Python dependencies
└── README.md

yaml
Kopieren
Bearbeiten

---

## 🚀 Setup Guide (Using Docker)

### 1. Clone & Configure

```bash
git clone https://github.com/yourusername/weather_pipeline.git
cd weather_pipeline
Update your WeatherStack API key and PostgreSQL credentials inside:

scripts/extract_weather.py

dags/weather_etl_dag.py

Or set them as environment variables.

2. Launch with Docker Compose
bash
Kopieren
Bearbeiten
docker-compose up --build
This will spin up:

Airflow Scheduler & Webserver

PostgreSQL Database

Superset

Airflow Worker (if Celery used)

3. Initialize Database Schema
After services are up:

bash
Kopieren
Bearbeiten
docker exec -it <postgres_container> psql -U postgres -d weather_data -f /db/schema.sql
4. Access Services
Airflow UI → http://localhost:8080

Superset → http://localhost:8088

Use default credentials (admin/admin) unless customized.

✅ Features
Automated ETL: Weather data pulled from WeatherStack API

Data Storage: Stored in structured PostgreSQL table

Scheduling: Orchestrated with Airflow DAGs

Visualization: Superset dashboards & SQL charts

Dockerized: Easily portable and reproducible

Error Handling & Deduplication included

📊 Superset Dashboard
Once data is loaded:

Log into Superset.

Connect to the PostgreSQL DB.

Add a new dataset using the weather_data table.

Build charts:

Temperature over time

Weather description counts

Add charts to a dashboard and share/report insights.

✏️ Example SQL Query for Superset
sql
Kopieren
Bearbeiten
SELECT
  city,
  AVG(temperature) as avg_temp,
  DATE_TRUNC('day', observation_time) as day
FROM weather_data
GROUP BY city, day
ORDER BY day;