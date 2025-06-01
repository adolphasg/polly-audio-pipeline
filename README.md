# Pixel Learning Audio Pipeline

##  What This Project Does

Automatically converts course text to speech and uploads it to Amazon S3 using AWS Polly.

##  How to Use

### 1. Modify Text

Edit `speech.txt` with your course content.

### 2. Make a Pull Request

Create a branch and push your changes. Open a pull request.

- This will run the `on_pull_request.yml` workflow.
- Audio will be uploaded to: `s3://pixel-learning-audio/polly-audio/beta.mp3`

### 3. Merge to Main

After review, merge the PR.

- This runs `on_merge.yml`.
- Audio will be uploaded to: `s3://pixel-learning-audio/polly-audio/prod.mp3`

##  AWS Setup

- Create an IAM user with `AmazonPollyFullAccess` and `AmazonS3FullAccess`.
- Create an S3 bucket and note its name.
- Save AWS keys as GitHub secrets.

##  Verifying Audio Uploads

1. Go to your [S3 Console](https://s3.console.aws.amazon.com/s3).
2. Open your bucket.
3. Navigate to the `polly-audio/` folder.
4. Download and listen to `beta.mp3` or `prod.mp3`.



