import os
from datetime import date
from dotenv import load_dotenv
from pathlib import Path


env_path = os.path.join(Path.cwd(), '.env')


load_dotenv(env_path)

# Database details
MONGODB_URL = os.environ['CONN_STRING']
DB_NAME=os.environ['DB_NAME']
COLLECTION_NAME=os.environ['COLLECTION_NAME']


# ML Constants
PIPELINE: str = 'visa_pipeline'
ARTIFACT_DIR: str = 'artifact'
MODEL_FILENAME: str = 'model.pkl'
TARGET_COLUMN = 'case_status'
CURRENT_YEAR = date.today().year
PREPROCESSING_OBJECT_FILENAME: str = 'preprocessing_object.pkl'

# data files constants
MAIN_FILENAME: str = 'EasyVisa.csv'
TRAIN_FILENAME: str = 'train.csv'
TEST_FILENAME: str = 'test.csv'
SCHEMA_FILEPATH: Path = os.path.join(Path.cwd(), 'config','schema.yaml')

# GCP Constants

# local data ingestion constants
DATA_INGESTION_DIR:str = 'data_ingestion'
FEATURE_STORE_DIR:str = 'feature_store'
INGESTED_DIR:str = 'ingested'
TRAIN_TEST_SPLIT_RATIO: float = 0.2