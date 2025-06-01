import boto3
import os

def synthesize_speech():
    # Load environment variables
    aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    bucket_name = os.getenv("AWS_S3_BUCKET")

    # Setup clients
    polly = boto3.client('polly', region_name='us-east-1',
                         aws_access_key_id=aws_access_key,
                         aws_secret_access_key=aws_secret_key)

    s3 = boto3.client('s3',
                      aws_access_key_id=aws_access_key,
                      aws_secret_access_key=aws_secret_key)

    # Read text file
    with open("speech.txt", "r") as f:
        text = f.read()

    # Synthesize speech
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId="Joanna"
    )

    # Save output
    output_file = "output.mp3"
    with open(output_file, 'wb') as f:
        f.write(response['AudioStream'].read())

    # Upload to S3
    s3.upload_file(
        Filename=output_file,
        Bucket=bucket_name,
        Key="polly-audio/beta.mp3"
    )

if __name__ == "__main__":
    synthesize_speech()