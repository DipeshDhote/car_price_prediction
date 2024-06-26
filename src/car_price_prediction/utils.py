import os 
import sys
from src.car_price_prediction.logger import logging
from src.car_price_prediction.exception import CustomException
import pandas as pd
import pymysql 
from dotenv import load_dotenv
import pickle
import numpy
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
import pymysql
import numpy as np
from dotenv import load_dotenv


load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password= os.getenv("password")
db = os.getenv('db')


def read_sql_data():
    logging.info("reading mySQL database started")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("connection established",mydb)
        df=pd.read_sql_query('select * from cars',mydb)
        print(df.head())

        return df
        

    except Exception as ex:
        raise CustomException(ex,sys)
    