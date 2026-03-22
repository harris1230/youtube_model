import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv("INvideos.csv")
df = df.dropna()

# Feature Engineering
df['title_length'] = df['title'].apply(len)

# Features
X = df[['likes', 'comment_count', 'title_length']]
y = df['views']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model Ready 🚀")