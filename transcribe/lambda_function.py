import boto3
import time

def getS3ObjectId(event):
    Records = event['Records']
    for eventItem in Records:
        Key = eventItem['s3']['object']['key']
        Bucket = eventItem['s3']['bucket']['name']
    s3 = boto3.client('s3')
    mediaUrl = 'https://s3.amazonaws.com/' + str(Bucket) + '/' + str(Key)
    return mediaUrl

def createTranscription(mediaUrl):
    client = boto3.client('transcribe')
    response = client.start_transcription_job(
        TranscriptionJobName='LambdaTest' + str(time.time()),
        LanguageCode='en-US',
        MediaSampleRateHertz=44100,
        MediaFormat='mp3',
        Media={
            'MediaFileUri': mediaUrl
        }
    )
    return response

def lambda_handler(event, context):
    mediaUrl = getS3ObjectId(event)
    print(createTranscription(mediaUrl))
    return 'Hello from Lambda'
