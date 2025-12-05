import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load model and scaler
model, scaler = pickle.load(open("rf_model.pkl", "rb"))

new_patient = [[3,118,70,36,0,34.6,0.727,30]]  # Example patient data

input_data = scaler.transform(new_patient)
prediction = model.predict(input_data)
print("Predicted outcome for the new patient: {}".format(prediction[0]))