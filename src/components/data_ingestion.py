import os  # Importing the os module for interacting with the operating system
import sys  # Importing the sys module to interact with the Python runtime environment
from pathlib import Path  # Importing Path from pathlib to handle filesystem paths
sys.path.append(str(Path('src').parent.parent))  # Adding the parent directory of 'src' to the system path
from src.exception import CustomException  # Importing the CustomException class from the src.exception module
from src.logger import logging  # Importing logging from a custom logger module in the src package
import pandas as pd  # Importing pandas for data manipulation and analysis

from sklearn.model_selection import train_test_split  # Importing train_test_split for splitting data into training and test sets
from dataclasses import dataclass  # Importing dataclass for creating data classes

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

@dataclass
class DataIngestionConfig:
    # Configuration class for data ingestion paths
    train_data_path: str = os.path.join('artifacts', "train.csv")  # Path for the training data
    test_data_path: str = os.path.join('artifacts', "test.csv")  # Path for the test data
    raw_data_path: str = os.path.join('artifacts', "data.csv")  # Path for the raw data

class DataIngestion:
    def __init__(self):
        # Initializer for DataIngestion class
        self.ingestion_config = DataIngestionConfig()  # Create an instance of DataIngestionConfig

    def initiate_data_ingestion(self):
        # Method to initiate data ingestion
        logging.info("Entered the data ingestion method or component")  # Log entry into the method
        try:
            df = pd.read_csv('notebook\data\stud.csv')  # Read the dataset into a pandas DataFrame
            logging.info('Read the dataset as dataframe')  # Log successful reading of the dataset

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)  # Create the directory for data paths if it doesn't exist

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)  # Save the raw data to a CSV file

            logging.info("Train test split initiated")  # Log initiation of train-test split
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)  # Split the data into training and test sets

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)  # Save the training set to a CSV file
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)  # Save the test set to a CSV file
            
            logging.info("Ingestion of the data is completed")  # Log completion of data ingestion

            return (
                self.ingestion_config.train_data_path,  # Return the training data path
                self.ingestion_config.test_data_path  # Return the test data path
            )
        
        except Exception as e:
            raise CustomException(e, sys)  # Raise a custom exception with detailed error information

if __name__ == "__main__":
    
    obj=DataIngestion() # Create an instance of the DataIngestion class
    train_data,test_data=obj.initiate_data_ingestion() # Initiate the data ingestion process

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

'''
--------------Summary of the code---------
This code performs the ingestion of data for a machine learning project. 
It reads a dataset, splits it into training and test sets, 
saves these sets to specified paths, and logs the process.
It also handles exceptions using a custom exception class to provide detailed error information.
'''