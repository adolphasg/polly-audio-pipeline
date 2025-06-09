import boto3
import os

def synthesize_speech():
    # Get AWS credentials and S3 configuration from environment variables
    aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    bucket_name = os.getenv("AWS_S3_BUCKET")
    upload_key = os.getenv("S3_UPLOAD_KEY")
# Raise an error if any required environment variables are missing
    if not all([aws_access_key, aws_secret_key, bucket_name, upload_key]):
        raise EnvironmentError("Missing required environment variables.")
# Create a Polly client for text-to-speech
    polly = boto3.client('polly', region_name='us-east-1',
                         aws_access_key_id=aws_access_key,
                         aws_secret_access_key=aws_secret_key)
# Create an S3 client to upload the audio file
    s3 = boto3.client('s3',
                      aws_access_key_id=aws_access_key,
                      aws_secret_access_key=aws_secret_key)
# Read the input text from a local file
    with open("speech.txt", "r") as f:
        text = f.read()
# Send text to Polly and get the synthesized speech in MP3 format
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId="Joanna"  # You can change the voice if desired
    )
# Save the audio stream returned by Polly to a local MP3 file
    output_file = "output.mp3"
    with open(output_file, 'wb') as f:
        f.write(response['AudioStream'].read())
# Upload the generated MP3 file to the specified S3 bucket
    s3.upload_file(
        Filename=output_file,
        Bucket=bucket_name,
        Key=upload_key
    )
# Run the function if this script is executed directly
if __name__ == "__main__":
    synthesize_speech()