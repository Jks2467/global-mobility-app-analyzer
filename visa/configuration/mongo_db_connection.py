import os
from visa.constants import DB_NAME, MONGODB_URL
from visa.logger import logging
from pymongo import MongoClient
import certifi

ca = certifi.where()
mongo_db_url = MONGODB_URL

class MongoDBConnection:
    Client = None
    def __init__(self, database_name=DB_NAME, mongodburl=mongo_db_url):
        try:
            if mongodburl is None:
                raise Exception("MongoDB URL is not set in environment variables.")
            MongoDBConnection.Client = MongoClient(mongodburl, tlsCAFile=ca)
            self.client = MongoDBConnection.Client
            self.database = self.client[database_name]
            logging.info("Successfully connected to MongoDB.")
        except Exception as e:
            logging.error(f"Error connecting to MongoDB: {e}")
            raise e