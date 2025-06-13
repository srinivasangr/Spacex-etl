# Spacex-etl
ETL SpaceX
# SpaceX Data ETL Pipeline

This project is an ETL (Extract, Transform, Load) pipeline for fetching SpaceX data, transforming it into CSV format, and uploading it to an AWS S3 bucket. Additionally, the project includes a dbt project for transforming the data in Redshift and an Airflow DAG to orchestrate the pipeline.

---
[ETL Pipeline](fig1.png)
## Features

- Fetch SpaceX data from the SpaceX API.
- Extract specific fields from the data.
- Save the transformed data as a CSV file.
- Upload the CSV file to an AWS S3 bucket.
- Automate dbt transformations and tests using Airflow.

---

## Project Structure

```
Space_Ex/
├── extract_spacex_data.py   # Python script for fetching, transforming, and uploading SpaceX data
├── spacex_dag.py            # Airflow DAG for dbt transformations
├── spacex_pipeline/         # dbt project for Redshift transformations
│   ├── dbt_project.yml      # dbt project configuration
│   ├── models/              # dbt models
│   ├── logs/                # dbt logs
│   └── README.md            # dbt-specific documentation
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## Prerequisites

1. **Python 3.12**
2. **AWS CLI** configured with appropriate credentials.
3. **Airflow** installed and running.
4. **dbt** installed and configured for Redshift.

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Space_Ex
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure AWS credentials:
   ```bash
   aws configure
   ```

---

## Usage

### 1. Fetch and Upload SpaceX Data
Run the `extract_spacex_data.py` script to fetch SpaceX data, transform it into CSV format, and upload it to S3:
```bash
python extract_spacex_data.py
```

### 2. Airflow DAG for dbt Transformations
The `spacex_dag.py` file defines an Airflow DAG to run dbt transformations and tests.

1. Place the `spacex_dag.py` file in your Airflow DAGs directory.
2. Start the Airflow scheduler and webserver:
   ```bash
   airflow scheduler
   airflow webserver
   ```
3. Trigger the DAG `spacex_dbt_pipeline` from the Airflow UI.

---

## Configuration

### SpaceX Data Script (`extract_spacex_data.py`)
- **API_URL**: List of SpaceX API endpoints to fetch data from.
- **BUCKET_NAME**: Name of the S3 bucket where the CSV files will be uploaded.

### Airflow DAG (`spacex_dag.py`)
- **dbt_run**: Executes dbt transformations.
- **dbt_test**: Runs dbt tests.

### dbt Project (`spacex_pipeline/`)
- **dbt_project.yml**: Configuration file for the dbt project.
- **models/**: Contains dbt models for transforming SpaceX data in Redshift.

---

## Example Output

### CSV File
A sample CSV file uploaded to S3 will contain the following fields:
- `id`
- `name`
- `date_utc`
- `success`
- `rocket`
- `details`
- `flight_number`

### S3 Path
The CSV files are uploaded to the `csv/` folder in the specified S3 bucket.

---

## Dependencies

- **Python Libraries**:
  - `requests`
  - `boto3`
  - `csv`
  - `apache-airflow`
- **AWS Services**:
  - S3
- **Tools**:
  - dbt
  - Airflow

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Author
Srinivasan
