# Serverless: Creating an HTTP Triggered Function

This exercise introduces the concepts of serverless functions through hands-on tasks involving different types of triggers. The goal is to deploy functions on Google Cloud Platform (GCP) that respond to HTTP events.

The task creates an HTTP-triggered function named __create_file_http__. The function is triggered when an HTTP request with a JSON body containing fileid is sent to the trigger endpoint. The function must create a file called __< fileid >__ in the Google Storage bucket (already created by the Terraform configuration). The function must also return an HTTP status code of 200.

For example, when an HTTP request is sent with:
 ```
 curl -X POST https://europe-west1-YOUR_PROJECT_ID.cloudfunctions.net/create_file_http \
             -H "Content-Type:application/json" --data '{"fileid":"c9880557-cb3d-49dd-8ab2-1a13b4f2b575"}'
 ```
 
 The function will create a file called __c9880557-cb3d-49dd-8ab2-1a13b4f2b575__ in the Google Storage bucket called __google_storage_bucket.output_bucket.name__ created in the Terraform configuration. This can be achieved by using an environment variable in the function that is set in the Terraform configuration to the __google_storage_bucket.output_bucket.name__.
