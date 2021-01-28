provider "google" {
  credentials = file("credentials.json")
  project = "my-cloud-project"
  region  = "europe-west1"
  zone    = "europe-west1-a"
}

resource "google_storage_bucket" "storage_triggered_bucket" {
  name = var.storage_trigger_bucket_name
  force_destroy = true
}

resource "google_storage_bucket" "code_bucket" {
  name = var.code_bucket_name
  force_destroy = true
}

resource "google_storage_bucket_object" "archive" {
  name   = "code.zip"
  bucket = google_storage_bucket.code_bucket.name
  source = "./code.zip"
  # NOTE: Source code code.zip must be in the same directory as Terraform configuration
}

resource "google_cloudfunctions_function" "storage_triggered_function" {
  source_archive_bucket = google_storage_bucket.code_bucket.name
  source_archive_object = google_storage_bucket_object.archive.name
  
  runtime = "python37"
  name= "resize_image_storage"

  environment_variables = {
      MY_BUCKET = google_storage_bucket.storage_triggered_bucket.name
  }
  event_trigger {
    event_type = "google.storage.object.finalize"
    resource   = google_storage_bucket.storage_triggered_bucket.name
  }
}

# Bucket name for input bucket which triggers storage_triggered_function
variable "storage_trigger_bucket_name" {
  description = "The name to use for the storage bucket that is the trigger for the cloud function"
  type        = string
}

# Bucket name for code archive
variable "code_bucket_name" {
  description = "The name to use for the bucket where code.zip will be uploaded"
  type        = string
}
