import sys  # Importing the sys module to interact with the Python runtime environment
from src.logger import logging  # Importing logging from a custom logger module in the src package

def error_message_detail(error, error_detail: sys):
    # Function to generate a detailed error message
    _, _, exc_tb = error_detail.exc_info()  # Extract the traceback object from the sys module
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the name of the file where the error occurred
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)  # Format the error message with file name, line number, and error message
    )
    return error_message  # Return the detailed error message

class CustomException(Exception):
    # Custom exception class inheriting from Python's built-in Exception class
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Initialize the base Exception class with the error message
        self.error_message = error_message_detail(error_message, error_detail=error_detail)  # Generate and assign the detailed error message

    def __str__(self):
        return self.error_message  # Return the detailed error message when the exception is printed

'''
------Summary of the code-----------------
The provided code defines a custom exception class CustomException that enhances the standard Python exception by including 
detailed information about where the error occurred (the file name and line number). This is achieved using the sys module
to extract the traceback information. The error_message_detail function formats this information into a readable string, 
which is then used as the exception's error message.
'''