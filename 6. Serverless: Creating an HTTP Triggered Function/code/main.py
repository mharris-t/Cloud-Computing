import os
import tempfile    # To create temporary file before uploading to bucket
from google.cloud import storage
from flask import escape
invoke_bucketname = os.getenv('MY_BUCKET')
# Add any imports that you may need, but make sure to update requirements.txt

def create_file_http(request):
    client = storage.Client()
    request_json = request.get_json(silent=True)

    if request_json and 'fileid' in request_json:

        with tempfile.NamedTemporaryFile() as fp:
            name = fp.name
            fp.write(b'Cloud Assignment code was here') # Write a byte string using fp.write()
            fp.seek(0) # Go to the start of the file
            content = fp.read()

        fileid = request_json['fileid']
        #Invoke bucket
        bucket=client.get_bucket(invoke_bucketname);  
        blob_file=bucket.blob(fileid)
        blob_file.upload_from_string(content, content_type="text/plain")

        return "200"

    else:
        error_msg = "File creation failed"
        return ("400", '{}'.format(escape(error_msg)))
