# Student Performance Prediction

This repository contains the end-to-end implementation of a project for predicting student performance, from data ingestion to model deployment. 

## Project Workflow
- **Data Ingestion:** Loading and preprocessing the data from CSV files (data_ingestion.py).
- **Data Transformation:** Applying transformations to the data to prepare it for model training (data_transformation.py).
- **Model Training:** Training the machine learning model using CatBoost (model_trainer.py).
- **Model Serialization:** Saving the trained model and preprocessor for deployment (model.pkl, preprocessor.pkl).
- **Deployment:** Deploying the model using Flask (app.py, application.py) and configuring the deployment environment (.ebextensions/).

## Reference

1. https://github.com/krishnaik06/mlproject

This project demonstrates a complete workflow from data preparation to model deployment, suitable for production use.
