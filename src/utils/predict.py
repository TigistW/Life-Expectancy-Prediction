from imports import *

def predict_with_model(model, X_data):
   
    # Use a trained model to make predictions on given data.
    print(X_data)
    
    predictions = model.predict(X_data)
    return predictions