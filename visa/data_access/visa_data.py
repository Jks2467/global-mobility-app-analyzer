from visa.configuration.mongo_db_connection import MongoDBConnection
from typing import Optional
import pandas as pd
import numpy as np
from visa.constants import DB_NAME, MONGODB_URL
from dotenv import load_dotenv
import os
from pathlib import Path

env_path = os.path.join(Path.cwd(), '.env')

load_dotenv(env_path)
print(env_path)

db = DB_NAME
url = MONGODB_URL

class VisaData:
    def __init__(self):
        try:
            self.mongo_client = MongoDBConnection(database_name=db, mongodburl=url).Client
        except Exception as e:
            raise Exception(f"Failed to initialize: {e}")
        
    def get_collection_as_df(self, collection_name:str, database_name:Optional[str]= None) -> pd.DataFrame:
        try:
            if database_name is None:
                collection = self.mongo_client[db][collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns:
                df.drop(columns=['_id'], inplace=True)

            df.replace({pd.NA: np.nan}, inplace=True)
            return df
        except Exception as e:
            raise Exception(f"Error getting collection: {e}")