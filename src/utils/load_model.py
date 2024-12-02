from imports import *
import base64

def load_model(filename):
   
    # Load a model from a file.
  
    with open(filename, "rb") as model_file:
        model = pickle.load(model_file)
        # model = base64.b64encode(model_file.read()).decode()
    print(f"Model loaded successfully from {filename}.")
    return model
