# Provisioning Infrastructure with Terraform

This exercise introduces the concepts of Infrastructure as a Code (IaaC) through a hands-on task using Terraform, a popular tool for provisioning infrastructure. The goal is to deploy a virtual machine (VM) on Google Cloud Platform (GCP).

VM creation
    It creates a VM instance that uses an Ubuntu 18.04 image. The VM instance name should be set through an input variable called instance_name_input.
    
VM information

    The configuration returns two output values:

        instance_name, as the instance name of the newly-created VM;
        public_ip, as the public IP of the newly-created VM.

Network access and GCP

    The created instance will allow SSH access.
