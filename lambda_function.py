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
        
        #Print successful parse message for testing 
        #print("Validation successful!, This is a '.txt' file.")
        #return {'statusCode': 200, 'body': 'File validation successful.'}
    
        #2.) Fetch the text file contents down from the S3 storage ;ayer
        s3_object = s3_client.get_object(Bucket = bucket_name, Key= file_key)
        raw_text = s3_object['Body'].read().decode('utf-8')
        if not raw_text.strip():
            print("Target text payload is vacant. Terminating compute pass")
            return{'statusCode': 400, 'body': 'Source payload empty'}
        
        print(f"Successfully retrieved raw text: {raw_text}") #Temp print for testing.
       

    except Exception as error:
        print(f"Fatal operational exception occured: {str(error)}")
        raise error
    

