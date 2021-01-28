terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
    }
  }
}

variable "instance_name_input" {
  type = string
  default = "terraform-instance"
}

provider "google" {
  version = "3.5.0"

  credentials = file("Credentials.json") #Provide the name of your GCP credentials here

  project = "my-new-project" #Provide your project name here
  region  = "us-central1"
  zone    = "us-central1-c"
}

resource "google_compute_network" "vpc_network" {
  name = var.instance_name_input
}

resource "google_compute_instance" "vm_instance" {
  name         = "terraform-instance"
  machine_type = "f1-micro"
  tags         = ["web", "dev"]
  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-1804-lts"
    }
  }

  network_interface {
    network = google_compute_network.vpc_network.name
    access_config {
    }
  }
}

resource "google_compute_firewall" "ssh-rule" {
  name = "demo-ssh"
  network = google_compute_network.vpc_network.name
  allow {
    protocol = "tcp"
    ports = ["22"]
  }
  target_tags = [var.instance_name_input]
  source_ranges = ["0.0.0.0/0"]
}

output "public_ip" {
  value = google_compute_instance.vm_instance.network_interface.0.access_config.0.nat_ip
}

output "instance_name" {
  value = google_compute_instance.vm_instance.name
}
