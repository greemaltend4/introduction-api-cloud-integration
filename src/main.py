import json

def lambda_handler(event, context):
    # Traitement de la requête
    try:
        message = event.get('queryStringParameters', {}).get('message', 'Bonjour, monde!')
        response = {
            'statusCode': 200,
            'body': json.dumps({'message': message})
        }
    except Exception as e:
        response = {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
    return response
