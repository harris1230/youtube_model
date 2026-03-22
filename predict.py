import pickle

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Example input
likes = 5000
comments = 300
title_length = 50

prediction = model.predict([[likes, comments, title_length]])

print("Predicted Views:", int(prediction[0]))