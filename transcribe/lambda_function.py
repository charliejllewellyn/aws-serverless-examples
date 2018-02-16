import boto3

def getS3ObjectId(event):
    Records = event['Records']
    for eventItem in Records:
        Key = eventItem['s3']['object']['key']
        Bucket = eventItem['s3']['bucket']['name']
    s3 = boto3.client('s3')
    mediaUrl = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': Bucket,
            'Key': Key
        }
    )
    print(mediaUrl)
    return mediaUrl

def createTranscription(mediaUrl):
    client = boto3.client('transcribe')
    response = client.start_transcription_job(
        TranscriptionJobName='LambdaTest',
        LanguageCode='en-US',
        MediaSampleRateHertz=42000,
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
