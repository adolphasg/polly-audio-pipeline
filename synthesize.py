import boto3
import os

def synthesize(text_file_path, output_file_path):
    print("Reading text from file:", text_file_path)
    with open(text_file_path, 'r') as file:
        text = file.read()

    print("Initializing Amazon Polly client...")
    polly = boto3.client(
        'polly',
        region_name='us-east-1',
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
    )

    print("Sending request to synthesize speech...")
    response = polly.synthesize_speech(Text=text, OutputFormat='mp3', VoiceId='Joanna')

    print("Saving synthesized speech to:", output_file_path)
    with open(output_file_path, 'wb') as file:
        file.write(response['AudioStream'].read())

    print("Speech synthesis complete.")

def upload_to_s3(file_path, bucket, key):
    print(f"Uploading {file_path} to s3://{bucket}/{key}...")
    s3 = boto3.client(
        's3',
        region_name='us-east-1',
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
    )
    s3.upload_file(file_path, bucket, key)
    print("Upload complete.")

if __name__ == "__main__":
    output_mp3 = "output.mp3"
    synthesize("speech.txt", output_mp3)
    s3_bucket = os.environ['S3_BUCKET_NAME']
    s3_key = os.environ['S3_UPLOAD_KEY']
    upload_to_s3(output_mp3, s3_bucket, s3_key)
