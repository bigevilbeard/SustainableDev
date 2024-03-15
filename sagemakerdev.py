# Import necessary libraries
import boto3
import sagemaker
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

# Load the data from Amazon S3
sagemaker_session = sagemaker.Session()
bucket = sagemaker_session.default_bucket()
data_key = 'data.csv'
data_location = 's3://{}/{}'.format(bucket, data_key)
data = pd.read_csv(data_location)

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

# Save the model to Amazon S3
model_data = sagemaker.get_execution_role().assume_role().arn
model_name = 'sustainable-dev-ai'
model_path = 's3://{}/{}/output'.format(bucket, model_name)
sagemaker.session.s3_input(model_path, distribution='FullyReplicated', content_type='text/csv')
model.save(model_path)

# Create a SageMaker model
sagemaker_model = sagemaker.model.Model(model_name, role=sagemaker_session.default_
