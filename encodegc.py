# encodegc.py
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="//Users/bakseo3060/Desktop/nepp_git/nepp-577ae-firebase-adminsdk-rwenk-5abd189704.json"
from google.cloud import storage

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    print("되ㅏ라고좀")
    print(storage_client)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))

for num in range(1, 21):
    download_blob('nepp-577ae.appspot.com','AutoBlur_scan_%d.jpeg'%num, '/Users/bakseo3060/Desktop/nepp_git/face-recognition-opencv/dataset/nepp_input/AutoBlur_scan_%d.jpeg'%num)