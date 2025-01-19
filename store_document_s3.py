import boto3
import base64

# Initialize the S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Extract inputs from the event
        bucket_name = "my-lambda-bucket-unique"  # Your bucket name
        file_name = event.get('file_name', '')  # File name
        file_content_base64 = event.get('file_content', '')  # Base64-encoded content

        # Validate inputs
        if not file_name or not file_content_base64:
            return {
                'statusCode': 400,
                'body': 'Invalid input. Provide file_name and file_content.'
            }

        # Decode Base64 content
        file_content = base64.b64decode(file_content_base64)

        # Upload the file to S3
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_content
        )

        return {
            'statusCode': 200,
            'body': f"File '{file_name}' successfully uploaded to bucket '{bucket_name}'."
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"An error occurred: {str(e)}"
        }
