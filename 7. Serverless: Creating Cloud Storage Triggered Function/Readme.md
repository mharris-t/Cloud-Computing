# Serverless: Creating Cloud Storage Triggered Function

This exercise creates a Cloud Storage-triggered function named **resize_image_storage** that is called when a file is uploaded to the Storage bucket **google_storage_bucket.storage_triggered_bucket** (the bucket is created in the sample Terraform configuration). The function will resize the uploaded image and resize it to (300 x 300) pixels, i.e., with both height and width set to 300. The resized image is then uploaded to the same bucket with the filename **resized_<original_file>.<ext>**.

For example, assume a Storage Bucket called **YOUR_TRIGGER_BUCKET_NAME** exists in your Google Cloud Project. When an image called **testimage.jpg** is uploaded to **YOUR_TRIGGER_BUCKET_NAME**, the Cloud Function **resize_image_storage** must be triggered. The function resizes the uploaded image and uploads a new image called **resized_testimage.jpg** to the same bucket.
