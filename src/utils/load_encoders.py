import pickle

# Load the label encoder for Country
with open('encoders/label_encoder_country.pkl', 'rb') as file:
    label_encoder_country = pickle.load(file)

# Load the label encoder for Status
with open('encoders/label_encoder_status.pkl', 'rb') as file:
    label_encoder_status = pickle.load(file)
