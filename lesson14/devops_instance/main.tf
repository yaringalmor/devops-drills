terraform {
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~> 5.0"
        }
    }
}

provider "aws" {
    region = "us-east-2"
}

resource "aws_instance" "web-server" {
    ami = "ami-0900fe555666598a2"
    instance_type           = "t2.micro"
    
    tags = {
        Name = var.instance_name
    }
}

variable "instance_name" {
    type = string
    description = "web-server name"
}

output "instace_public_ip" {
    value = aws_instance.web-server.public_ip
}