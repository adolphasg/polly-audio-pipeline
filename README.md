# Pixel Learning Audio Pipeline

## What This Project Does

This project automates the process of converting course text into speech using Amazon Polly and uploads the resulting audio file to an Amazon S3 bucket. It uses GitHub Actions to handle automation for both beta testing and production publishing.

## How It Works

### 1. Modify Text

Update the `speech.txt` file with the content you want to convert into speech.

### 2. Make a Pull Request

- Create a new branch, make your changes, and open a pull request to the `main` branch.
- This will trigger the **Beta Workflow** (`on_pull_request.yml`).
- The generated audio will be uploaded to the S3 path:  
  `s3://pixel-learning-audio/polly-audio/beta.mp3`

### 3. Merge to Main

- After your pull request is approved and merged into `main`, the **Production Workflow** (`on_merge.yml`) will run.
- The audio file will be uploaded to:  
  `s3://pixel-learning-audio/polly-audio/prod.mp3`

## Setup Instructions

### Requirements

- Python 3.10
- An AWS account with permissions for Amazon Polly and Amazon S3
- A GitHub repository with GitHub Actions enabled

##  Verifying Audio Uploads

1. Go to your [S3 Console](https://s3.console.aws.amazon.com/s3).
2. Open your bucket.
3. Navigate to the `polly-audio/` folder.
4. Download and listen to `beta.mp3` or `prod.mp3`.



