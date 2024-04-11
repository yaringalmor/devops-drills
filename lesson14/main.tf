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
  access_key = "AKIAVBOY4QDZ2EJ2LFSF"
  secret_key = "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"
}

data "aws_key_pair" "web_server_key_pair" {
  key_name           = "web-server-1"
}

data "aws_security_group" "network-security-group" {
  id        = "sg-0cc34486b87a7deb7"
}

resource "aws_instance" "web-server" {
    count = 30
    ami = "ami-0900fe555666598a2"
    instance_type           = "t2.micro"
    key_name                = data.aws_key_pair.web_server_key_pair.key_name
    vpc_security_group_ids  = [data.aws_security_group.network-security-group.id]
    
    tags = {
        Name = "web-server-${count.index}"
    }
}