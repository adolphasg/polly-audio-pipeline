import boto3
import os
import sys

def synthesize(text_file_path, output_file_path):
    try:
        with open(text_file_path, 'r') as file:
            text = file.read()
        print("Read text from file.")

        polly = boto3.client(
            'polly',
            region_name='us-east-1',
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
        )
        print("Initialized Polly client.")

        response = polly.synthesize_speech(Text=text, OutputFormat='mp3', VoiceId='Joanna')

        with open(output_file_path, 'wb') as file:
            file.write(response['AudioStream'].read())
        print(f"Audio saved to {output_file_path}.")

    except Exception as e:
        print(f"Error in synthesize: {e}")
        sys.exit(1)

def upload_to_s3(file_path, bucket, key):
    try:
        s3 = boto3.client(
            's3',
            region_name='us-east-1',
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
        )
        print("Initialized S3 client.")

        s3.upload_file(file_path, bucket, key)
        print(f"Uploaded {file_path} to s3://{bucket}/{key}.")

    except Exception as e:
        print(f"Error in upload_to_s3: {e}")
        sys.exit(1)

if __name__ == "__main__":
    output_mp3 = "output.mp3"
    synthesize("speech.txt", output_mp3)
    s3_bucket = os.environ['S3_BUCKET_NAME']
    s3_key = os.environ['S3_UPLOAD_KEY']
    upload_to_s3(output_mp3, s3_bucket, s3_key)
