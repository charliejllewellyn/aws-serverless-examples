import os
import os.path
import sys
import boto3

print(boto3.__version__)

def createTranscription(event):
    client = boto3.client('transcribe')
    response = client.start_transcription_job(
        TranscriptionJobName='LambdaTest',
        LanguageCode='en-US',
        MediaSampleRateHertz=42000,
        MediaFormat='mp3',
        Media={
            'MediaFileUri': 'https://s3.amazonaws.com/aws-interview-transcoded/Meeting+Recording+-+Llewellyn%2C+Charlie+Instant+Meeting.mp3'
        }
    )
    return response

def lambda_handler(event, context):
    print(createTranscription(event))
    return 'Hello from Lambda'

createTranscription('test')
