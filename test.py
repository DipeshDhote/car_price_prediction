from src.car_price_prediction.logger import logging
from src.car_price_prediction.exception import CustomException
from src.car_price_prediction.components.data_ingestion import DataIngestion
from src.car_price_prediction.components.data_ingestion import DataIngestionConfig
import sys

if __name__== "__main__":
    logging.info("The excection has started")

    try:
        # Data Ingestion
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(e,sys)