# Import necessary libraries and modules
from flask import Flask, request, render_template  # Flask for web framework, request for handling HTTP requests, render_template for rendering HTML templates
import numpy as np  # NumPy for numerical operations
import pandas as pd  # Pandas for data manipulation

# Importing additional modules from scikit-learn and custom pipeline
from sklearn.preprocessing import StandardScaler  # StandardScaler for feature scaling (not used directly in this code)
from src.pipeline.predict_pipeline import CustomData, PredictPipeline  # CustomData and PredictPipeline from the project's pipeline

# Initialize Flask application
application = Flask(__name__)  # Create a Flask application instance, it is like a entry point to flask

# Alias 'app' to 'application' for convenience
app = application  # Alias for the Flask application instance

# Define route for the home page
@app.route('/')  # Define route for the root URL ('/')
def index():  # Define the view function for the home page
    return render_template('index.html')  # Render and return the 'index.html' template

# Define route for the data prediction page
@app.route('/predictdata', methods=['GET', 'POST'])  # Define route for '/predictdata' with GET and POST methods
def predict_datapoint():  # Define the view function for predicting data points
    if request.method == 'GET':  # If the request method is GET
        return render_template('home.html')  # Render and return the 'home.html' template
    else:  # If the request method is POST
        # Create an instance of CustomData with form data
        data = CustomData(
            gender=request.form.get('gender'),  # Get 'gender' from the form data
            race_ethnicity=request.form.get('ethnicity'),  # Get 'ethnicity' from the form data
            parental_level_of_education=request.form.get('parental_level_of_education'),  # Get 'parental_level_of_education' from the form data
            lunch=request.form.get('lunch'),  # Get 'lunch' from the form data
            test_preparation_course=request.form.get('test_preparation_course'),  # Get 'test_preparation_course' from the form data
            reading_score=float(request.form.get('writing_score')),  # Get 'writing_score' from the form data and convert to float
            writing_score=float(request.form.get('reading_score'))  # Get 'reading_score' from the form data and convert to float
        )
        # Convert the data to a DataFrame
        pred_df = data.get_data_as_data_frame()  # Convert CustomData instance to a pandas DataFrame
        print(pred_df)  # Print the DataFrame for debugging
        #print("Before Prediction")  # Debugging statement before prediction

        # Initialize prediction pipeline and make prediction
        predict_pipeline = PredictPipeline()  # Create an instance of PredictPipeline
        #print("Mid Prediction")  # Debugging statement during prediction
        results = predict_pipeline.predict(pred_df)  # Predict using the DataFrame and get results
        #print("after Prediction")  # Debugging statement after prediction

        # Render the 'home.html' template with the prediction results
        return render_template('home.html', results=results[0])  # Render 'home.html' with the prediction result

# Run the application
if __name__ == "__main__":  # Check if the script is run directly
    app.run(host="0.0.0.0", debug=True)  # Start the Flask application, enabling debug mode, and make it accessible from all network interfaces
