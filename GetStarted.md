# Running SustainableDev AI on AWS

To run the SustainableDev AI on AWS, follow these steps:

## Prerequisites

- Prepare your AWS account and necessary permissions.
- Create an S3 bucket to store the data and the trained model.
- Create an Amazon EMR cluster for data processing.

## 1. Prepare the data for training the model

- Upload the data to the S3 bucket.
- Process the data using Amazon EMR and store the processed data in the S3 bucket.

## 2. Train the model using Amazon SageMaker

- In the AWS Management Console, navigate to the Amazon SageMaker service.
- Create a new training job using the processed data in the S3 bucket.
- Store the trained model in the S3 bucket.

## 3. Deploy the model as a REST API using Amazon SageMaker

- In the AWS Management Console, navigate to the Amazon SageMaker service.
- Create a new endpoint using the trained model.

## 4. Create a Flask application to interact with the REST API

Create a Flask application with the following components:

- A route to handle incoming requests with project details.
- Code to send the project details to the SageMaker endpoint and receive the prediction.
- Code to process the prediction and return the recommended programming language.

## 5. Deploy the Flask application as a web service

- Package the Flask application as a Lambda function.
- Create an AWS Lambda function and upload the package.
- Create an API Gateway and link it to the Lambda function.

## Detailed Instructions

### Prepare your AWS account and necessary permissions:

1. Sign up for an AWS account if you don't have one.
2. Create an IAM user with necessary permissions for Amazon S3, Amazon EMR, Amazon SageMaker, and AWS Lambda.

### Create an S3 bucket to store the data and the trained model:

1. In the AWS Management Console, navigate to the Amazon S3 service.
2. Create a new S3 bucket with a unique name.

### Create an Amazon EMR cluster for data processing:

1. In the AWS Management Console, navigate to the Amazon EMR service.
2. Create a new EMR cluster with the necessary configurations.

### Prepare the data for training the model:

1. Upload the data to the S3 bucket.
2. Process the data using Amazon EMR and store the processed data in the S3 bucket.

### Train the model using Amazon SageMaker:

1. In the AWS Management Console, navigate to the Amazon SageMaker service.
2. Create a new training job using the processed data in the S3 bucket.
3. Store the trained model in the S3 bucket.

### Deploy the model as a REST API using Amazon SageMaker:

1. In the AWS Management Console, navigate to the Amazon SageMaker service.
2. Create a new endpoint using the trained model.

### Create a Flask application to interact with the REST API:

Create a Flask application with the following components:

- A route to handle incoming requests with project details.
- Code to send the project details to the SageMaker endpoint and receive the prediction.
- Code to process the prediction and return the recommended programming language.

### Deploy the Flask application as a web service:

1. Package the Flask application as a Lambda function.
2. Create an AWS Lambda function and upload the package.
3. Create an API Gateway and link it to the Lambda function.
