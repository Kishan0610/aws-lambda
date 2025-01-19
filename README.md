## AWS Lambda Functions

### Function 1: Add Two Numbers
- **File**: `add_two_numbers.py`
- **Description**: This function takes two numbers as input (via an API Gateway) and returns their sum.
- **Deployment Instructions**:
  1. Create a Lambda function in the AWS Management Console.
  2. Test the function.

### Function 2: Store Document in S3
- **File**: `store_document_s3.py`
- **Description**: This function uploads a document to an S3 bucket.
- **Deployment Instructions**:
  1. Create an S3 bucket in AWS.
  2. Create a Lambda function in the AWS Management Console.
  3. Upload the `store_document_s3.py`.
  4. Test the function by passing a sample file.


 ### Screenshots
![AWS_addTwoNymbers_SS](https://github.com/user-attachments/assets/bdc033cc-c4c1-4842-83d9-0ac3620f3dac)
![AWS_S3Bucket_SS](https://github.com/user-attachments/assets/71506297-5a47-4854-b388-4946289844cd)
![AWS_S3Bucket_savedFile](https://github.com/user-attachments/assets/c81df564-6053-407c-9527-2d2a843f385c)


### Example Payloads
For Function 1:
```json
{
  "number1": 5,
  "number2": 10
}

For Function 2:
{
  "bucket_name": "my-lambda-bucket-unique",
  "file_name": "test.pdf",
  "file_content": "content.."
}

