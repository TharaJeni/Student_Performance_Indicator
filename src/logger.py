import logging  # Import the logging module to enable logging capabilities
import os  # Import the os module for interacting with the operating system
from datetime import datetime  # Import datetime to get the current date and time

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # Create a log file name with the current date and time

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)  # Define the path for the logs directory and log file
os.makedirs(logs_path, exist_ok=True)  # Create the logs directory if it doesn't exist

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)  # Define the full path for the log file

logging.basicConfig(
    filename=LOG_FILE_PATH,  # Set the log file path
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Define the log message format
    level=logging.INFO,  # Set the logging level to INFO
)



'''
-----------Summary of the code ---------
This code sets up a logging configuration that allows you to log messages to a file. 
The log file is named based on the current date and time, ensuring a unique file for each run. 
The logs are stored in a directory named "logs" in the current working directory. 
The logging configuration includes a specific format for the log messages and 
sets the logging level to INFO, meaning that all messages at this level or higher will be logged.
'''