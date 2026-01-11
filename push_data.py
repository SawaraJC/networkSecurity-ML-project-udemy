import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from dotenv import load_dotenv

load_dotenv()
uri = os.getenv("MONGO_DB_URI")

ca = certifi.where()

class NetwrokDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def cv_to_json_converter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = data.to_dict(orient="records")
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database = database
            self.collection=collection
            self.records=records
            self.mongo_client = pymongo.MongoClient(uri)
            self.database = self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
if __name__=='__main__':
    FILE_PATH = "Network_Data\\phisingData.csv"
    DATABASE = "sanwcha"
    Collection = "networkData"
    networkobj = NetwrokDataExtract()
    records=networkobj.cv_to_json_converter(file_path=FILE_PATH)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)