-- This script runs as the POSTGRES_USER (db_user) in the POSTGRES_DB (db)
-- The 'db_user' needs to have privileges to create users and databases,
-- which it does by default as the initial user.

-- 1. Create the 'airflow' user first
CREATE USER airflow WITH PASSWORD 'airflow';

-- 2. Create the 'airflow_db' database and explicitly set its owner to 'airflow'
CREATE DATABASE airflow_db OWNER airflow;

-- 3. (Optional but good practice) Grant all privileges on the airflow_db to the airflow user.
-- This might seem redundant since 'airflow' is the owner, but it can help
-- ensure all necessary privileges are explicitly set and cover future objects.
GRANT ALL PRIVILEGES ON DATABASE airflow_db TO airflow;

-- You can also revoke connect privileges from the public schema if desired for security.
-- REVOKE CONNECT ON DATABASE airflow_db FROM PUBLIC;

-- Add any other initializations for the 'db' database or other purposes here if needed.