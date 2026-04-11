from visa.entity.config_entity import DataIngestionConfig
import pandas as pd
from visa.data_access.visa_data import VisaData
from visa.logger import logging
import os
from sklearn.model_selection import train_test_split
from visa.entity.artifact_entity import DataIngestionArtifact


class DataIngestion:
    def __init__(self, data_ingestion_config = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise Exception(f"error initializing data ingestion config : {e}")
        
    def export_data_into_feature_store(self) -> pd.DataFrame:
        try:
            logging.info("Extracting data from MongoDB Collection")
            visa_data = VisaData()
            dataframe = visa_data.get_collection_as_df(collection_name=self.data_ingestion_config.collection_name)
            logging.info(f"Dataframe Shape: {dataframe.shape}")
            feature_store_dir = self.data_ingestion_config.feature_store_dir
            os.makedirs(feature_store_dir, exist_ok=True)
            logging.info(f"Exporting data to feature store: {feature_store_dir}")
            dataframe.to_csv(f"{feature_store_dir}.csv", index=False, header=True)
            logging.info("Data exported to feature store successfully")
            return dataframe
        except Exception as e:
            raise Exception(f"Error exporting data to feature store: {e}")


    def split_data_as_train_test(self, dataframe: pd.DataFrame) -> None:
        try:
            logging.info("Splitting data into train and test sets")
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info(f"Split done Train Shape : {train_set.shape} and Test Shape: {test_set.shape}")
            os.makedirs(os.path.dirname(self.data_ingestion_config.training_dir), exist_ok=True)
            os.makedirs(os.path.dirname(self.data_ingestion_config.test_dir), exist_ok=True)
            logging.info(f"Exporting Data to Train and Test Folders")

            train_set.to_csv(self.data_ingestion_config.training_dir)
            test_set.to_csv(self.data_ingestion_config.test_dir)

            logging.info("Successfuly exported the split data")
        except Exception as e:
            raise Exception(f"Error splitting the data: {e}")
        

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            dataframe = self.export_data_into_feature_store()
            logging.info(f"Exported data into feature store. DF Shape : {dataframe.shape}")

            self.split_data_as_train_test(dataframe=dataframe)
            logging.info(f"Successfully split the data.")

            data_ingestion_artifact = DataIngestionArtifact(train_file_path=self.data_ingestion_config.training_dir,
                                                            test_file_path=self.data_ingestion_config.test_dir)
            
            logging.info(f"Data Ingestion Artifact initialized: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise Exception(f"Error in data ingestion artifact {e}")

