#1.S3 Trigger setup - done


#2.read the data file that was upload via s3 event

import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("Received event:", json.dumps(event, indent=2))
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    print(f"Reading file from bucket: {bucket}, key: {key}")
    
    response = s3.get_object(Bucket=bucket, Key=key)
    data = response['Body'].read().decode('utf-8')
    
    print("File content:")
    print(data)
    
    return {
        'statusCode': 200,
        'body': json.dumps(f"Successfully processed {key} from {bucket}")
    }

#3.write a separate file into s3 "output" prefix

import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("Received event:", json.dumps(event, indent=2))

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    print(f"Reading file from bucket: {bucket}, key: {key}")

    response = s3.get_object(Bucket=bucket, Key=key)
    file_content = response['Body'].read().decode('utf-8')

    print("File content:")
    print(file_content)

    try:
        data = json.loads(file_content)
        
        record_count = len(data)
        avg_age = round(sum(item.get("Age", 0) for item in data) / record_count, 2)

        print(f"Found {record_count} records. Average Age = {avg_age}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file content.")
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid JSON format!')
        }

    output_data = {
        "input_file": key,
        "record_count": record_count,
        "average_age": avg_age
    }

    output_key = f"output/{key.split('/')[-1].replace('.json', '_summary.json')}"

    s3.put_object(
        Bucket=bucket,
        Key=output_key,
        Body=json.dumps(output_data, indent=2),
        ContentType='application/json'
    )

    print(f"Output written to s3://{bucket}/{output_key}")

    return {
        'statusCode': 200,
        'body': json.dumps('File processed successfully!')
    }
