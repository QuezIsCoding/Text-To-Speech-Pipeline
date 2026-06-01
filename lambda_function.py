import json
import boto3

#Instantiating clients outside the handler to enable warm reuse accross handlers
s3_client = boto3.client('s3')
polly_client = boto3.client('polly')

def lambda_handler(event, context):
    try:
        #1.) Parse out the operational s3 event metadata from the incoming trigger payload 
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']

        print(f"Inbound payload detected :{file_key} within S3 bucket :{bucket_name}")

        #Security guard Clause: stop execution if a wrong file format hits the s3 bucket
        if not file_key.endswith('.txt'):
            print(f"Stopping process. S3 object {file_key} is not in '.txt' format.")
            return {'statusCode': 200, 'body': 'Skipped non-txt source file.'}
        
        #Print successful parse message
        print("Validation successful!, This is a '.txt' file.")
        return {'statusCode': 200, 'body': 'File validation successful.'}
    except Exception as error:
        print(f"Fatal operational exception occured: {str(error)}")
        raise error