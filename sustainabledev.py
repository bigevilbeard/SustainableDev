import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

# Load the data
data = pd.read_csv('data.csv')

# Preprocess the data
data = data.dropna()

# Define the features and the target variable
features = data.drop('energy_consumption', axis=1)
target = data['energy_consumption']

# Split the data into training and testing sets
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train the model
model = GradientBoostingRegressor(random_state=42)
model.fit(features_train, target_train)

# Make predictions on the testing set
predictions = model.predict(features_test)

# Evaluate the model
mse = mean_squared_error(target_test, predictions)
print('Mean Squared Error:', mse)

# Function to recommend the most energy-efficient programming language for a given project
def recommend_language(project_details):
    prediction = model.predict([project_details])
    if prediction < 100:
        return 'Python'
    elif prediction < 200:
        return 'JavaScript'
    elif prediction < 300:
        return 'Java'
    else:
        return 'C++'

# Example usage
project_details = {'functionality': 'web development', 'performance_requirements': 'low latency', 'codebase_size': 'small'}
recommended_language = recommend_language(project_details)
print('Recommended Language:', recommended_language)
