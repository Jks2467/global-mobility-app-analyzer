import os
from visa.constants import *
from datetime import datetime
from dataclasses import dataclass

TIMESTAMP = datetime.now().strftime('YYYYMMDD_HHMMSS')

@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE
    artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)
    timestamp: str = TIMESTAMP


training_pipeline_config = TrainingPipelineConfig()


@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR)
    feature_store_dir: str = os.path.join(data_ingestion_dir, FEATURE_STORE_DIR)
    ingested_dir: str = os.path.join(data_ingestion_dir, INGESTED_DIR)
    train_test_split_ratio: float = TRAIN_TEST_SPLIT_RATIO
    training_dir: str = os.path.join(ingested_dir, TRAIN_FILENAME)
    test_dir: str = os.path.join(ingested_dir, TEST_FILENAME)
    collection_name: str = COLLECTION_NAME