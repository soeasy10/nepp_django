# importgc.py

from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))
#text 파일로 올리는 것으로 수정해야함!
upload_blob('nepp-577ae.appspot.com', '/Users/bakseo3060/Desktop/nepp/nepp_django/input/Autoblur_gaussian.jpeg', 'Autoblur_gaussian.jpeg')
upload_blob('nepp-577ae.appspot.com', '/Users/bakseo3060/Desktop/nepp/nepp_django/input/Autoblur_mosaic.jpeg', 'Autoblur_mosaic.jpeg')