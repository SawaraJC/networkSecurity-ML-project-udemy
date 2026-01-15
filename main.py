from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig

if __name__ == '__main__':
    try:
        logging.info("Before data ingestion stage")
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Data ingestion initiated")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        logging.info("Data ingestion completed")
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)