import json
import boto3
import os
import logging

# Initialize the SNS client
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    try:
        # Extract the details from the event
        record = event['Records'][0]
        event_name = record['eventName']
        bucket_name = record['s3']['bucket']['name']
        object_name = record['s3']['object']['key']

        # Determine the type of event and give the appropriate message
        if event_name.startswith('ObjectCreated:'):
            action = 'uploaded to'
        elif event_name.startswith('ObjectRemoved:'):
            action = 'deleted from'
        else:
            action = 'affected in'  # Default action for unknown events

      #Format of the message
        message = (
            f"An object was {action} the bucket '{bucket_name}'. "
            f"The file name is '{object_name}'."
        )

        # Get the SNS Topic ARN from environment variables in labda function
        sns_topic_arn = os.environ.get('SNS_Topic_ARN')
        if not sns_topic_arn:
            raise ValueError("SNS_TOPIC_ARN environment variable is not set")

        # Publish the message to the SNS topic
        response = sns_client.publish(
            TopicArn=sns_topic_arn,
            Message=message,
            Subject=f'S3 {action.capitalize()} Notification',
        )

    except Exception as e:
        # Log the error
        print(f"Error processing S3 event: {e}")
        raise e
