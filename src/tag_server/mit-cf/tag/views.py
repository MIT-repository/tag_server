from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import os, boto3
from .models import Song 
from .DeepAudioClassification.main import predict
# Create your views here.

service_name = os.environ.get('service_name')
endpoint_url = os.environ.get('s3_url')
region_name = os.environ.get('reg')
access_key = os.environ.get('s3_key')
secret_key = os.environ.get('secret_key')

s3 = boto3.client(service_name, endpoint_url=endpoint_url, aws_access_key_id=access_key,
                      aws_secret_access_key=secret_key)
base = os.path.dirname( os.path.abspath( __file__ ) )
master_path = base+'/DeepAudioClassification/Prediction/'
#master_path = '/'

def tag(requests, bucket,folder, name):
    down_name = folder+'/'+name
    local_file_path = master_path + 'Raw/{}'.format(name)
#    try:
 #       song = Song.objects.get(name=name,bucket=bucket)
    print("download :", local_file_path)
    #except Exception as err:
        #print(err)
    s3.download_file(bucket, down_name, local_file_path)
        #song = Song.objects.create(name=name, bucket=bucket, genre='test')

    genre = predict()
    os.remove(local_file_path)
    os.remove(master_path+'Slices/predict/*')




    return JsonResponse(
        {
            "bucket": bucket,
            "name": name,
            "genre": genre
        },
        safe=False, json_dumps_params={'ensure_ascii': False}
    )
