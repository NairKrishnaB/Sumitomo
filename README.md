Prerequisites
Python 3.11+
git
venv
Airflow

Execution steps
git clone https://github.com/NairKrishnaB/Sumitomo.git
cd datapipeline
python3 -m venv venv
source venv/bin/activate (for windows machine - venv\Scripts\activate)
pip install --upgrade pip
pip install -r requirements.txt
python -m etl.ingest
python -m etl.transform(Converting USD to GBP)
python -m etl.load

Verify Data
sudo apt install sqlite3
sqlite3 products.db
sqlite> .tables
sqlite> SELECT * FROM products LIMIT 5;


Running with Airflow
pip install "apache-airflow[celery,postgres,sqlite,fab]"
airflow db migrate
airflow connections create-default-connections
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password ******
export AIRFLOW_HOME=~/datapipeline/airflow_home
mkdir -p $AIRFLOW_HOME/dags
cp dags/dags/product_pipeline_dag.py $AIRFLOW_HOME/dags/
airflow standalone
airflow dags list
airflow dags trigger datapipeline_dag


Improved with more time

1) Add robust error handling for API failures and Implement retries
2) Write tests cases for each ETL module
3) I can set up this as Github action to perform CICD from Dev --> QA --> Production with approval
4) Move API URLs, database paths, thresholds, and currency codes to a .env or to scheduling tools environment variable
5) Implement structured logging for ETL steps and monitoring tools and alerts such as AWS cloudwatch, SNS, Datadog etc 
6) Add visualization layer on top of transformed data