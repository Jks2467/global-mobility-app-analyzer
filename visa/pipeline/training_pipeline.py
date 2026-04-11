from visa.entity.config_entity import DataIngestionConfig
from visa.components.data_ingestion import DataIngestion
from visa.entity.artifact_entity import DataIngestionArtifact
from visa.logger import logging


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Starting data ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data Ingestion completed: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise Exception(f"Error in start_data_ingestion: {e}")
        
    def run_pipeline(self):
        try:
            logging.info("Starting Training Pipeline")
            data_ingestion_artifact = self.start_data_ingestion()
            logging.info(f"Data Ingestion Artifact: {data_ingestion_artifact}")
            logging.info("Training Pipeline completed successfully")
        except Exception as e:
            raise Exception(f"Error in run_pipeline: {e}")