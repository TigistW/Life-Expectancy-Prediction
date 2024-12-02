from imports import *


def evaluate_model(model, X_data, y_true):
  
    # Use a trained model to make predictions and evaluate performance.
    
    # Make predictions
    predictions = model.predict(X_data)
    
    # Calculate evaluation metrics
    mae = mean_absolute_error(y_true, predictions)
    mse = mean_squared_error(y_true, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, predictions)
    
    # Print the metrics
    print("Evaluation Metrics:")
    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"Mean Squared Error (MSE): {mse}")
    print(f"Root Mean Squared Error (RMSE): {rmse}")
    print(f"R² Score: {r2}")
    
    # Return the metrics as a dictionary
    return {
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "R²": r2
    }
