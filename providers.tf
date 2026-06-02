#Make the providers.tf for terraform
terraform {
    #Version of terrform CLI
    required_version = ">= 1.5.0"  #Version of terrform CLI

   #Setup Terraform for aws 
    required_providers {   
    aws= {
        source = "hashicorp/aws"
        version = "~> 5.0"
    }
  }
}

#Setup AWS Engine
  provider "aws"{
    region = "us-east-2"
  }