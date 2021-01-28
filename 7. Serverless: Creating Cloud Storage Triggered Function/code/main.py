import os
import tempfile # To create a temporary resized file before uploading
from google.cloud import storage
from wand.image import Image  # To resize image
# Add any imports that you may need, but make sure to update requirements.txt
invoke_bucketname = os.getenv('MY_BUCKET')
client = storage.Client()


def resize_image_storage(event, context):

    # Get the file that has been uploaded to GCS
    bucket = client.get_bucket(invoke_bucketname)
    f = event['name']
    if "testimage" in f and "resized_" not in f:
        blob = bucket.get_blob(f)
        imagedata = blob.download_as_string()
        # Create a new image object and resample it
        with tempfile.NamedTemporaryFile() as fp:
            name = fp.name
            fp.write(imagedata) # Write a byte string using fp.write()
            fp.seek(0) # Go to the start of the file
            newimage = fp.read()

        newimage = Image(blob=imagedata)
        newimage.sample(300,300)
        # Upload the resampled image to the other bucket
        bucket = client.get_bucket(invoke_bucketname)
        newblob = bucket.blob('resized_' + f)     
        newblob.upload_from_string(newimage.make_blob())

    return "Success"
