from imports import *


def load_model(filename):
   
    # Load a model from a file.
  
    with open(filename, "rb") as model_file:
        model = pickle.load(model_file)
    print(f"Model loaded successfully from {filename}.")
    return model
