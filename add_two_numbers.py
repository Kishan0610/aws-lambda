def lambda_handler(event, context):
    # Extract numbers from the event object
    num1 = event.get('num1', 0)
    num2 = event.get('num2', 0)

    # Ensure the inputs are numbers
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return {
            'statusCode': 400,
            'body': 'Invalid input. Please provide two numbers.'
        }

    # Calculate the sum
    result = num1 + num2

    return {
        'statusCode': 200,
        'body': {
            'num1': num1,
            'num2': num2,
            'result': result
        }
    }
