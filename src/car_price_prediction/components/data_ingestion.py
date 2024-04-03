import os 
import sys
from src.car_price_prediction.logger import logging
from src.car_price_prediction.exception import CustomException
import pandas as pd
from src.car_price_prediction.utils import read_sql_data
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestionconfig=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            df = read_sql_data()
            logging.info("reading complited from mysql database")

            os.makedirs(os.path.dirname(self.ingestionconfig.train_data_path),exist_ok=True)
            
            df.to_csv(self.ingestionconfig.raw_data_path,index=False,header=True)
        
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=40)

            train_set.to_csv(self.ingestionconfig.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestionconfig.test_data_path,index=False,header=True)

            logging.info("Data ingestion is completed")

            return (
                self.ingestionconfig.train_data_path,
                self.ingestionconfig.test_data_path
            )
 

        except Exception as e:
            raise CustomException(e,sys)
        