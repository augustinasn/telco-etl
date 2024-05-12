# telco-etl

## Description
This project is designed to perform data extraction, transformation, and loading (ETL) from multiple source files into a PostgreSQL database. It includes functionalities to deploy the database set up its schema, transform & load raw data into the database, and create analytical views based on predefined SQL scripts.

## Project structure
```
│   .env                
│   .gitignore
│   constants.py
│   docker-compose.yml
│   Dockerfile
│   main.py
│   README.md
│   requirements.txt
│           
├───data/
│       gsm.csv
│       lte.csv
│       site.csv
│       umts.csv
│       
├───logs/
│       .gitkeep
│       
└───src/
    │   logger.py
    │   transformation.py
    │   
    ├───db/
    │       models.py
    │       __init__.py
    │       
    └───sql/
            cells_per_frequency_for_sites.sql
            cells_per_technology_for_sites.sql
```

- `main.py`: The main script orchestrating the ETL process.
- `constants.py`: Contains project-wide constants and configurations.
- `src/logger.py`: Logger setup for logging messages.
- `src/transformation.py`: Functions for data transformation.
- `src/db`: Database related functionalities.
- `src/sql`: SQL scripts for creating views.

## Setup and usage
1. Clone the repository.
2. Ensure you have Docker installed.
3. Rename `.env_example` to `.env` and fill in the required environment variables.
4. Run `docker-compose up` to build and start the Docker containers.
5. Once the containers are running, connect to the database via a db browser of your choice at `localhost:5432` to inspect the results (use credentials from .env file).
6. To troubleshoot the process refer to the `debug.log` file that will be generated in the `logs/` subdirectory.